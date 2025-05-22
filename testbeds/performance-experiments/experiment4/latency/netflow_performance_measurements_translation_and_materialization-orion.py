import pandas as pd
import matplotlib.pyplot as plt

raw_netflow_df1 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_10flows-orion.csv')
sum_by_10_rows = raw_netflow_df1.groupby(raw_netflow_df1.index // 10)['iteration_execution_time'].sum()
netflow_df1 = pd.DataFrame({'iteration_execution_time': sum_by_10_rows})

raw_netflow_df2 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_20flows-orion.csv')
sum_by_20_rows = raw_netflow_df2.groupby(raw_netflow_df2.index // 20)['iteration_execution_time'].sum()
netflow_df2 = pd.DataFrame({'iteration_execution_time': sum_by_20_rows})

raw_netflow_df3 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_50flows-orion.csv')
sum_by_50_rows = raw_netflow_df3.groupby(raw_netflow_df3.index // 50)['iteration_execution_time'].sum()
netflow_df3 = pd.DataFrame({'iteration_execution_time': sum_by_50_rows})

print("NetFlow performance measurements for YANG to NGSI-LD translation and materialization: \n")

netflow_raw_mean_1 = raw_netflow_df1['iteration_execution_time'].mean()
netflow_raw_standard_deviation_1 = netflow_df1['iteration_execution_time'].std()
netflow_mean_1 = netflow_df1['iteration_execution_time'].mean()
netflow_standard_deviation_1 = netflow_df1['iteration_execution_time'].std()
print("10 flows - Mean (per 1 event):", netflow_raw_mean_1)
print("10 flows - Standard deviation (per 1 event):", netflow_raw_standard_deviation_1)
print("10 flows - Mean (per 10 events):", netflow_mean_1)
print("10 flows - Standard deviation (per 10 events):", netflow_standard_deviation_1)
print("\n")

netflow_raw_mean_2 = raw_netflow_df2['iteration_execution_time'].mean()
netflow_raw_standard_deviation_2 = netflow_df2['iteration_execution_time'].std()
netflow_mean_2 = netflow_df2['iteration_execution_time'].mean()
netflow_standard_deviation_2 = netflow_df2['iteration_execution_time'].std()
print("20 flows - Mean (per 1 event):", netflow_raw_mean_2)
print("20 flows - Standard deviation (per 1 event):", netflow_raw_standard_deviation_2)
print("20 flows - Mean (per 20 events):", netflow_mean_2)
print("20 flows - Standard deviation (20 events):", netflow_standard_deviation_2)
print("\n")

netflow_raw_mean_3 = raw_netflow_df3['iteration_execution_time'].mean()
netflow_raw_standard_deviation_3 = netflow_df3['iteration_execution_time'].std()
netflow_mean_3 = netflow_df3['iteration_execution_time'].mean()
netflow_standard_deviation_3 = netflow_df3['iteration_execution_time'].std()
print("50 flows - Mean (per 1 event):", netflow_raw_mean_3)
print("50 flows - Standard deviation (per 1 event):", netflow_raw_standard_deviation_3)
print("50 flows - Mean (per 50 events):", netflow_mean_3)
print("50 flows - Standard deviation (per 50 events):", netflow_standard_deviation_3)
print("\n")

fig, ax = plt.subplots()

plot1 = netflow_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[1])

plot2 = netflow_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[2])

plot3 = netflow_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['10', '20', '50'])
plt.xlabel('Number of network flows per export packet')
plt.ylabel('Latency (milliseconds)')
plt.title('YANG to NGSI-LD translation and materialization performance for NetFlow')
plt.suptitle('')
plt.savefig("netflow_performance_measurements_translation_and_materialization-orion.png", format="png", dpi=1500)
plt.show()