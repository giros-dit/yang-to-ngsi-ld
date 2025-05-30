package tid;

import com.google.gson.Gson;
// GOOGLE JSON imports
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonSyntaxException;

// FLINK imports
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.api.common.functions.FilterFunction;
import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.common.serialization.DeserializationSchema;
import org.apache.flink.api.common.serialization.SerializationSchema;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.partitioner.FlinkKafkaPartitioner;
import org.apache.kafka.common.TopicPartition;
import org.apache.flink.connector.base.DeliveryGuarantee;
import org.apache.flink.connector.kafka.sink.KafkaRecordSerializationSchema;
import org.apache.flink.connector.kafka.sink.KafkaSink;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;

// GENERATED-SOURCES imports
import org.opendaylight.yang.gen.v1.http.data.aggregator.com.ns.netflow.aggregated.rev220302.PerDecimal;
import org.opendaylight.yang.gen.v1.http.data.aggregator.com.ns.netflow.rev211008.NetflowBuilder;
import org.opendaylight.yang.gen.v1.http.data.aggregator.com.ns.netflow.rev211008.netflow.ExportPacketBuilder;
import org.opendaylight.yang.gen.v1.http.data.aggregator.com.ns.netflow.rev211008.netflow.export.packet.FlowDataRecord;
import org.opendaylight.yang.gen.v1.http.data.aggregator.com.ns.netflow.aggregated.rev220302.FlowDataRecord1;
import org.opendaylight.yang.gen.v1.http.data.aggregator.com.ns.netflow.aggregated.rev220302.FlowDataRecord1Builder;
import org.opendaylight.yang.gen.v1.http.data.aggregator.com.ns.netflow.rev211008.netflow.export.packet.FlowDataRecordBuilder;
import org.opendaylight.yang.gen.v1.urn.ietf.params.xml.ns.yang.ietf.yang.types.rev230123.Timestamp;

// YANG-TOOLS imports
import org.opendaylight.mdsal.binding.dom.codec.api.BindingNormalizedNodeSerializer;
import org.opendaylight.mdsal.binding.dom.codec.impl.BindingCodecContext;
import org.opendaylight.mdsal.binding.runtime.spi.BindingRuntimeHelpers;
import org.opendaylight.mdsal.binding.spec.reflect.BindingReflections;
import org.opendaylight.yang.gen.v1.http.data.aggregator.com.ns.netflow.rev211008.Netflow;
import org.opendaylight.yangtools.yang.binding.InstanceIdentifier;
import org.opendaylight.yangtools.yang.common.QName;
import org.opendaylight.yangtools.yang.common.Uint32;
import org.opendaylight.yangtools.yang.data.api.YangInstanceIdentifier;
import org.opendaylight.yangtools.yang.data.api.schema.MapEntryNode;
import org.opendaylight.yangtools.yang.data.api.schema.NormalizedNode;
import org.opendaylight.yangtools.yang.data.api.schema.stream.NormalizedNodeStreamWriter;
import org.opendaylight.yangtools.yang.data.api.schema.stream.NormalizedNodeWriter;
import org.opendaylight.yangtools.yang.data.codec.gson.*;
import org.opendaylight.yangtools.yang.data.codec.xml.XMLStreamNormalizedNodeStreamWriter;
import org.opendaylight.yangtools.yang.data.codec.xml.XmlParserStream;
import org.opendaylight.yangtools.yang.data.impl.schema.ImmutableNormalizedNodeStreamWriter;
import org.opendaylight.yangtools.yang.data.impl.schema.NormalizedNodeResult;
import org.opendaylight.yangtools.yang.model.api.EffectiveModelContext;
import org.opendaylight.yangtools.yang.model.api.SchemaNode;
import org.opendaylight.yangtools.yang.model.api.SchemaPath;
import org.xml.sax.SAXException;
import javax.xml.stream.XMLStreamException;

// JAVA imports
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Map.Entry;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.stream.FactoryConfigurationError;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLOutputFactory;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamReader;
import javax.xml.stream.XMLStreamWriter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.StringReader;
import java.io.StringWriter;
import java.lang.IllegalArgumentException;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Flink Streaming Application that make stateless aggregation on goflow2
 * traffic received in XML format.
 *
 * <p>
 * To create bindings of your application, run 'mvn generate-bindings' on the
 * command line.
 * Do not forget to make sure your "yangFilesPath" points to the yang-models
 * folder
 *
 * <p>
 * To package your application into a JAR file for execution, run
 * 'mvn package' on the command line.
 *
 * <p>
 * If you change the name of the main class (with the public static void
 * main(String[] args))
 * method, change the respective entry in the POM.xml file (simply search for
 * 'mainClass').
 */
public class NetflowAggregator {

	public static class netflowAggregateMap implements MapFunction<String, String> {

		@Override
		public String map(String input) throws Exception {

			// get Object of class Netflow from the input (XML)
			StringReader stringReader = new StringReader(input);
			XMLStreamReader xmlReader = XMLInputFactory.newInstance().createXMLStreamReader(stringReader);
			Netflow netflowv9_netflow = null;
			try {
				netflowv9_netflow = input2NetflowClass(xmlReader);

			} catch (IllegalStateException | IllegalArgumentException e) {
				System.out.println("EXCEPTION: Malformed INPUT (XML)");
				e.printStackTrace();
			} catch (Exception e) {
				System.out.println("Unknown exception:");
				e.printStackTrace();
			}

			String serialized = "";
			if (netflowv9_netflow != null) {
				// make aggregations
				Netflow newnetflow = netflowAggregation(netflowv9_netflow);

				// serialize to string
				serialized = serialize2JSONstring(newnetflow);

			}

			return serialized;
		}
	}

	public static void main(String[] args) throws Exception {

		if (args.length == 5) {
			multitenants(args);
		} else {
			if (args.length == 3) {
				singletenant(args);
			} else {
				System.exit(1);
			}
		}

	}

	public static void singletenant(String[] args) throws Exception {

		// GET EXECUTION ENVIRONMENT
		StreamExecutionEnvironment environment = StreamExecutionEnvironment.getExecutionEnvironment();

		// KAFKA CONSUMER
		KafkaSource<String> consumer = KafkaSource.<String>builder()
				.setTopics(args[1])
				.setGroupId("netflow-aggregation-group")
				.setBootstrapServers(args[0])
				.setStartingOffsets(OffsetsInitializer.latest())
				.setValueOnlyDeserializer((DeserializationSchema<String>) new SimpleStringSchema())
				.build();

		// KAFKA PRODUCER
		KafkaSink<String> producer = KafkaSink
				.<String>builder()
				.setBootstrapServers(args[0])
				.setRecordSerializer(KafkaRecordSerializationSchema.builder()
						.setTopic(args[2])
						.setValueSerializationSchema((SerializationSchema<String>) new SimpleStringSchema())
						.build())
				.setDeliverGuarantee(DeliveryGuarantee.AT_LEAST_ONCE)
				.build();

		// SOURCE DATASTREAM
		DataStreamSource<String> dss = environment.fromSource(consumer, WatermarkStrategy.noWatermarks(),
				"Kafka Source");

		DataStream<String> serializedds = dss.map(new netflowAggregateMap()).filter(new FilterFunction<String>() {
			// make sure only valid values are processed, then filter by permissible
			// sources (netflow)
			@Override
			public boolean filter(String value) throws Exception {
				// if empty do not return
				return !value.equals("");
			}
		});

		serializedds.sinkTo(producer);

		environment.execute("netflowAggregator");
	}

	public static void multitenants(String[] args) throws Exception {

		int topic_partition = getPartition(args[3], args[4]);

		FlinkKafkaPartitioner<String> customPartitioner = new MyCustomPartitioner(topic_partition);

		// GET EXECUTION ENVIRONMENT
		StreamExecutionEnvironment environment = StreamExecutionEnvironment.getExecutionEnvironment();

		final HashSet<TopicPartition> consumerPartitionSet = new HashSet<>(Arrays.asList(
				new TopicPartition(args[1], topic_partition)));

		// KAFKA CONSUMER
		KafkaSource<String> consumer = KafkaSource.<String>builder()
				.setPartitions(consumerPartitionSet)
				.setGroupId("netflow-aggregation-group")
				.setBootstrapServers(args[0])
				.setStartingOffsets(OffsetsInitializer.latest())
				.setValueOnlyDeserializer((DeserializationSchema<String>) new SimpleStringSchema())
				.build();

		// KAFKA PRODUCER
		KafkaSink<String> producer = KafkaSink
				.<String>builder()
				.setBootstrapServers(args[0])
				.setRecordSerializer(KafkaRecordSerializationSchema.builder()
						.setTopic(args[2])
						.setPartitioner(customPartitioner)
						.setValueSerializationSchema((SerializationSchema<String>) new SimpleStringSchema())
						.build())
				.setDeliverGuarantee(DeliveryGuarantee.AT_LEAST_ONCE)
				.build();

		// SOURCE DATASTREAM
		DataStreamSource<String> dss = environment.fromSource(consumer, WatermarkStrategy.noWatermarks(),
				"Kafka Source");

		DataStream<String> serializedds = dss.map(new netflowAggregateMap()).filter(new FilterFunction<String>() {
			// make sure only valid json values are processed, then filter by permissible
			// sources (netflow)
			@Override
			public boolean filter(String value) throws Exception {
				// if empty do not return
				return !value.equals("");
			}
		});

		serializedds.sinkTo(producer);

		environment.execute("netflowAggregator");
	}

	/**
	 * Method for obtaining the topic partition associated with a tenant id by
	 * making a call to the tenant service.
	 * 
	 * @param tenant_service_url
	 * @param tenant_id
	 * @return
	 */
	public static int getPartition(String tenant_service_url, String tenant_id) {
		int topic_partition = 0;
		try {
			// URL of tenant-service
			URL url = new URL(tenant_service_url + tenant_id);

			// Opening HTTP connection
			HttpURLConnection connection = (HttpURLConnection) url.openConnection();
			connection.setConnectTimeout(2000);
			connection.setRequestMethod("GET");

			int responseCode = connection.getResponseCode();

			if (responseCode >= 200 && responseCode <= 299) {
				// Reading server response
				BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
				String line;
				StringBuilder response = new StringBuilder();
				while ((line = reader.readLine()) != null) {
					response.append(line);
				}

				Gson json = new Gson();
				JsonObject jsonObject = json.fromJson(response.toString(), JsonObject.class);
				String partition = jsonObject.get("partition").getAsString();

				reader.close();

				topic_partition = Integer.parseInt(partition);
			} else {
				System.exit(1);
			}

			// Closing connection
			connection.disconnect();
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(1);
		}
		return topic_partition;
	}

	/**
	 * Custom implementation of FlinkKafkaPartitioner
	 */
	public static class MyCustomPartitioner extends FlinkKafkaPartitioner<String> {

		private int partition;

		MyCustomPartitioner(int partition) {
			this.partition = partition;
		}

		@Override
		public int partition(String record, byte[] key, byte[] value, String targetTopic, int[] partitions) {

			return partition;
		}
	}

	private static Netflow netflowAggregation(Netflow netflowv9) {
		// get Object of class Netflow from the input (JSON-IETF)

		List<FlowDataRecord> newlist = new ArrayList<>();
		// iterate over the FlowDataRecord List and create newlist with AUGMENTED
		// aggregations
		for (FlowDataRecord fdr : netflowv9.getExportPacket().getFlowDataRecord()) {

			FlowDataRecordBuilder flowbuilder = new FlowDataRecordBuilder(fdr); // create builder for adding
																				// aggregations

			// create builder for flow aggregations
			FlowDataRecord1Builder fdr1_builder = new FlowDataRecord1Builder();

			// AGGREGATIONS --->
			// FLOW DURATION
			Float flowduration = Float.valueOf(fdr.getLastSwitched().longValue() - fdr.getFirstSwitched().longValue()); // duration
																														// in
																														// milliseconds
			Float durationSeconds = flowduration / 1000; // duration in seconds
			fdr1_builder.setFlowDuration(new Timestamp(Uint32.valueOf(flowduration.intValue())));

			Float temp;

			if (durationSeconds != 0) {

				// BytesInPerSecond
				temp = fdr.getBytesIn().getValue().floatValue() / durationSeconds;
				fdr1_builder.setBytesInPerSecond(PerDecimal.getDefaultInstance(temp.toString()));

				// PktsInPerSecond
				temp = fdr.getPktsIn().getValue().floatValue() / durationSeconds;
				fdr1_builder.setPktsInPerSecond(PerDecimal.getDefaultInstance(temp.toString()));

				// BytesOutPerSecond
				temp = fdr.getBytesOut().getValue().floatValue() / durationSeconds;
				fdr1_builder.setBytesOutPerSecond(PerDecimal.getDefaultInstance(temp.toString()));

				// PktsOutPerSecond
				temp = fdr.getPktsOut().getValue().floatValue() / durationSeconds;
				fdr1_builder.setPktsOutPerSecond(PerDecimal.getDefaultInstance(temp.toString()));
			} else {
				// BytesInPerSecond
				fdr1_builder.setBytesInPerSecond(PerDecimal.getDefaultInstance("0"));
				// PktsInPerSecond
				fdr1_builder.setPktsInPerSecond(PerDecimal.getDefaultInstance("0"));
				// BytesOutPerSecond
				fdr1_builder.setBytesOutPerSecond(PerDecimal.getDefaultInstance("0"));
				// PktsOutPerSecond
				fdr1_builder.setPktsOutPerSecond(PerDecimal.getDefaultInstance("0"));
			}

			if (fdr.getPktsIn().getValue().floatValue() != 0) {
				// BytesInPerPacket
				temp = fdr.getBytesIn().getValue().floatValue() / fdr.getPktsIn().getValue().floatValue();
				fdr1_builder.setBytesInPerPacket(PerDecimal.getDefaultInstance(temp.toString()));
			} else {
				fdr1_builder.setBytesInPerPacket(PerDecimal.getDefaultInstance("0"));
			}

			if (fdr.getPktsOut().getValue().floatValue() != 0) {
				// BytesOutPerPacket
				temp = fdr.getBytesOut().getValue().floatValue() / fdr.getPktsOut().getValue().floatValue();
				fdr1_builder.setBytesOutPerPacket(PerDecimal.getDefaultInstance(temp.toString()));
			} else {
				fdr1_builder.setBytesOutPerPacket(PerDecimal.getDefaultInstance("0"));
			}

			if (fdr.getBytesOut().getValue().floatValue() != 0) {
				// RatioBytesInPerOut
				temp = fdr.getBytesIn().getValue().floatValue() / fdr.getBytesOut().getValue().floatValue();
				fdr1_builder.setRatioBytesInPerOut(PerDecimal.getDefaultInstance(temp.toString()));
			} else {
				fdr1_builder.setRatioBytesInPerOut(PerDecimal.getDefaultInstance("0"));
			}

			if (fdr.getPktsOut().getValue().floatValue() != 0) {
				// RatioPktsInPerOut
				temp = fdr.getPktsIn().getValue().floatValue() / fdr.getPktsOut().getValue().floatValue();
				fdr1_builder.setRatioPktsInPerOut(PerDecimal.getDefaultInstance(temp.toString()));
			} else {
				fdr1_builder.setRatioPktsInPerOut(PerDecimal.getDefaultInstance("0"));
			}
			// <--- AGGREGATIONS

			// build the object into an aggregations FlowDataRecord
			FlowDataRecord1 fdr1 = fdr1_builder.build(); // ready to add to an augmentation
			// Add augmentations to the flowbuilder
			flowbuilder.addAugmentation(fdr1);
			// build new FlowDataRecord
			FlowDataRecord newfdr = flowbuilder.build();

			// change the old FlowDataRecord with the aggregated one
			newlist.add(newfdr);
		}

		// aggregate newlist to old netflowv9 value
		NetflowBuilder nb = new NetflowBuilder(netflowv9);
		ExportPacketBuilder eb = new ExportPacketBuilder(netflowv9.getExportPacket());
		eb.setFlowDataRecord(newlist);
		nb.setExportPacket(eb.build());
		return nb.build();
	}

	// VARIABLES TO SERIALIZE AND DESERIALIZE
	private static final BindingNormalizedNodeSerializer netflow_agg_codec = new BindingCodecContext(
			BindingRuntimeHelpers.createRuntimeContext(
					Netflow.class,
					FlowDataRecord1.class));
	private static final EffectiveModelContext schemaContext = BindingRuntimeHelpers
			.createEffectiveModel(BindingReflections.loadModuleInfos());


	public static Netflow input2NetflowClass(XMLStreamReader xmlReader) {
		Netflow netflowv9 = null;
		try{
			NormalizedNodeResult result = new NormalizedNodeResult();
			NormalizedNodeStreamWriter streamWriter = ImmutableNormalizedNodeStreamWriter.from(result);

			QName qname = QName.create("http://data-aggregator.com/ns/netflow", "2021-10-08", "netflow");

			Optional<org.opendaylight.yangtools.yang.model.api.Module> moduleOptional = schemaContext.findModule(qname.getModule());

			if (moduleOptional.isPresent()) {
				org.opendaylight.yangtools.yang.model.api.Module module = moduleOptional.get();

				Optional<? extends SchemaNode> nodeOptional = module.findDataChildByName(qname);

				if (nodeOptional.isPresent()) {
					SchemaNode parentNode = nodeOptional.get();
					XmlParserStream xmlParser = XmlParserStream.create(streamWriter, schemaContext, parentNode);
					xmlParser.parse(xmlReader);
					NormalizedNode<?, ?> transformedInput = result.getResult();
					InstanceIdentifier<Netflow> netflow_iid = InstanceIdentifier.create(Netflow.class);
					YangInstanceIdentifier netflow_yiid = netflow_agg_codec.toYangInstanceIdentifier(netflow_iid);
					netflowv9 = (Netflow) netflow_agg_codec.fromNormalizedNode(netflow_yiid, transformedInput).getValue();
				}
			}


		} catch(IllegalStateException | XMLStreamException | IllegalArgumentException e){
			System.out.println("EXCEPTION: Malformed INPUT (XML)");
			e.printStackTrace();
		} catch(Exception e){
			System.out.println("Unknown exception:");
			e.printStackTrace();
		}
		
		return netflowv9;

	}

	// CONVERSIONS FROM NETFLOW CLASS TO XML STRING --->

	/**
	 * Performs the actual data conversion.
	 * @param schemaPath
	 * @param data
	 * @return
	 * @throws XMLStreamException
	 * @throws FactoryConfigurationError
	 * @throws ParserConfigurationException
	 * @throws SAXException
	 */
	private static String doConvert(SchemaPath schemaPath, NormalizedNode<?, ?> data)
			throws XMLStreamException, FactoryConfigurationError, ParserConfigurationException, SAXException {
		try (StringWriter writer = new StringWriter()) {
			XMLStreamWriter xmlWriter = XMLOutputFactory.newInstance().createXMLStreamWriter(writer);
			final NormalizedNodeStreamWriter xmlStream = XMLStreamNormalizedNodeStreamWriter.create(xmlWriter,
					schemaContext, schemaPath);
			try (NormalizedNodeWriter nodeWriter = NormalizedNodeWriter.forStreamWriter(xmlStream)) {
				nodeWriter.write(data);
				nodeWriter.flush();
			}
			System.out.println(writer.toString());
			return writer.toString();
		} catch (IOException e) {
			return null;
		}
	}

	private static String serialize2JSONstring(Netflow netflow) {

		InstanceIdentifier<Netflow> iid = InstanceIdentifier.create(Netflow.class);
		JsonObject gson_obj = new JsonObject();
		String xml_obj = new String();
		try {
			Entry<YangInstanceIdentifier, NormalizedNode<?, ?>> normalized = netflow_agg_codec.toNormalizedNode(iid,
					netflow);
			xml_obj = doConvert(schemaContext.getPath(), normalized.getValue());
		} catch (Exception ex) {
			ex.printStackTrace();
			StringWriter errors = new StringWriter();
			ex.printStackTrace(new PrintWriter(errors));
		}

		return xml_obj;

	}

	// <--- CONVERSIONS FROM NETFLOW CLASS TO XML STRING

}
