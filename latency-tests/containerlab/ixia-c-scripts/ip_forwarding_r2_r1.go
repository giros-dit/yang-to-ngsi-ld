/*
Test IPv4 Forwarding with
- Endpoints: OTG 10.0.2.2 -----> 10.0.2.1 DUT (r2) 192.168.254.2 -----> 192.168.254.1 DUT (r1) 10.0.1.1 -----> OTG 10.0.1.2
- Static Route on DUT (r2): 10.10.10.0/24 -> 192.168.254.1
- Static Route on DUT (r1): 10.10.10.0/24 -> 10.0.1.2
- TCP flow from OTG: 10.20.20.1 -> 10.10.10.1

To run: go run ipv4_forwarding.go
*/

package main

import (
	"log"
	"time"

	"github.com/open-traffic-generator/snappi/gosnappi"
)

// hostname and interfaces of ixia-c-one node from containerlab topology.
const (
	otgHost  = "https://clab-telemetry-ixiac-lab-ixia-c:8443"
	otgPort1 = "eth1"
	otgPort2 = "eth2"
)

var (
	r1Mac      = "02:00:00:00:01:aa"
	r2Mac      = "02:00:00:00:02:aa"
	r1Ip       = "10.0.1.2"
	r2Ip       = "10.0.2.2"
	r1IpPrefix = uint32(24)
	r2IpPrefix = uint32(24)
	r1IpGw     = "10.0.1.1"
	r2IpGw     = "10.0.2.1"
	pktCount   = 1000
)

func main() {
	api, config := newConfig()

	// push traffic configuration to otgHost
	res, err := api.SetConfig(config)
	checkResponse(res, err)

	// start transmitting configured flows
	ts := api.NewControlState()
	ts.Traffic().FlowTransmit().SetState(gosnappi.StateTrafficFlowTransmitState.START)
	res, err = api.SetControlState(ts)
	checkResponse(res, err)

	// fetch flow metrics and wait for received frame count to be correct
	mr := api.NewMetricsRequest()
	mr.Flow()
	waitFor(
		func() bool {
			res, err := api.GetMetrics(mr)
			checkResponse(res, err)

			fm := res.FlowMetrics().Items()[0]
			return fm.Transmit() == gosnappi.FlowMetricTransmit.STOPPED && fm.FramesRx() == uint64(pktCount)
		},
		10*time.Second,
	)
}

func checkResponse(res interface{}, err error) {
	if err != nil {
		log.Fatal(err) // skipcq: RVV-A0003
	}
	switch v := res.(type) {
	case gosnappi.MetricsResponse:
		log.Printf("Metrics Response:\n%s\n", v)
	case gosnappi.Warning:
		for _, w := range v.Warnings() {
			log.Println("WARNING:", w)
		}
	default:
		log.Fatal("Unknown response type:", v) // skipcq: RVV-A0003
	}
}

func newConfig() (gosnappi.GosnappiApi, gosnappi.Config) {
	// create a new API handle to make API calls against otgHost
	api := gosnappi.NewApi()
	api.NewHttpTransport().SetLocation(otgHost).SetVerify(false)

	// create an empty traffic configuration
	config := api.NewConfig()
	// create traffic endpoints
	p1 := config.Ports().Add().SetName("p1").SetLocation(otgPort1)
	p2 := config.Ports().Add().SetName("p2").SetLocation(otgPort2)

	// create emulated devices (routers) – needed for ARP protocol to work
	r1 := config.Devices().Add().SetName("r1")
	r2 := config.Devices().Add().SetName("r2")

	// device ethernets
	r1Eth := r1.Ethernets().Add().SetName("r1Eth").SetMac(r1Mac)
	r2Eth := r2.Ethernets().Add().SetName("r2Eth").SetMac(r2Mac)

	// connections to test ports
	r1Eth.Connection().SetPortName(p1.Name())
	r2Eth.Connection().SetPortName(p2.Name())

	// device IP configuration
	r1Ip := r1Eth.Ipv4Addresses().Add().
		SetName("r1Ip").
		SetAddress(r1Ip).
		SetPrefix(r1IpPrefix).
		SetGateway(r1IpGw)

	r2Ip := r2Eth.Ipv4Addresses().Add().
		SetName("r2Ip").
		SetAddress(r2Ip).
		SetPrefix(r2IpPrefix).
		SetGateway(r2IpGw)

	// create a flow between r2 and r1
	f1 := config.Flows().Add().SetName("r2.v4.r1")
	f1.TxRx().Device().SetTxNames([]string{r1Ip.Name()})
	f1.TxRx().Device().SetRxNames([]string{r2Ip.Name()})

	// enable per flow metrics tracking
	f1.Metrics().SetEnable(true)
	// set size, count and transmit rate for all packets in the flow
	f1.Size().SetFixed(512)
	f1.Rate().SetPps(10)
	f1.Duration().FixedPackets().SetPackets(uint32(pktCount))

	// configure headers for all packets in the flow
	eth := f1.Packet().Add().Ethernet()
	ip := f1.Packet().Add().Ipv4()
	tcp := f1.Packet().Add().Tcp()

	eth.Src().SetValue(r2Mac)
	eth.Dst().SetChoice("auto")

	ip.Src().SetValue("10.20.20.1")
	ip.Dst().Increment().SetStart("10.10.10.1").SetStep("0.0.0.1").SetCount(5)

	tcp.SrcPort().SetValue(3250)
	tcp.DstPort().Decrement().SetStart(8070).SetStep(2).SetCount(10)

	log.Printf("OTG configuration:\n%s\n", config)
	return api, config
}

func waitFor(fn func() bool, timeout time.Duration) {
	start := time.Now()
	for {
		if fn() {
			return
		}
		if time.Since(start) > timeout {
			log.Fatal("Timeout occurred !") // skipcq: RVV-A0003
		}

		time.Sleep(500 * time.Millisecond)
	}
}
