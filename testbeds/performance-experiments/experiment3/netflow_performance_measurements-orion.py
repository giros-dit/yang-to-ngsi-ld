import pandas as pd
import matplotlib.pyplot as plt

raw_netflow_df1 = pd.read_csv('netflow_performance_measurements_translation_10flows-orion.csv')
sum_by_10_rows = raw_netflow_df1.groupby(raw_netflow_df1.index // 10)['iteration_execution_time'].sum()
netflow_df1 = pd.DataFrame({'iteration_execution_time': sum_by_10_rows})

raw_netflow_df2 = pd.read_csv('netflow_performance_measurements_translation_20flows-orion.csv')
sum_by_20_rows = raw_netflow_df2.groupby(raw_netflow_df2.index // 20)['iteration_execution_time'].sum()
netflow_df2 = pd.DataFrame({'iteration_execution_time': sum_by_20_rows})

raw_netflow_df3 = pd.read_csv('netflow_performance_measurements_translation_50flows-orion.csv')
sum_by_50_rows = raw_netflow_df3.groupby(raw_netflow_df3.index // 50)['iteration_execution_time'].sum()
netflow_df3 = pd.DataFrame({'iteration_execution_time': sum_by_50_rows})

print("NetFlow performance measurements for YANG to NGSI-LD translation: \n")

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

fig, (ax_netflow_1, ax_netflow_2) = plt.subplots(1, 2, figsize=(10, 5))

netflow_1_plot1 = netflow_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax_netflow_1, positions=[1])

netflow_1_plot2 = netflow_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax_netflow_1, positions=[2])

netflow_1_plot3 = netflow_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax_netflow_1, positions=[3])

raw_netflow_df4 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_10flows-orion.csv')
sum_by_10_rows = raw_netflow_df4.groupby(raw_netflow_df4.index // 10)['iteration_execution_time'].sum()
netflow_df4 = pd.DataFrame({'iteration_execution_time': sum_by_10_rows})

raw_netflow_df5 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_20flows-orion.csv')
sum_by_20_rows = raw_netflow_df5.groupby(raw_netflow_df5.index // 20)['iteration_execution_time'].sum()
netflow_df5 = pd.DataFrame({'iteration_execution_time': sum_by_20_rows})

raw_netflow_df6 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_50flows-orion.csv')
sum_by_50_rows = raw_netflow_df6.groupby(raw_netflow_df6.index // 50)['iteration_execution_time'].sum()
netflow_df6 = pd.DataFrame({'iteration_execution_time': sum_by_50_rows})

print("NetFlow performance measurements for YANG to NGSI-LD translation and materialization: \n")

netflow_raw_mean_4 = raw_netflow_df1['iteration_execution_time'].mean()
netflow_raw_standard_deviation_4 = netflow_df4['iteration_execution_time'].std()
netflow_mean_4 = netflow_df4['iteration_execution_time'].mean()
netflow_standard_deviation_4 = netflow_df4['iteration_execution_time'].std()
print("10 flows - Mean (per 1 event):", netflow_raw_mean_4)
print("10 flows - Standard deviation (per 1 event):", netflow_raw_standard_deviation_4)
print("10 flows - Mean (per 10 events):", netflow_mean_4)
print("10 flows - Standard deviation (per 10 events):", netflow_standard_deviation_4)
print("\n")

netflow_raw_mean_5 = raw_netflow_df5['iteration_execution_time'].mean()
netflow_raw_standard_deviation_5 = netflow_df5['iteration_execution_time'].std()
netflow_mean_5 = netflow_df5['iteration_execution_time'].mean()
netflow_standard_deviation_5 = netflow_df5['iteration_execution_time'].std()
print("20 flows - Mean (per 1 event):", netflow_raw_mean_5)
print("20 flows - Standard deviation (per 1 event):", netflow_raw_standard_deviation_5)
print("20 flows - Mean (per 20 events):", netflow_mean_5)
print("20 flows - Standard deviation (20 events):", netflow_standard_deviation_5)
print("\n")

netflow_raw_mean_6 = raw_netflow_df6['iteration_execution_time'].mean()
netflow_raw_standard_deviation_6 = netflow_df6['iteration_execution_time'].std()
netflow_mean_6 = netflow_df6['iteration_execution_time'].mean()
netflow_standard_deviation_6 = netflow_df6['iteration_execution_time'].std()
print("50 flows - Mean (per 1 event):", netflow_raw_mean_6)
print("50 flows - Standard deviation (per 1 event):", netflow_raw_standard_deviation_6)
print("50 flows - Mean (per 50 events):", netflow_mean_6)
print("50 flows - Standard deviation (per 50 events):", netflow_standard_deviation_6)
print("\n")

netflow_2_plot1 = netflow_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax_netflow_2, positions=[1])

netflow_2_plot2 = netflow_df5.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax_netflow_2, positions=[2])

netflow_2_plot3 = netflow_df6.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "black", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax_netflow_2, positions=[3])

ax_netflow_1.set_xlabel('Number of network flows per export packet')
ax_netflow_1.set_ylabel('Latency (milliseconds)')
ax_netflow_1.set_title('YANG to NGSI-LD translation \n performance for NetFlow')
ax_netflow_1.set_xticks([1, 2, 3], ['10', '20', '50'])

ax_netflow_2.set_xlabel('Number of network flows per export packet')
ax_netflow_2.set_ylabel('Latency (milliseconds)')
ax_netflow_2.set_title('YANG to NGSI-LD translation and materialization \n performance for NetFlow')
ax_netflow_2.set_xticks([1, 2, 3], ['10', '20', '50'])

plt.tight_layout()
plt.savefig("netflow_performance_measurements-orion.png", format="png", dpi=1500)
plt.show()