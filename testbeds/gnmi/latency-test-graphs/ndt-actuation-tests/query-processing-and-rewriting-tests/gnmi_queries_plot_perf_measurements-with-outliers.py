import pandas as pd
import matplotlib.pyplot as plt

df_materialization = pd.read_csv('performance_measurements-gnmi-materialization-1.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 1: \n")

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

df_virtualization_context_broker = pd.read_csv('performance_measurements-gnmi-virtualization-1-cb.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker) - Iteration 1: \n")

query_mean_virtualization_context_broker = df_virtualization_context_broker ['query_execution_time'].mean()
query_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['query_execution_time'].std()
print("Data virtualization (context broker) - Mean query time:", query_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query standard deviation:", query_standard_deviation_virtualization_context_broker)
print("\n")

query_reply_mean_virtualization_context_broker = df_virtualization_context_broker ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['processing_time_since_observed_at'].std()
print("Data virtualization (context broker) - Mean query reply time:", query_reply_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query reply standard deviation:", query_reply_standard_deviation_virtualization_context_broker)
print("\n")

df_virtualization_context_source = pd.read_csv('performance_measurements-gnmi-virtualization-1-cs.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source) - Iteration 1: \n")

query_mean_virtualization_context_source = df_virtualization_context_source ['query_execution_time'].mean()
query_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['query_execution_time'].std()
print("Data virtualization (context source) - Mean query time", query_mean_virtualization_context_source)
print("Data virtualization (context source) - Query standard deviation:", query_standard_deviation_virtualization_context_source)
print("\n")

query_reply_mean_virtualization_context_source = df_virtualization_context_source ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['processing_time_since_observed_at'].std()
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
plt.savefig("query_performance_measurements_data_integration-iteration-1.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_reply_plot_materialization = df_materialization.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_reply_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_reply_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean reply time per \n  gNMI RPC query operation')
plt.savefig("query_reply_performance_measurements_data_integration-iteration-1.png", format="png", dpi=1500)

df_materialization = pd.read_csv('performance_measurements-gnmi-materialization-2.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 2: \n")

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

df_virtualization_context_broker = pd.read_csv('performance_measurements-gnmi-virtualization-2-cb.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker) - Iteration 2: \n")

query_mean_virtualization_context_broker = df_virtualization_context_broker ['query_execution_time'].mean()
query_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['query_execution_time'].std()
print("Data virtualization (context broker) - Mean query time:", query_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query standard deviation:", query_standard_deviation_virtualization_context_broker)
print("\n")

query_reply_mean_virtualization_context_broker = df_virtualization_context_broker ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['processing_time_since_observed_at'].std()
print("Data virtualization (context broker) - Mean query reply time:", query_reply_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query reply standard deviation:", query_reply_standard_deviation_virtualization_context_broker)
print("\n")

df_virtualization_context_source = pd.read_csv('performance_measurements-gnmi-virtualization-2-cs.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source) - Iteration 2: \n")

query_mean_virtualization_context_source = df_virtualization_context_source ['query_execution_time'].mean()
query_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['query_execution_time'].std()
print("Data virtualization (context source) - Mean query time", query_mean_virtualization_context_source)
print("Data virtualization (context source) - Query standard deviation:", query_standard_deviation_virtualization_context_source)
print("\n")

query_reply_mean_virtualization_context_source = df_virtualization_context_source ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['processing_time_since_observed_at'].std()
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
plt.savefig("query_performance_measurements_data_integration-iteration-2.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_reply_plot_materialization = df_materialization.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_reply_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_reply_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean reply time per \n  gNMI RPC query operation')
plt.savefig("query_reply_performance_measurements_data_integration-iteration-2.png", format="png", dpi=1500)

df_materialization = pd.read_csv('performance_measurements-gnmi-materialization-3.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 3: \n")

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

df_virtualization_context_broker = pd.read_csv('performance_measurements-gnmi-virtualization-3-cb.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker) - Iteration 3: \n")

query_mean_virtualization_context_broker = df_virtualization_context_broker ['query_execution_time'].mean()
query_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['query_execution_time'].std()
print("Data virtualization (context broker) - Mean query time:", query_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query standard deviation:", query_standard_deviation_virtualization_context_broker)
print("\n")

query_reply_mean_virtualization_context_broker = df_virtualization_context_broker ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_broker  = df_virtualization_context_broker ['processing_time_since_observed_at'].std()
print("Data virtualization (context broker) - Mean query reply time:", query_reply_mean_virtualization_context_broker)
print("Data virtualization (context broker) - Query reply standard deviation:", query_reply_standard_deviation_virtualization_context_broker)
print("\n")

df_virtualization_context_source = pd.read_csv('performance_measurements-gnmi-virtualization-3-cs.csv')

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source) - Iteration 3: \n")

query_mean_virtualization_context_source = df_virtualization_context_source ['query_execution_time'].mean()
query_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['query_execution_time'].std()
print("Data virtualization (context source) - Mean query time", query_mean_virtualization_context_source)
print("Data virtualization (context source) - Query standard deviation:", query_standard_deviation_virtualization_context_source)
print("\n")

query_reply_mean_virtualization_context_source = df_virtualization_context_source ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_source  = df_virtualization_context_source ['processing_time_since_observed_at'].std()
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
plt.savefig("query_performance_measurements_data_integration-iteration-3.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_reply_plot_materialization = df_materialization.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_reply_plot_virtualization_context_source = df_virtualization_context_source.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_reply_plot_virtualization_context_broker = df_virtualization_context_broker.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean reply time per \n  gNMI RPC query operation')
plt.savefig("query_reply_performance_measurements_data_integration-iteration-3.png", format="png", dpi=1500)

materialization_files = [
    'performance_measurements-gnmi-materialization-1.csv',
    'performance_measurements-gnmi-materialization-2.csv',
    'performance_measurements-gnmi-materialization-3.csv'
]

df_materialization_queries_all = pd.concat(
    [pd.read_csv(file) for file in materialization_files],
    ignore_index=True
)

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data materialization: \n")

query_mean_materialization_all = df_materialization_queries_all ['query_execution_time'].mean()
query_standard_deviation_materialization_all  = df_materialization_queries_all ['query_execution_time'].std()
print("Data materialization - Mean query time:", query_mean_materialization_all)
print("Data materialization - Query standard deviation:", query_standard_deviation_materialization_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_materialization_queries_all ['query_execution_time']
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
materialization_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_reply_mean_materialization_all = df_materialization_queries_all ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_materialization_all  = df_materialization_queries_all ['processing_time_since_observed_at'].std()
print("Data materialization - Mean query reply time:", query_reply_mean_materialization_all)
print("Data materialization - Query reply standard deviation:", query_reply_standard_deviation_materialization_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_materialization_queries_all ['processing_time_since_observed_at']
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
materialization_reply_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

virtualization_cb_files = [
    'performance_measurements-gnmi-virtualization-1-cb.csv',
    'performance_measurements-gnmi-virtualization-2-cb.csv',
    'performance_measurements-gnmi-virtualization-3-cb.csv'
]

df_virtualization_cb_queries_all = pd.concat(
    [pd.read_csv(file) for file in virtualization_cb_files],
    ignore_index=True
)

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Broker): \n")

query_mean_virtualization_context_broker_all = df_virtualization_cb_queries_all ['query_execution_time'].mean()
query_standard_deviation_virtualization_context_broker_all  = df_virtualization_cb_queries_all ['query_execution_time'].std()
print("Data virtualization (context broker) - Mean query time:", query_mean_virtualization_context_broker_all)
print("Data virtualization (context broker) - Query standard deviation:", query_standard_deviation_virtualization_context_broker_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cb_queries_all ['query_execution_time']
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
virtualization_cb_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_reply_mean_virtualization_context_broker_all = df_virtualization_cb_queries_all ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_broker_all  = df_virtualization_cb_queries_all ['processing_time_since_observed_at'].std()
print("Data virtualization (context broker) - Mean query reply time:", query_reply_mean_virtualization_context_broker_all)
print("Data virtualization (context broker) - Query reply standard deviation:", query_reply_standard_deviation_virtualization_context_broker_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cb_queries_all ['processing_time_since_observed_at']
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
virtualization_cb_reply_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

virtualization_cs_files = [
    'performance_measurements-gnmi-virtualization-1-cs.csv',
    'performance_measurements-gnmi-virtualization-2-cs.csv',
    'performance_measurements-gnmi-virtualization-3-cs.csv'
]

df_virtualization_cs_queries_all = pd.concat(
    [pd.read_csv(file) for file in virtualization_cs_files],
    ignore_index=True
)

print("gNMI RPC Query performance measurements for YANG to NGSI-LD translation using data virtualization (interacting with Context Source): \n")

query_mean_virtualization_context_source_all = df_virtualization_cs_queries_all ['query_execution_time'].mean()
query_standard_deviation_virtualization_context_source_all  = df_virtualization_cs_queries_all ['query_execution_time'].std()
print("Data virtualization (context source) - Mean query time", query_mean_virtualization_context_source)
print("Data virtualization (context source) - Query standard deviation:", query_standard_deviation_virtualization_context_source)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cs_queries_all ['query_execution_time']
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
virtualization_cs_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

query_reply_mean_virtualization_context_source_all = df_virtualization_cs_queries_all ['processing_time_since_observed_at'].mean()
query_reply_standard_deviation_virtualization_context_source_all  = df_virtualization_cs_queries_all ['processing_time_since_observed_at'].std()
print("Data virtualization (context source) - Mean query reply time", query_reply_mean_virtualization_context_source_all)
print("Data virtualization (context source) - Query reply standard deviation:", query_reply_standard_deviation_virtualization_context_source_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_cs_queries_all ['processing_time_since_observed_at']
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
virtualization_cs_reply_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

fig, ax = plt.subplots()

query_plot_materialization_queries_all = df_materialization_queries_all.boxplot(column = ['query_execution_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_plot_virtualization_cs_queries_all = df_virtualization_cs_queries_all.boxplot(column = ['query_execution_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_plot_virtualization_cb_queries_all = df_virtualization_cb_queries_all.boxplot(column = ['query_execution_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['Materialization', 'Virtualization_CS', 'Virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean execution time per \n gNMI RPC query operation')

# Texto estadístico
text_outliers_materialization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % materialization_outlier_percentage
))

text_outliers_cs_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cs_outlier_percentage
))

text_outliers_cb_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cb_outlier_percentage
))

# Estilo del recuadro
props = dict(boxstyle='round', facecolor='white', alpha=0.8)

# Añadir recuadro en esquina inferior izquierda
ax.text(0.05, 0.95, text_outliers_materialization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='left', bbox=props, color='blue')

# Añadir recuadro en centro inferior
ax.text(0.5, 0.95, text_outliers_cs_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props, color='grey')


# Añadir recuadro en esquina inferior derecha
ax.text(0.95, 0.05, text_outliers_cb_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', horizontalalignment='right', bbox=props)

plt.savefig("query_performance_measurements_data_integration-with-outliers.png", format="png", dpi=1500)

fig, ax = plt.subplots()

query_reply_plot_materialization_all = df_materialization_queries_all.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
query_reply_plot_virtualization_context_source_all = df_virtualization_cs_queries_all.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
query_reply_plot_virtualization_context_broker_all = df_virtualization_cb_queries_all.boxplot(column = ['processing_time_since_observed_at'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['Materialization', 'Virtualization_CS', 'Virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean reply time per \n  gNMI RPC query operation')

# Texto estadístico
text_outliers_reply_materialization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % materialization_reply_outlier_percentage
))

text_outliers_cs_reply_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cs_reply_outlier_percentage
))

text_outliers_cb_reply_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_cb_reply_outlier_percentage
))

# Estilo del recuadro
props = dict(boxstyle='round', facecolor='white', alpha=0.8)

# Añadir recuadro en esquina inferior izquierda
ax.text(0.05, 0.05, text_outliers_reply_materialization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', horizontalalignment='left', bbox=props, color='blue')

# Añadir recuadro en centro superior
ax.text(0.5, 0.95, text_outliers_cs_reply_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='center', bbox=props, color='grey')


# Añadir recuadro en esquina inferior derecha
ax.text(0.95, 0.95, text_outliers_cb_reply_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='right', bbox=props)


plt.savefig("query_reply_performance_measurements_data_integration-with-outliers.png", format="png", dpi=1500)