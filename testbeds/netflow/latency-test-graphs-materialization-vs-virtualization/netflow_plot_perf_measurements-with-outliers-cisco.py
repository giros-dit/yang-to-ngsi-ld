import pandas as pd
import matplotlib.pyplot as plt

df_materialization_parsing = pd.read_csv('performance_measurements_parsing_materialization-cisco.csv')
df_materialization_integration = pd.read_csv('performance_measurements_integration_materialization-cisco.csv')

print("NetFlow v9 performance measurements for YANG to NGSI-LD translation using data materialization: \n")

mean_materialization_parsing = df_materialization_parsing ['iteration_execution_time'].mean()
standard_deviation_materialization_parsing  = df_materialization_parsing ['iteration_execution_time'].std()
print("Data materialization - Mean subscription parsing time:", mean_materialization_parsing)
print("Data materialization - Subscription parsing standard deviation:", standard_deviation_materialization_parsing)
print("\n")

mean_materialization_integration = df_materialization_integration ['iteration_execution_time'].mean()
standard_deviation_materialization_integration  = df_materialization_integration ['iteration_execution_time'].std()
print("Data materialization - Mean subscription parsing integration time:", mean_materialization_integration)
print("Data materialization - Subscription parsing integration standard deviation:", standard_deviation_materialization_integration)
print("\n")

df_virtualization_parsing = pd.read_csv('performance_measurements_parsing_virtualization-cisco.csv')
df_virtualization_integration = pd.read_csv('performance_measurements_integration_virtualization-cisco.csv')

print("NetFlow v9 performance measurements for YANG to NGSI-LD translation using data virtualization: \n")

mean_virtualization_parsing = df_virtualization_parsing ['iteration_execution_time'].mean()
standard_deviation_virtualization_parsing  = df_virtualization_parsing ['iteration_execution_time'].std()
print("Data virtualization - Mean subscription parsing time:", mean_virtualization_parsing)
print("Data virtualization - Subscription parsing standard deviation:", standard_deviation_virtualization_parsing)
print("\n")

mean_virtualization_integration = df_virtualization_integration ['iteration_execution_time'].mean()
standard_deviation_virtualization_integration  = df_virtualization_integration ['iteration_execution_time'].std()
print("Data virtualization - Mean subscription parsing integration time:", mean_virtualization_integration)
print("Data virtualization - Subscription parsing integration standard deviation:", standard_deviation_virtualization_integration)
print("\n")

fig, ax = plt.subplots()

plot_materialization_parsing = df_materialization_parsing.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_parsing = df_virtualization_parsing.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plt.xticks([1, 2], ['materialization', 'virtualization_CS'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean evaluation time per notification in \n NetFlow v9 telemetry')
plt.savefig("notification_parsing_performance_measurements_data_integration-cisco.png", format="png", dpi=1500)

fig, ax = plt.subplots()

plot_materialization_integration = df_materialization_integration.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_integration = df_virtualization_integration.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plt.xticks([1, 2], ['materialization', 'virtualization_CS'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean integration time per notification in \n NetFlow v9 telemetry')
plt.savefig("notification_integration_performance_measurements_data_integration-cisco.png", format="png", dpi=1500)