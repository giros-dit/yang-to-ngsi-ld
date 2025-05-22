import pandas as pd
import matplotlib.pyplot as plt

df_materialization = pd.read_csv('query_tester_materialization_context_broker_performance_measurements.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization: \n")

query_mean_materialization = df_materialization ['query_execution_time'].mean()
query_standard_deviation_materialization  = df_materialization ['query_execution_time'].std()
print("Data materialization - Mean query time:", query_mean_materialization)
print("Data materialization - Query standard deviation:", query_standard_deviation_materialization)
print("\n")

query_reply_mean_materialization = df_materialization ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_materialization  = df_materialization ['processing_time_since_observed_at'].std()
print("Data materialization - Mean query reply time:", query_reply_mean_materialization)
print("Data materialization - Query reply standard deviation:", query_reply_standard_deviation_materialization)
print("\n")

df_virtualization_context_broker = pd.read_csv('query_tester_virtualization_context_broker_performance_measurements.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker): \n")

query_mean_virtualization_context_broker = df_virtualization_context_broker['query_execution_time'].mean()
query_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['query_execution_time'].std()
print("Data virtualization (context broker) - Mean query time:", query_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query standard deviation:", query_standard_deviation_virtualization_context_broker)
print("\n")

query_reply_mean_virtualization_context_broker = df_virtualization_context_broker['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['processing_time_since_observed_at'].std()
print("Data virtualization (context broker) - Mean query reply time:", query_reply_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query reply standard deviation:", query_reply_standard_deviation_virtualization_context_broker)
print("\n")

df_virtualization_context_source = pd.read_csv('query_tester_virtualization_context_source_performance_measurements.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source): \n")

query_mean_virtualization_context_source = df_virtualization_context_source['query_execution_time'].mean()
query_standard_deviation_virtualization_context_source  = df_virtualization_context_source['query_execution_time'].std()
print("Data virtualization (context source) - Mean query time", query_mean_virtualization_context_source)
print("Data virtualization (context source) - Query standard deviation:", query_standard_deviation_virtualization_context_source)
print("\n")

query_reply_mean_virtualization_context_source = df_virtualization_context_source['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_source  = df_virtualization_context_source['processing_time_since_observed_at'].std()
print("Data virtualization (context source) - Mean query reply time", query_reply_mean_virtualization_context_source)
print("Data virtualization (context source) - Query reply standard deviation:", query_reply_standard_deviation_virtualization_context_source)
print("\n")

fig, ax = plt.subplots()

query_plot_materialization = df_materialization.boxplot(column = ['query_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['query_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['query_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean execution time per \n gNMI RPC query operation')
plt.savefig("query_performance_measurements_data_integration.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_reply_plot_materialization = df_materialization.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_reply_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_reply_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean reply time \n per gNMI RPC query operation')
plt.savefig("query_reply_performance_measurements_data_integration.png", format="png", dpi=1500)
