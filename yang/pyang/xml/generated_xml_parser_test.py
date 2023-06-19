import sys
import xml.etree.ElementTree as et
import subprocess
import pdb
    
xml_file = sys.argv[1]
    
tree = et.parse(xml_file)
    
root = tree.getroot()

name = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}name")

print(name[0].text)

description = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}description")

print(description[0].text)

type = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}type")

print(type[0].text)

enabled = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled")

print(enabled[0].text)

linkUpDownTrapEnable = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}link-up-down-trap-enable")

print(linkUpDownTrapEnable[0].text)

adminStatus = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}admin-status")

print(adminStatus[0].text)

operStatus = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}oper-status")

print(operStatus[0].text)

lastChange = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}last-change")

print(lastChange[0].text)

ifIndex = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}if-index")

print(ifIndex[0].text)

physAddress = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}phys-address")

print(physAddress[0].text)

higherLayerIf = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}higher-layer-if")

print(higherLayerIf[0].text)

lowerLayerIf = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}lower-layer-if")

print(lowerLayerIf[0].text)

speed = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}speed")

print(speed[0].text)

discontinuityTime = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}discontinuity-time")

print(discontinuityTime[0].text)

inOctets = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-octets")

print(inOctets[0].text)

inUnicastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unicast-pkts")

print(inUnicastPkts[0].text)

inBroadcastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-broadcast-pkts")

print(inBroadcastPkts[0].text)

inMulticastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-multicast-pkts")

print(inMulticastPkts[0].text)

inDiscards = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-discards")

print(inDiscards[0].text)

inErrors = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-errors")

print(inErrors[0].text)

inUnknownProtos = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unknown-protos")

print(inUnknownProtos[0].text)

outOctets = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-octets")

print(outOctets[0].text)

outUnicastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-unicast-pkts")

print(outUnicastPkts[0].text)

outBroadcastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-broadcast-pkts")

print(outBroadcastPkts[0].text)

outMulticastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-multicast-pkts")

print(outMulticastPkts[0].text)

outDiscards = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-discards")

print(outDiscards[0].text)

outErrors = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-errors")

print(outErrors[0].text)
