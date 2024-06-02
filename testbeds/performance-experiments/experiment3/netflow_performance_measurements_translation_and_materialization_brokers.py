import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Create custom legend handles
legend_handles = [
    Patch(facecolor='grey', edgecolor='yellow', label='ORION-LD'),
    Patch(facecolor='blue', edgecolor='red', label='SCORPIO')
]

scorpio_raw_netflow_df1 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_10flows.csv')
scorpio_sum_by_10_rows = scorpio_raw_netflow_df1.groupby(scorpio_raw_netflow_df1.index // 10)['iteration_execution_time'].sum()
scorpio_netflow_df1 = pd.DataFrame({'iteration_execution_time': scorpio_sum_by_10_rows})

scorpio_raw_netflow_df2 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_20flows.csv')
scorpio_sum_by_20_rows = scorpio_raw_netflow_df2.groupby(scorpio_raw_netflow_df2.index // 20)['iteration_execution_time'].sum()
scorpio_netflow_df2 = pd.DataFrame({'iteration_execution_time': scorpio_sum_by_20_rows})

scorpio_raw_netflow_df3 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_50flows.csv')
scorpio_sum_by_50_rows = scorpio_raw_netflow_df3.groupby(scorpio_raw_netflow_df3.index // 50)['iteration_execution_time'].sum()
scorpio_netflow_df3 = pd.DataFrame({'iteration_execution_time': scorpio_sum_by_50_rows})

print("NetFlow performance measurements for YANG to NGSI-LD translation and materialization with Scorpio NGSI-LD Context Broker: \n")

scorpio_netflow_raw_mean_1 = scorpio_raw_netflow_df1['iteration_execution_time'].mean()
scorpio_netflow_raw_standard_deviation_1 = scorpio_netflow_df1['iteration_execution_time'].std()
scorpio_netflow_mean_1 = scorpio_netflow_df1['iteration_execution_time'].mean()
scorpio_netflow_standard_deviation_1 = scorpio_netflow_df1['iteration_execution_time'].std()
print("10 flows - Mean (per 1 event):", scorpio_netflow_raw_mean_1)
print("10 flows - Standard deviation (per 1 event):", scorpio_netflow_raw_standard_deviation_1)
print("10 flows - Mean (per 10 events):", scorpio_netflow_mean_1)
print("10 flows - Standard deviation (per 10 events):", scorpio_netflow_standard_deviation_1)
print("\n")

scorpio_netflow_raw_mean_2 = scorpio_raw_netflow_df2['iteration_execution_time'].mean()
scorpio_netflow_raw_standard_deviation_2 = scorpio_netflow_df2['iteration_execution_time'].std()
scorpio_netflow_mean_2 = scorpio_netflow_df2['iteration_execution_time'].mean()
scorpio_netflow_standard_deviation_2 = scorpio_netflow_df2['iteration_execution_time'].std()
print("20 flows - Mean (per 1 event):", scorpio_netflow_raw_mean_2)
print("20 flows - Standard deviation (per 1 event):", scorpio_netflow_raw_standard_deviation_2)
print("20 flows - Mean (per 20 events):", scorpio_netflow_mean_2)
print("20 flows - Standard deviation (20 events):", scorpio_netflow_standard_deviation_2)
print("\n")

scorpio_netflow_raw_mean_3 = scorpio_raw_netflow_df3['iteration_execution_time'].mean()
scorpio_netflow_raw_standard_deviation_3 = scorpio_netflow_df3['iteration_execution_time'].std()
scorpio_netflow_mean_3 = scorpio_netflow_df3['iteration_execution_time'].mean()
scorpio_netflow_standard_deviation_3 = scorpio_netflow_df3['iteration_execution_time'].std()
print("50 flows - Mean (per 1 event):", scorpio_netflow_raw_mean_3)
print("50 flows - Standard deviation (per 1 event):", scorpio_netflow_raw_standard_deviation_3)
print("50 flows - Mean (per 50 events):", scorpio_netflow_mean_3)
print("50 flows - Standard deviation (per 50 events):", scorpio_netflow_standard_deviation_3)
print("\n")

fig, ax = plt.subplots()

scorpio_plot1 = scorpio_netflow_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])

scorpio_plot2 = scorpio_netflow_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[2])

scorpio_plot3 = scorpio_netflow_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[3])

orion_raw_netflow_df1 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_10flows-orion.csv')
orion_sum_by_10_rows = orion_raw_netflow_df1.groupby(orion_raw_netflow_df1.index // 10)['iteration_execution_time'].sum()
orion_netflow_df1 = pd.DataFrame({'iteration_execution_time': orion_sum_by_10_rows})

orion_raw_netflow_df2 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_20flows-orion.csv')
orion_sum_by_20_rows = orion_raw_netflow_df2.groupby(orion_raw_netflow_df2.index // 20)['iteration_execution_time'].sum()
orion_netflow_df2 = pd.DataFrame({'iteration_execution_time': orion_sum_by_20_rows})

orion_raw_netflow_df3 = pd.read_csv('netflow_performance_measurements_translation_and_materialization_50flows-orion.csv')
orion_sum_by_50_rows = orion_raw_netflow_df3.groupby(orion_raw_netflow_df3.index // 50)['iteration_execution_time'].sum()
orion_netflow_df3 = pd.DataFrame({'iteration_execution_time': orion_sum_by_50_rows})

print("NetFlow performance measurements for YANG to NGSI-LD translation and materialization with Orion NGSI-LD Context Broker: \n")

orion_netflow_raw_mean_1 = orion_raw_netflow_df1['iteration_execution_time'].mean()
orion_netflow_raw_standard_deviation_1 = orion_netflow_df1['iteration_execution_time'].std()
orion_netflow_mean_1 = orion_netflow_df1['iteration_execution_time'].mean()
orion_netflow_standard_deviation_1 = orion_netflow_df1['iteration_execution_time'].std()
print("10 flows - Mean (per 1 event):", orion_netflow_raw_mean_1)
print("10 flows - Standard deviation (per 1 event):", orion_netflow_raw_standard_deviation_1)
print("10 flows - Mean (per 10 events):", orion_netflow_mean_1)
print("10 flows - Standard deviation (per 10 events):", orion_netflow_standard_deviation_1)
print("\n")

orion_netflow_raw_mean_2 = orion_raw_netflow_df2['iteration_execution_time'].mean()
orion_netflow_raw_standard_deviation_2 = orion_netflow_df2['iteration_execution_time'].std()
orion_netflow_mean_2 = orion_netflow_df2['iteration_execution_time'].mean()
orion_netflow_standard_deviation_2 = orion_netflow_df2['iteration_execution_time'].std()
print("20 flows - Mean (per 1 event):", orion_netflow_raw_mean_2)
print("20 flows - Standard deviation (per 1 event):", orion_netflow_raw_standard_deviation_2)
print("20 flows - Mean (per 20 events):", orion_netflow_mean_2)
print("20 flows - Standard deviation (20 events):", orion_netflow_standard_deviation_2)
print("\n")

orion_netflow_raw_mean_3 = orion_raw_netflow_df3['iteration_execution_time'].mean()
orion_netflow_raw_standard_deviation_3 = orion_netflow_df3['iteration_execution_time'].std()
orion_netflow_mean_3 = orion_netflow_df3['iteration_execution_time'].mean()
orion_netflow_standard_deviation_3 = orion_netflow_df3['iteration_execution_time'].std()
print("50 flows - Mean (per 1 event):", orion_netflow_raw_mean_3)
print("50 flows - Standard deviation (per 1 event):", orion_netflow_raw_standard_deviation_3)
print("50 flows - Mean (per 50 events):", orion_netflow_mean_3)
print("50 flows - Standard deviation (per 50 events):", orion_netflow_standard_deviation_3)
print("\n")

orion_plot1 = orion_netflow_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[1])

orion_plot2 = orion_netflow_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

orion_plot3 = orion_netflow_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[3])

plt.legend(handles=legend_handles)
plt.xticks([1, 2, 3], ['10', '20', '50'])
plt.xlabel('Number of network flows per export packet')
plt.ylabel('Latency (milliseconds)')
plt.title('YANG to NGSI-LD translation and materialization performance for NetFlow')
plt.suptitle('')
plt.savefig("netflow_performance_measurements_translation_and_materialization_brokers.png", format="png", dpi=1500)
plt.show()