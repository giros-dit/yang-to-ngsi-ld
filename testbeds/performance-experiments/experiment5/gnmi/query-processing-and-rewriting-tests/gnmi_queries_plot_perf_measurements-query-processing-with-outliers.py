import pandas as pd
import matplotlib.pyplot as plt

df_materialization = pd.read_csv('performance_measurements_operation-gnmi-materialization-1.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 1: \n")

query_operation_mean_materialization = df_materialization ['operation_time'].mean()
query_operation_standard_deviation_materialization  = df_materialization ['operation_time'].std()
print("Data materialization - Mean query operation time:", query_operation_mean_materialization)
print("Data materialization - Query operation standard deviation:", query_operation_standard_deviation_materialization)
print("\n")

query_translation_mean_materialization = df_materialization ['translation_time'].mean()
query_translation_standard_deviation_materialization  = df_materialization ['translation_time'].std()
print("Data materialization - Mean query translation time:", query_translation_mean_materialization)
print("Data materialization - Query translation standard deviation:", query_translation_standard_deviation_materialization)
print("\n")

query_request_mean_materialization = df_materialization ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_materialization  = df_materialization ['processing_time_since_notified_at'].std()
print("Data materialization - Mean query request time:", query_request_mean_materialization)
print("Data materialization - Query request standard deviation:", query_request_standard_deviation_materialization)
print("\n")

df_virtualization_context_broker = pd.read_csv('performance_measurements_operation-gnmi-virtualization-1-cb.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker) - Iteration 1: \n")

query_operation_mean_virtualization_context_broker = df_virtualization_context_broker ['operation_time'].mean()
query_operation_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['operation_time'].std()
print("Data virtualization (context broker) - Mean query operation time:", query_operation_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query operation standard deviation:", query_operation_standard_deviation_virtualization_context_broker)
print("\n")

query_translation_mean_virtualization_context_broker = df_virtualization_context_broker ['translation_time'].mean()
query_translation_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['translation_time'].std()
print("Data virtualization (context broker) - Mean query translation time:", query_translation_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query translation standard deviation:", query_translation_standard_deviation_virtualization_context_broker)
print("\n")

query_request_mean_virtualization_context_broker = df_virtualization_context_broker ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['processing_time_since_notified_at'].std()
print("Data virtualization (context broker) - Mean query request time:", query_request_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query request standard deviation:", query_request_standard_deviation_virtualization_context_broker)
print("\n")

df_virtualization_context_source = pd.read_csv('performance_measurements_operation-gnmi-virtualization-1-cs.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source) - Iteration 1: \n")

query_operation_mean_virtualization_context_source = df_virtualization_context_source ['operation_time'].mean()
query_operation_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['operation_time'].std()
print("Data virtualization (context source) - Mean query operation time", query_operation_mean_virtualization_context_source)
print("Data virtualization (context source) - Query operation standard deviation:", query_operation_standard_deviation_virtualization_context_source)
print("\n")

query_translation_mean_virtualization_context_source = df_virtualization_context_source ['translation_time'].mean()
query_translation_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['translation_time'].std()
print("Data virtualization (context source) - Mean query translation time", query_translation_mean_virtualization_context_source)
print("Data virtualization (context source) - Query translation standard deviation:", query_translation_standard_deviation_virtualization_context_source)
print("\n")

query_request_mean_virtualization_context_source = df_virtualization_context_source ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['processing_time_since_notified_at'].std()
print("Data virtualization (context source) - Mean query request time", query_request_mean_virtualization_context_source)
print("Data virtualization (context source) - Query request standard deviation:", query_request_standard_deviation_virtualization_context_source)
print("\n")

fig, ax = plt.subplots()

query_operation_plot_materialization = df_materialization.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_operation_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_operation_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean execution time per \n gNMI RPC query operation')
plt.savefig("query_operation_performance_measurements_data_integration-iteration-1.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_translation_plot_materialization = df_materialization.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_translation_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_translation_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean translation time per \n gNMI RPC query operation')
plt.savefig("query_translation_performance_measurements_data_integration-iteration-1.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_request_plot_materialization = df_materialization.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_request_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_request_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean request time per \n gNMI RPC query operation')
plt.savefig("query_request_performance_measurements_data_integration-iteration-1.png", format="png", dpi=1500)

df_materialization = pd.read_csv('performance_measurements_operation-gnmi-materialization-2.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 2: \n")

query_operation_mean_materialization = df_materialization ['operation_time'].mean()
query_operation_standard_deviation_materialization  = df_materialization ['operation_time'].std()
print("Data materialization - Mean query operation time:", query_operation_mean_materialization)
print("Data materialization - Query operation standard deviation:", query_operation_standard_deviation_materialization)
print("\n")

query_translation_mean_materialization = df_materialization ['translation_time'].mean()
query_translation_standard_deviation_materialization  = df_materialization ['translation_time'].std()
print("Data materialization - Mean query translation time:", query_translation_mean_materialization)
print("Data materialization - Query translation standard deviation:", query_translation_standard_deviation_materialization)
print("\n")

query_request_mean_materialization = df_materialization ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_materialization  = df_materialization ['processing_time_since_notified_at'].std()
print("Data materialization - Mean query request time:", query_request_mean_materialization)
print("Data materialization - Query request standard deviation:", query_request_standard_deviation_materialization)
print("\n")

df_virtualization_context_broker = pd.read_csv('performance_measurements_operation-gnmi-virtualization-2-cb.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker) - Iteration 2: \n")

query_operation_mean_virtualization_context_broker = df_virtualization_context_broker ['operation_time'].mean()
query_operation_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['operation_time'].std()
print("Data virtualization (context broker) - Mean query operation time:", query_operation_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query operation standard deviation:", query_operation_standard_deviation_virtualization_context_broker)
print("\n")

query_translation_mean_virtualization_context_broker = df_virtualization_context_broker ['translation_time'].mean()
query_translation_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['translation_time'].std()
print("Data virtualization (context broker) - Mean query translation time:", query_translation_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query translation standard deviation:", query_translation_standard_deviation_virtualization_context_broker)
print("\n")

query_request_mean_virtualization_context_broker = df_virtualization_context_broker ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['processing_time_since_notified_at'].std()
print("Data virtualization (context broker) - Mean query request time:", query_request_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query request standard deviation:", query_request_standard_deviation_virtualization_context_broker)
print("\n")

df_virtualization_context_source = pd.read_csv('performance_measurements_operation-gnmi-virtualization-2-cs.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source) - Iteration 2: \n")

query_operation_mean_virtualization_context_source = df_virtualization_context_source ['operation_time'].mean()
query_operation_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['operation_time'].std()
print("Data virtualization (context source) - Mean query operation time", query_operation_mean_virtualization_context_source)
print("Data virtualization (context source) - Query operation standard deviation:", query_operation_standard_deviation_virtualization_context_source)
print("\n")

query_translation_mean_virtualization_context_source = df_virtualization_context_source ['translation_time'].mean()
query_translation_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['translation_time'].std()
print("Data virtualization (context source) - Mean query translation time", query_translation_mean_virtualization_context_source)
print("Data virtualization (context source) - Query translation standard deviation:", query_translation_standard_deviation_virtualization_context_source)
print("\n")

query_request_mean_virtualization_context_source = df_virtualization_context_source ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['processing_time_since_notified_at'].std()
print("Data virtualization (context source) - Mean query request time", query_request_mean_virtualization_context_source)
print("Data virtualization (context source) - Query request standard deviation:", query_request_standard_deviation_virtualization_context_source)
print("\n")

fig, ax = plt.subplots()

query_operation_plot_materialization = df_materialization.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_operation_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_operation_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean execution time per \n gNMI RPC query operation')
plt.savefig("query_operation_performance_measurements_data_integration-iteration-2.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_translation_plot_materialization = df_materialization.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_translation_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_translation_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean translation time per \n gNMI RPC query operation')
plt.savefig("query_translation_performance_measurements_data_integration-iteration-2.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_request_plot_materialization = df_materialization.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_request_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_request_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean request time per \n gNMI RPC query operation')
plt.savefig("query_request_performance_measurements_data_integration-iteration-2.png", format="png", dpi=1500)

df_materialization = pd.read_csv('performance_measurements_operation-gnmi-materialization-3.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 3: \n")

query_operation_mean_materialization = df_materialization ['operation_time'].mean()
query_operation_standard_deviation_materialization  = df_materialization ['operation_time'].std()
print("Data materialization - Mean query operation time:", query_operation_mean_materialization)
print("Data materialization - Query operation standard deviation:", query_operation_standard_deviation_materialization)
print("\n")

query_translation_mean_materialization = df_materialization ['translation_time'].mean()
query_translation_standard_deviation_materialization  = df_materialization ['translation_time'].std()
print("Data materialization - Mean query translation time:", query_translation_mean_materialization)
print("Data materialization - Query translation standard deviation:", query_translation_standard_deviation_materialization)
print("\n")

query_request_mean_materialization = df_materialization ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_materialization  = df_materialization ['processing_time_since_notified_at'].std()
print("Data materialization - Mean query request time:", query_request_mean_materialization)
print("Data materialization - Query request standard deviation:", query_request_standard_deviation_materialization)
print("\n")

df_virtualization_context_broker = pd.read_csv('performance_measurements_operation-gnmi-virtualization-3-cb.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker) - Iteration 3: \n")

query_operation_mean_virtualization_context_broker = df_virtualization_context_broker ['operation_time'].mean()
query_operation_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['operation_time'].std()
print("Data virtualization (context broker) - Mean query operation time:", query_operation_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query operation standard deviation:", query_operation_standard_deviation_virtualization_context_broker)
print("\n")

query_translation_mean_virtualization_context_broker = df_virtualization_context_broker ['translation_time'].mean()
query_translation_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['translation_time'].std()
print("Data virtualization (context broker) - Mean query translation time:", query_translation_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query translation standard deviation:", query_translation_standard_deviation_virtualization_context_broker)
print("\n")

query_request_mean_virtualization_context_broker = df_virtualization_context_broker ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['processing_time_since_notified_at'].std()
print("Data virtualization (context broker) - Mean query request time:", query_request_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query request standard deviation:", query_request_standard_deviation_virtualization_context_broker)
print("\n")

df_virtualization_context_source = pd.read_csv('performance_measurements_operation-gnmi-virtualization-3-cs.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source) - Iteration 3: \n")

query_operation_mean_virtualization_context_source = df_virtualization_context_source ['operation_time'].mean()
query_operation_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['operation_time'].std()
print("Data virtualization (context source) - Mean query operation time", query_operation_mean_virtualization_context_source)
print("Data virtualization (context source) - Query operation standard deviation:", query_operation_standard_deviation_virtualization_context_source)
print("\n")

query_translation_mean_virtualization_context_source = df_virtualization_context_source ['translation_time'].mean()
query_translation_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['translation_time'].std()
print("Data virtualization (context source) - Mean query translation time", query_translation_mean_virtualization_context_source)
print("Data virtualization (context source) - Query translation standard deviation:", query_translation_standard_deviation_virtualization_context_source)
print("\n")

query_request_mean_virtualization_context_source = df_virtualization_context_source ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['processing_time_since_notified_at'].std()
print("Data virtualization (context source) - Mean query request time", query_request_mean_virtualization_context_source)
print("Data virtualization (context source) - Query request standard deviation:", query_request_standard_deviation_virtualization_context_source)
print("\n")

fig, ax = plt.subplots()

query_operation_plot_materialization = df_materialization.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_operation_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_operation_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean execution time per \n gNMI RPC query operation')
plt.savefig("query_operation_performance_measurements_data_integration-iteration-3.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_translation_plot_materialization = df_materialization.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_translation_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_translation_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean translation time per \n gNMI RPC query operation')
plt.savefig("query_translation_performance_measurements_data_integration-iteration-3.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_request_plot_materialization = df_materialization.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_request_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_request_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean request time per \n gNMI RPC query operation')
plt.savefig("query_request_performance_measurements_data_integration-iteration-3.png", format="png", dpi=1500)

materialization_files = [
    'performance_measurements_operation-gnmi-materialization-1.csv',
    'performance_measurements_operation-gnmi-materialization-2.csv',
    'performance_measurements_operation-gnmi-materialization-3.csv'
]

df_materialization_queries_all = pd.concat(
    [pd.read_csv(file) for file in materialization_files],
    ignore_index=True
)

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization: \n")

query_operation_mean_materialization_all = df_materialization_queries_all ['operation_time'].mean()
query_operation_standard_deviation_materialization_all  = df_materialization_queries_all ['operation_time'].std()
print("Data materialization - Mean query operation time:", query_operation_mean_materialization_all)
print("Data materialization - Query operation standard deviation:", query_operation_standard_deviation_materialization_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_materialization_queries_all ['operation_time']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_materialization_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
materialization_operation_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_translation_mean_materialization_all = df_materialization_queries_all ['translation_time'].mean()
query_translation_standard_deviation_materialization_all  = df_materialization_queries_all ['translation_time'].std()
print("Data materialization - Mean query translation time:", query_translation_mean_materialization_all)
print("Data materialization - Query translation standard deviation:", query_translation_standard_deviation_materialization_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_materialization_queries_all ['translation_time']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_materialization_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
materialization_translation_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_request_mean_materialization_all = df_materialization_queries_all ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_materialization_all  = df_materialization_queries_all ['processing_time_since_notified_at'].std()
print("Data materialization - Mean query request time:", query_request_mean_materialization_all)
print("Data materialization - Query request standard deviation:", query_request_standard_deviation_materialization_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_materialization_queries_all ['processing_time_since_notified_at']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_materialization_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
materialization_request_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

virtualization_cb_files = [
    'performance_measurements_operation-gnmi-virtualization-1-cb.csv',
    'performance_measurements_operation-gnmi-virtualization-2-cb.csv',
    'performance_measurements_operation-gnmi-virtualization-3-cb.csv'
]

df_virtualization_cb_queries_all = pd.concat(
    [pd.read_csv(file) for file in virtualization_cb_files],
    ignore_index=True
)

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker): \n")

query_operation_mean_virtualization_context_broker_all = df_virtualization_cb_queries_all ['operation_time'].mean()
query_operation_standard_deviation_virtualization_context_broker_all  = df_virtualization_cb_queries_all ['operation_time'].std()
print("Data virtualization (context broker) - Mean query operation time:", query_operation_mean_virtualization_context_broker_all)
print("Data virtualization (context broker) - Query operation standard deviation:", query_operation_standard_deviation_virtualization_context_broker_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cb_queries_all ['operation_time']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_virtualization_cb_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
virtualization_cb_operation_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_translation_mean_virtualization_context_broker_all = df_virtualization_cb_queries_all ['translation_time'].mean()
query_translation_standard_deviation_virtualization_context_broker_all  = df_virtualization_cb_queries_all ['translation_time'].std()
print("Data virtualization (context broker) - Mean query translation time:", query_translation_mean_virtualization_context_broker_all)
print("Data virtualization (context broker) - Query translation standard deviation:", query_translation_standard_deviation_virtualization_context_broker_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cb_queries_all ['translation_time']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_virtualization_cb_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
virtualization_cb_translation_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_request_mean_virtualization_context_broker_all = df_virtualization_cb_queries_all ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_virtualization_context_broker_all  = df_virtualization_cb_queries_all ['processing_time_since_notified_at'].std()
print("Data virtualization (context broker) - Mean query request time:", query_request_mean_virtualization_context_broker_all)
print("Data virtualization (context broker) - Query request standard deviation:", query_request_standard_deviation_virtualization_context_broker_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cb_queries_all ['processing_time_since_notified_at']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_virtualization_cb_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
virtualization_cb_request_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

virtualization_cs_files = [
    'performance_measurements_operation-gnmi-virtualization-1-cs.csv',
    'performance_measurements_operation-gnmi-virtualization-2-cs.csv',
    'performance_measurements_operation-gnmi-virtualization-3-cs.csv'
]

df_virtualization_cs_queries_all = pd.concat(
    [pd.read_csv(file) for file in virtualization_cs_files],
    ignore_index=True
)

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source): \n")

query_operation_mean_virtualization_context_source_all = df_virtualization_cs_queries_all ['operation_time'].mean()
query_operation_standard_deviation_virtualization_context_source_all  = df_virtualization_cs_queries_all ['operation_time'].std()
print("Data virtualization (context source) - Mean query operation time", query_operation_mean_virtualization_context_source)
print("Data virtualization (context source) - Query operation standard deviation:", query_operation_standard_deviation_virtualization_context_source)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cs_queries_all ['operation_time']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_virtualization_cs_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
virtualization_cs_operation_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_translation_mean_virtualization_context_source_all = df_virtualization_cs_queries_all ['translation_time'].mean()
query_translation_standard_deviation_virtualization_context_source_all  = df_virtualization_cs_queries_all ['translation_time'].std()
print("Data virtualization (context source) - Mean query translation time", query_translation_mean_virtualization_context_source_all)
print("Data virtualization (context source) - Query translation standard deviation:", query_translation_standard_deviation_virtualization_context_source_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cs_queries_all ['translation_time']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_virtualization_cs_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
virtualization_cs_translation_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_request_mean_virtualization_context_source_all = df_virtualization_cs_queries_all ['processing_time_since_notified_at'].mean()
query_request_standard_deviation_virtualization_context_source_all  = df_virtualization_cs_queries_all ['processing_time_since_notified_at'].std()
print("Data virtualization (context source) - Mean query request time", query_request_mean_virtualization_context_source_all)
print("Data virtualization (context source) - Query request standard deviation:", query_request_standard_deviation_virtualization_context_source_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cs_queries_all ['processing_time_since_notified_at']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_virtualization_cs_queries_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
virtualization_cs_request_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

fig, ax = plt.subplots()

query_operation_plot_materialization_queries_all = df_materialization_queries_all.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_operation_plot_virtualization_cs_queries_all = df_virtualization_cs_queries_all.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_operation_plot_virtualization_cb_queries_all = df_virtualization_cb_queries_all.boxplot(column = ['operation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['Materialization', 'Virtualization_CS', 'Virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean execution time per \n gNMI RPC query operation')

# Texto estadístico
text_outliers_operation_materialization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % materialization_operation_outlier_percentage
))

text_outliers_cs_operation_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cs_operation_outlier_percentage
))

text_outliers_cb_operation_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cb_operation_outlier_percentage
))

# Estilo del recuadro
props = dict(boxstyle='round', facecolor='white', alpha=0.8)

# Añadir ambos recuadros en esquinas opuestas
ax.text(0.05, 0.05, text_outliers_operation_materialization , transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', bbox=props, color='blue')

ax.text(0.5, 0.95, text_outliers_cs_operation_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props, color='grey')

ax.text(0.95, 0.05, text_outliers_cb_operation_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', horizontalalignment='right', bbox=props)


plt.savefig("query_operation_performance_measurements_data_integration-with-outliers.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_translation_plot_materialization_queries_all = df_materialization_queries_all.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_translation_plot_virtualization_cs_queries_all = df_virtualization_cs_queries_all.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_translation_plot_virtualization_cb_queries_all = df_virtualization_cb_queries_all.boxplot(column = ['translation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['Materialization', 'Virtualization_CS', 'Virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean translation time per \n gNMI RPC query operation')

# Texto estadístico
text_outliers_translation_materialization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % materialization_translation_outlier_percentage
))

text_outliers_cs_translation_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cs_translation_outlier_percentage
))

text_outliers_cb_translation_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cb_translation_outlier_percentage
))

# Estilo del recuadro
props = dict(boxstyle='round', facecolor='white', alpha=0.8)

# Añadir ambos recuadros en esquinas opuestas
ax.text(0.05, 0.95, text_outliers_translation_materialization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', bbox=props, color='blue')

ax.text(0.5, 0.95, text_outliers_cs_translation_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props, color='grey')

ax.text(0.95, 0.05, text_outliers_cb_translation_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', horizontalalignment='right', bbox=props)


plt.savefig("query_translation_performance_measurements_data_integration-with-outliers.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_request_plot_materialization_all = df_materialization_queries_all.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_request_plot_virtualization_context_source_all = df_virtualization_cs_queries_all.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_request_plot_virtualization_context_broker_all = df_virtualization_cb_queries_all.boxplot(column = ['processing_time_since_notified_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['Materialization', 'Virtualization_CS', 'Virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean request time per \n gNMI RPC query operation')

# Texto estadístico
text_outliers_request_materialization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % materialization_request_outlier_percentage
))

text_outliers_cs_request_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cs_request_outlier_percentage
))

text_outliers_cb_request_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cb_request_outlier_percentage
))

# Estilo del recuadro
props = dict(boxstyle='round', facecolor='white', alpha=0.8)

# Añadir ambos recuadros en esquinas opuestas
ax.text(0.05, 0.04, text_outliers_request_materialization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', bbox=props, color='blue')

ax.text(0.5, 0.96, text_outliers_cs_request_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props, color='grey')

ax.text(0.95, 0.04, text_outliers_cb_request_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', horizontalalignment='right', bbox=props)

plt.savefig("query_request_performance_measurements_data_integration-with-outliers.png", format="png", dpi=1500)