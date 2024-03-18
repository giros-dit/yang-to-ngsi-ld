package upm.dit.giros;

import java.io.IOException;
import java.io.PrintWriter;
import java.io.StringReader;
import java.io.StringWriter;
import java.io.Writer;
import java.util.Map.Entry;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.stream.FactoryConfigurationError;
import javax.xml.stream.XMLOutputFactory;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamWriter;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import java.util.*;

import org.opendaylight.mdsal.binding.dom.codec.api.BindingNormalizedNodeSerializer;
import org.opendaylight.mdsal.binding.dom.codec.impl.BindingCodecContext;
import org.opendaylight.mdsal.binding.runtime.spi.BindingRuntimeHelpers;
import org.opendaylight.mdsal.binding.spec.reflect.BindingReflections;
import org.opendaylight.yangtools.yang.binding.InstanceIdentifier;
import org.opendaylight.yangtools.yang.data.api.YangInstanceIdentifier;
import org.opendaylight.yangtools.yang.data.api.schema.MapEntryNode;
import org.opendaylight.yangtools.yang.data.api.schema.NormalizedNode;
import org.opendaylight.yangtools.yang.data.api.schema.stream.NormalizedNodeStreamWriter;
import org.opendaylight.yangtools.yang.data.api.schema.stream.NormalizedNodeWriter;
import org.opendaylight.yangtools.yang.data.codec.gson.JSONCodecFactory;
import org.opendaylight.yangtools.yang.data.codec.gson.JSONCodecFactorySupplier;
import org.opendaylight.yangtools.yang.data.codec.gson.JSONNormalizedNodeStreamWriter;
import org.opendaylight.yangtools.yang.data.codec.gson.JsonWriterFactory;
import org.opendaylight.yangtools.yang.model.api.EffectiveModelContext;
import org.opendaylight.yangtools.yang.model.api.SchemaPath;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

import org.opendaylight.yangtools.yang.data.codec.xml.XMLStreamNormalizedNodeStreamWriter;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.Networks;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.NetworkId;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.NodeId;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.NetworksBuilder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.networks.Network;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.networks.NetworkBuilder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.networks.NetworkKey;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.networks.network.Node;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.networks.network.NodeBuilder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.rev180226.networks.network.NodeKey;

import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.Network1Builder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.Network1;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.Node1Builder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.Node1;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.LinkId;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.TpId;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.Link;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.LinkBuilder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.LinkKey;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.link.Source;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.link.SourceBuilder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.link.Destination;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.link.DestinationBuilder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.node.TerminationPoint;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.node.TerminationPointBuilder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.network.topology.rev180226.networks.network.node.TerminationPointKey;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonParser;
import com.google.gson.stream.JsonWriter;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.lang.String;

/**
 * Java application based on the YANG Tools library for parsing data from network topology descriptor based on the 
 * ContainerLab simulation testbed and mapping it to YANG-compliant data according to the ietf-network and ietf-network YANG data models.
 */
public class TopologyDriver {

    public static void main(String[] args) throws Exception {

        String network_id = new String();
        ArrayList<String> nodes_id = new ArrayList<String>();

        //JSON parser object to parse read file
        JsonParser jsonParser = new JsonParser();
        
        Map<String, ArrayList<String>> node_termination_points = new HashMap<String, ArrayList<String>>();
        Map<String, ArrayList<String>> node_links = new HashMap<String, ArrayList<String>>();

        NetworksBuilder networks_builder = new NetworksBuilder();
        Map<NetworkKey, Network> map_networks = new HashMap<NetworkKey, Network>();
        NetworkBuilder network_builder = new NetworkBuilder();
        Network1Builder network_aug_builder = new Network1Builder();
        Map<NodeKey, Node> map_nodes = new HashMap<NodeKey, Node>();
        NodeBuilder node_builder = new NodeBuilder();
        Node1Builder node_aug_builder = new Node1Builder();
        Map<LinkKey, Link> map_links = new HashMap<LinkKey, Link>();
        LinkBuilder link_builder = new LinkBuilder();
        SourceBuilder link_source_builder = new SourceBuilder();
        DestinationBuilder link_destination_builder = new DestinationBuilder();
        Map<TerminationPointKey, TerminationPoint> map_tp = new HashMap<TerminationPointKey, TerminationPoint> ();
        TerminationPointBuilder tp_builder = new TerminationPointBuilder();
         
        File input_file = new File("src/main/resources/containerlab-topology-data.json");
        System.out.println(input_file.getAbsolutePath());
        try (FileReader reader = new FileReader(input_file.getAbsolutePath())){
            
            //Read JSON file
            Object obj = jsonParser.parseReader(reader);
 
            JsonObject topo = (JsonObject) obj;

            network_id = topo.get("name").getAsString();

            network_builder.setNetworkId(NetworkId.getDefaultInstance(network_id));

            JsonObject nodes = (JsonObject) topo.getAsJsonObject("nodes");

            for (Map.Entry<String, JsonElement> entry : nodes.entrySet()) {
                nodes_id.add(entry.getKey().toString());
			}

            JsonArray links = (JsonArray) topo.get("links");

            for (int i = 0; i < nodes_id.size(); i++){
                ArrayList<String> n_links = new ArrayList<String>();
                ArrayList<String> n_tp = new ArrayList<String>();
                for(int j = 0; j < links.size(); j++) {
                    JsonObject link = links.get(j).getAsJsonObject();
                    JsonObject link_tp_a = link.get("a").getAsJsonObject();
                    JsonObject link_tp_z = link.get("z").getAsJsonObject();
                    for (Map.Entry<String, JsonElement> entry : link.entrySet()){
                        if (nodes_id.get(i).equals(entry.getValue().getAsJsonObject().get("node").getAsString())){
                            if (entry.getKey().equals("a")){
                                link_source_builder.setSourceNode(NodeId.getDefaultInstance(link_tp_a.get("node").getAsString()));
                                //node_builder.setNodeId(NodeId.getDefaultInstance(link_tp_a.get("node").getAsString()));
                                link_source_builder.setSourceTp((Object)link_tp_a.get("interface").getAsString());
                                link_destination_builder.setDestNode(NodeId.getDefaultInstance(link_tp_z.get("node").getAsString()));
                                link_destination_builder.setDestTp((Object)link_tp_z.get("interface").getAsString());
                                tp_builder.setTpId(TpId.getDefaultInstance(link_tp_a.get("interface").getAsString()));

                                n_tp.add(link_tp_a.get("interface").getAsString());
                                n_links.add(link_tp_a.get("node").getAsString()+","+link_tp_a.get("interface").getAsString()+","+link_tp_z.get("node").getAsString()+","+link_tp_z.get("interface").getAsString());
                            } else {
                                link_source_builder.setSourceNode(NodeId.getDefaultInstance(link_tp_z.get("node").getAsString()));
                                //node_builder.setNodeId(NodeId.getDefaultInstance(link_tp_z.get("node").getAsString()));
                                link_source_builder.setSourceTp((Object)link_tp_z.get("interface").getAsString());
                                link_destination_builder.setDestNode(NodeId.getDefaultInstance(link_tp_a.get("node").getAsString()));
                                link_destination_builder.setDestTp((Object)link_tp_a.get("interface").getAsString());
                                tp_builder.setTpId(TpId.getDefaultInstance(link_tp_z.get("interface").getAsString()));

                                n_tp.add(link_tp_z.get("interface").getAsString());
                                n_links.add(link_tp_z.get("node").getAsString()+","+link_tp_z.get("interface").getAsString()+","+link_tp_a.get("node").getAsString()+","+link_tp_a.get("interface").getAsString());
                            }

                            TerminationPoint tp = tp_builder.build();
                            map_tp.put(tp.key(), tp);
                            Source link_source = link_source_builder.build();
                            Destination link_destination = link_destination_builder.build();

                            link_builder.setLinkId(LinkId.getDefaultInstance(link_tp_a.get("node").getAsString()+"-"+link_tp_a.get("interface").getAsString()+"-"+link_tp_z.get("node").getAsString()+"-"+link_tp_z.get("interface").getAsString()));
                            link_builder.setSource(link_source);
                            link_builder.setDestination(link_destination);
                            Link link_instance = link_builder.build();
                            map_links.put(link_instance.key(), link_instance);
                        }
                    }
                }
                node_aug_builder.setTerminationPoint(map_tp);
                Node1 node_aug = node_aug_builder.build();
                node_builder.setNodeId((NodeId.getDefaultInstance(nodes_id.get(i))));
                node_builder.addAugmentation(node_aug);
                Node node = node_builder.build();
                map_nodes.put(node.key(),node);

                node_termination_points.put(nodes_id.get(i), n_tp);
                node_links.put(nodes_id.get(i), n_links);
            }

            network_aug_builder.setLink(map_links);
            Network1 network_aug = network_aug_builder.build();
            network_builder.addAugmentation(network_aug);
            network_builder.setNode(map_nodes);
            Network network = network_builder.build();
            map_networks.put(network.key(), network);
            networks_builder.setNetwork(map_networks);
            

            System.out.println("\nNETWORKS BUILDER: " + networks_builder.build().toString());

            final Networks networks = networks_builder.build();

            InstanceIdentifier<Networks> iid = InstanceIdentifier.create(Networks.class);

            System.out.println("\nNetworks InstanceIdentifier (iid): " + iid);

            JsonObject network_topology_json = new JsonObject();

            String network_topology_xml = new String();
		
            try {
                BindingNormalizedNodeSerializer codec = new BindingCodecContext(BindingRuntimeHelpers.createRuntimeContext());
                Entry<YangInstanceIdentifier, NormalizedNode<?, ?>> normalized = codec.toNormalizedNode(iid, networks);
                network_topology_json = doConvert(schemaContext.getPath(), normalized.getValue());
                network_topology_xml = doConvertXML(schemaContext.getPath(), normalized.getValue());
            } catch (Exception ex) {
                    ex.printStackTrace();
                    StringWriter errors = new StringWriter();
                    ex.printStackTrace(new PrintWriter(errors));
                    LOG.error(errors.toString());
            }

            //System.out.println("\nJSON Network Topology: \n" + network_topology_json.toString());

            Gson json_format = new GsonBuilder().setPrettyPrinting().create();

            System.out.println("\nJSON Network Topology: \n" + json_format.toJson(network_topology_json));

            File output_file_json = new File("src/main/resources/topology-data-compliant-yang.json");
            BufferedWriter writer_json = new BufferedWriter(new FileWriter(output_file_json.getAbsoluteFile()));
            writer_json.write(json_format.toJson(network_topology_json));
            writer_json.close();

            //System.out.println("\nXML Network Topology: \n" + network_topology_xml);

            InputSource src = new InputSource(new StringReader(network_topology_xml));
            Document document = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(src);
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            transformerFactory.setAttribute("indent-number", 2);
            Transformer transformer = TransformerFactory.newInstance().newTransformer();
            transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
            transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, true ? "yes" : "no");
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            //transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "2");
            Writer transformer_output = new StringWriter();
            transformer.transform(new DOMSource(document),new StreamResult(transformer_output));
            network_topology_xml = transformer_output.toString();

            System.out.println("\nXML Network Topology: \n" + network_topology_xml);

            File output_file_xml = new File("src/main/resources/topology-data-compliant-yang.xml");
            BufferedWriter writer_xml = new BufferedWriter(new FileWriter(output_file_xml.getAbsoluteFile()));
            writer_xml.write(network_topology_xml);
            writer_xml.close();

            System.out.println("\nNETWORK ID: " + network_id);

            System.out.println("\nNODES ID: " + nodes_id.toString());
            
            System.out.println("\nNODE TERMINATION POINTS: ");

            Iterator it_node_tps = node_termination_points.keySet().iterator();
            while (it_node_tps.hasNext()){
                String key = (String) it_node_tps.next();
                System.out.println("Node: " + key + " -> Termination Points: " + node_termination_points.get(key));
            }

            System.out.println("\nNODE LINKS: ");

            Iterator it_node_links = node_links.keySet().iterator();
            while (it_node_links.hasNext()){
                String key = (String) it_node_links.next();
                System.out.println("Node: " + key + " -> Links: " + node_links.get(key));
            }
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Schema context initialization
    // Code borrowed from:
    // https://github.com/opendaylight/jsonrpc/blob/1331a9f73db2fe308e3bbde00ff42359431dbc7f/
    // binding-adapter/src/main/java/org/opendaylight/jsonrpc/binding/EmbeddedRpcInvocationAdapter.java#L38
    private static final EffectiveModelContext schemaContext = BindingRuntimeHelpers
            .createEffectiveModel(BindingReflections.loadModuleInfos());

    // Code borrowed from:
    // https://git.opendaylight.org/gerrit/gitweb?p=jsonrpc.git;a=blob_plain;f=impl/src/
    // main/java/org/opendaylight/jsonrpc/impl/
    // JsonConverter.java;h=ea8069c67ece073e3d9febb694c4e15b01238c10;hb=3ea331d0e57712654d9ecbf2ae2a46cb0ce02d31
    private static final String JSON_IO_ERROR = "I/O problem in JSON codec";
    private static final String XML_IO_ERROR = "I/O problem in XML codec";
    private static final Logger LOG = LogManager.getLogger(TopologyDriver.class);
    private static final JSONCodecFactorySupplier CODEC_SUPPLIER = JSONCodecFactorySupplier.RFC7951;
    private static final JsonParser PARSER = new JsonParser();

    /**
     * Performs the actual JSON data conversion.
     *
     * @param schemaPath - schema path for data
     * @param data       - Normalized Node
     * @return data converted as a JsonObject
     */
    private static JsonObject doConvert(SchemaPath schemaPath, NormalizedNode<?, ?> data) {
        try (StringWriter writer = new StringWriter();
                JsonWriter jsonWriter = JsonWriterFactory.createJsonWriter(writer)) {
            final JSONCodecFactory codecFactory = CODEC_SUPPLIER.getShared(schemaContext);
            final NormalizedNodeStreamWriter jsonStream = (data instanceof MapEntryNode)
                    ? JSONNormalizedNodeStreamWriter.createNestedWriter(codecFactory, schemaPath, null, jsonWriter)
                    : JSONNormalizedNodeStreamWriter.createExclusiveWriter(codecFactory, schemaPath, null, jsonWriter);
            try (NormalizedNodeWriter nodeWriter = NormalizedNodeWriter.forStreamWriter(jsonStream)) {
                nodeWriter.write(data);
                nodeWriter.flush();
            }
            return PARSER.parse(writer.toString()).getAsJsonObject();
        } catch (IOException e) {
            LOG.error(JSON_IO_ERROR, e);
            return null;
        }
    }
    
    /**
     * Performs the actual XML data conversion.
     * @param schemaPath
     * @param data
     * @return
     * @throws XMLStreamException
     * @throws FactoryConfigurationError
     * @throws ParserConfigurationException
     * @throws SAXException
     */
    private static String doConvertXML(SchemaPath schemaPath, NormalizedNode<?, ?> data) throws XMLStreamException, FactoryConfigurationError, ParserConfigurationException, SAXException {
        try (StringWriter writer = new StringWriter()) {
            XMLStreamWriter xmlWriter = XMLOutputFactory.newInstance().createXMLStreamWriter(writer);
            final NormalizedNodeStreamWriter xmlStream = XMLStreamNormalizedNodeStreamWriter.create(xmlWriter,schemaContext, schemaPath);
            try (NormalizedNodeWriter nodeWriter = NormalizedNodeWriter.forStreamWriter(xmlStream)) {
                nodeWriter.write(data);
                nodeWriter.flush();
            }
            return writer.toString(); 
        } catch (IOException e) {
            LOG.error(XML_IO_ERROR, e);
            return null;
        }
    }
}