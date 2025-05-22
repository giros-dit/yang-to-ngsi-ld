import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Create custom legend handles
legend_handles = [
    Patch(facecolor='grey', edgecolor='yellow', label='ORION'),
    Patch(facecolor='blue', edgecolor='red', label='SCORPIO')
]

scorpio_raw_gnmi_df1 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_12ifaces.csv')
scorpio_sum_by_12_rows = scorpio_raw_gnmi_df1.groupby(scorpio_raw_gnmi_df1.index // 12)['iteration_execution_time'].sum()
scorpio_gnmi_df1 = pd.DataFrame({'iteration_execution_time': scorpio_sum_by_12_rows})

scorpio_raw_gnmi_df2 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_24ifaces.csv')
scorpio_sum_by_24_rows = scorpio_raw_gnmi_df2.groupby(scorpio_raw_gnmi_df2.index // 24)['iteration_execution_time'].sum()
scorpio_gnmi_df2 = pd.DataFrame({'iteration_execution_time': scorpio_sum_by_24_rows})

scorpio_raw_gnmi_df3 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_36ifaces.csv')
scorpio_sum_by_36_rows = scorpio_raw_gnmi_df3.groupby(scorpio_raw_gnmi_df3.index // 36)['iteration_execution_time'].sum()
scorpio_gnmi_df3 = pd.DataFrame({'iteration_execution_time': scorpio_sum_by_36_rows})

scorpio_raw_gnmi_df4 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_48ifaces.csv')
scorpio_sum_by_48_rows = scorpio_raw_gnmi_df4.groupby(scorpio_raw_gnmi_df4.index // 48)['iteration_execution_time'].sum()
scorpio_gnmi_df4 = pd.DataFrame({'iteration_execution_time': scorpio_sum_by_48_rows})

print("gNMI performance measurements for YANG to NGSI-LD translation and materialization with Scorpio NGSI-LD Context Broker: \n")

scorpio_gnmi_raw_mean_1 = scorpio_raw_gnmi_df1['iteration_execution_time'].mean()
scorpio_gnmi_raw_standard_deviation_1 = scorpio_gnmi_df1['iteration_execution_time'].std()
scorpio_gnmi_mean_1 = scorpio_gnmi_df1['iteration_execution_time'].mean()
scorpio_gnmi_standard_deviation_1 = scorpio_gnmi_df1['iteration_execution_time'].std()
print("12 Interfaces - Mean (per 1 event):", scorpio_gnmi_raw_mean_1)
print("12 Interfaces - Standard deviation (per 1 event):", scorpio_gnmi_raw_standard_deviation_1)
print("12 Interfaces - Mean (per 12 events):", scorpio_gnmi_mean_1)
print("12 Interfaces - Standard deviation (per 12 events):", scorpio_gnmi_standard_deviation_1)
print("\n")

scorpio_gnmi_raw_mean_2 = scorpio_raw_gnmi_df2['iteration_execution_time'].mean()
scorpio_gnmi_raw_standard_deviation_2 = scorpio_gnmi_df2['iteration_execution_time'].std()
scorpio_gnmi_mean_2 = scorpio_gnmi_df2['iteration_execution_time'].mean()
scorpio_gnmi_standard_deviation_2 = scorpio_gnmi_df2['iteration_execution_time'].std()
print("24 Interfaces - Mean (per 1 event):", scorpio_gnmi_raw_mean_2)
print("24 Interfaces - Standard deviation (per 1 event):", scorpio_gnmi_raw_standard_deviation_2)
print("24 Interfaces - Mean (per 24 events):", scorpio_gnmi_mean_2)
print("24 Interfaces - Standard deviation (24 events):", scorpio_gnmi_standard_deviation_2)
print("\n")

scorpio_gnmi_raw_mean_3 = scorpio_raw_gnmi_df3['iteration_execution_time'].mean()
scorpio_gnmi_raw_standard_deviation_3 = scorpio_gnmi_df3['iteration_execution_time'].std()
scorpio_gnmi_mean_3 = scorpio_gnmi_df3['iteration_execution_time'].mean()
scorpio_gnmi_standard_deviation_3 = scorpio_gnmi_df3['iteration_execution_time'].std()
print("36 Interfaces - Mean (per 1 event):", scorpio_gnmi_raw_mean_3)
print("36 Interfaces - Standard deviation (per 1 event):", scorpio_gnmi_raw_standard_deviation_3)
print("36 Interfaces - Mean (per 36 events):", scorpio_gnmi_mean_3)
print("36 Interfaces - Standard deviation (per 36 events):", scorpio_gnmi_standard_deviation_3)
print("\n")

scorpio_gnmi_raw_mean_4 = scorpio_raw_gnmi_df4['iteration_execution_time'].mean()
scorpio_gnmi_raw_standard_deviation_4 = scorpio_gnmi_df4['iteration_execution_time'].std()
scorpio_gnmi_mean_4 = scorpio_gnmi_df4['iteration_execution_time'].mean()
scorpio_gnmi_standard_deviation_4 = scorpio_gnmi_df4['iteration_execution_time'].std()
print("48 Interfaces - Mean (per 1 event):", scorpio_gnmi_raw_mean_4)
print("48 Interfaces - Standard deviation (per 1 event):", scorpio_gnmi_raw_standard_deviation_4)
print("48 Interfaces - Mean (per 48 events):", scorpio_gnmi_mean_4)
print("48 Interfaces - Standard deviation (per 48 events):", scorpio_gnmi_standard_deviation_4)
print("\n")

fig, (ax_gnmi, ax_netconf) = plt.subplots(1, 2, figsize=(10, 5))

scorpio_plot1 = scorpio_gnmi_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_gnmi, positions=[1])

scorpio_plot2 = scorpio_gnmi_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_gnmi, positions=[2])

scorpio_plot3 = scorpio_gnmi_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_gnmi, positions=[3])

scorpio_plot4 = scorpio_gnmi_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_gnmi, positions=[4])

orion_raw_gnmi_df1 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_12ifaces-orion.csv')
orion_sum_by_12_rows = orion_raw_gnmi_df1.groupby(orion_raw_gnmi_df1.index // 12)['iteration_execution_time'].sum()
orion_gnmi_df1 = pd.DataFrame({'iteration_execution_time': orion_sum_by_12_rows})

orion_raw_gnmi_df2 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_24ifaces-orion.csv')
orion_sum_by_24_rows = orion_raw_gnmi_df2.groupby(orion_raw_gnmi_df2.index // 24)['iteration_execution_time'].sum()
orion_gnmi_df2 = pd.DataFrame({'iteration_execution_time': orion_sum_by_24_rows})

orion_raw_gnmi_df3 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_36ifaces-orion.csv')
orion_sum_by_36_rows = orion_raw_gnmi_df3.groupby(orion_raw_gnmi_df3.index // 36)['iteration_execution_time'].sum()
orion_gnmi_df3 = pd.DataFrame({'iteration_execution_time': orion_sum_by_36_rows})

orion_raw_gnmi_df4 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_48ifaces-orion.csv')
orion_sum_by_48_rows = orion_raw_gnmi_df4.groupby(orion_raw_gnmi_df4.index // 48)['iteration_execution_time'].sum()
orion_gnmi_df4 = pd.DataFrame({'iteration_execution_time': orion_sum_by_48_rows})

print("gNMI performance measurements for YANG to NGSI-LD translation and materialization with Orion NGSI-LD Context Broker: \n")

orion_gnmi_raw_mean_1 = orion_raw_gnmi_df1['iteration_execution_time'].mean()
orion_gnmi_raw_standard_deviation_1 = orion_gnmi_df1['iteration_execution_time'].std()
orion_gnmi_mean_1 = orion_gnmi_df1['iteration_execution_time'].mean()
orion_gnmi_standard_deviation_1 = orion_gnmi_df1['iteration_execution_time'].std()
print("12 Interfaces - Mean (per 1 event):", orion_gnmi_raw_mean_1)
print("12 Interfaces - Standard deviation (per 1 event):", orion_gnmi_raw_standard_deviation_1)
print("12 Interfaces - Mean (per 12 events):", orion_gnmi_mean_1)
print("12 Interfaces - Standard deviation (per 12 events):", orion_gnmi_standard_deviation_1)
print("\n")

orion_gnmi_raw_mean_2 = orion_raw_gnmi_df2['iteration_execution_time'].mean()
orion_gnmi_raw_standard_deviation_2 = orion_gnmi_df2['iteration_execution_time'].std()
orion_gnmi_mean_2 = orion_gnmi_df2['iteration_execution_time'].mean()
orion_gnmi_standard_deviation_2 = orion_gnmi_df2['iteration_execution_time'].std()
print("24 Interfaces - Mean (per 1 event):", orion_gnmi_raw_mean_2)
print("24 Interfaces - Standard deviation (per 1 event):", orion_gnmi_raw_standard_deviation_2)
print("24 Interfaces - Mean (per 24 events):", orion_gnmi_mean_2)
print("24 Interfaces - Standard deviation (24 events):", orion_gnmi_standard_deviation_2)
print("\n")

orion_gnmi_raw_mean_3 = orion_raw_gnmi_df3['iteration_execution_time'].mean()
orion_gnmi_raw_standard_deviation_3 = orion_gnmi_df3['iteration_execution_time'].std()
orion_gnmi_mean_3 = orion_gnmi_df3['iteration_execution_time'].mean()
orion_gnmi_standard_deviation_3 = orion_gnmi_df3['iteration_execution_time'].std()
print("36 Interfaces - Mean (per 1 event):", orion_gnmi_raw_mean_3)
print("36 Interfaces - Standard deviation (per 1 event):", orion_gnmi_raw_standard_deviation_3)
print("36 Interfaces - Mean (per 36 events):", orion_gnmi_mean_3)
print("36 Interfaces - Standard deviation (per 36 events):", orion_gnmi_standard_deviation_3)
print("\n")

orion_gnmi_raw_mean_4 = orion_raw_gnmi_df4['iteration_execution_time'].mean()
orion_gnmi_raw_standard_deviation_4 = orion_gnmi_df4['iteration_execution_time'].std()
orion_gnmi_mean_4 = orion_gnmi_df4['iteration_execution_time'].mean()
orion_gnmi_standard_deviation_4 = orion_gnmi_df4['iteration_execution_time'].std()
print("48 Interfaces - Mean (per 1 event):", orion_gnmi_raw_mean_4)
print("48 Interfaces - Standard deviation (per 1 event):", orion_gnmi_raw_standard_deviation_4)
print("48 Interfaces - Mean (per 48 events):", orion_gnmi_mean_4)
print("48 Interfaces - Standard deviation (per 48 events):", orion_gnmi_standard_deviation_4)
print("\n")

orion_plot1 = orion_gnmi_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_gnmi, positions=[1])

orion_plot2 = orion_gnmi_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_gnmi, positions=[2])

orion_plot3 = orion_gnmi_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_gnmi, positions=[3])

orion_plot4 = orion_gnmi_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_gnmi, positions=[4])

scorpio_df1 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_12ifaces-scorpio.csv')
scorpio_df2 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_24ifaces-scorpio.csv')
scorpio_df3 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_36ifaces-scorpio.csv')
scorpio_df4 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_48ifaces-scorpio.csv')

print("NETCONF performance measurements for YANG to NGSI-LD translation and materialization with Scorpio NGSI-LD Context Broker: \n")

scorpio_mean_1 = scorpio_df1['iteration_execution_time'].mean()
scorpio_standard_deviation_1 = scorpio_df1['iteration_execution_time'].std()
print("12 Interfaces - Mean:", scorpio_mean_1)
print("12 Interfaces - Standard deviation:", scorpio_standard_deviation_1)
print("\n")

scorpio_mean_2 = scorpio_df2['iteration_execution_time'].mean()
scorpio_standard_deviation_2 = scorpio_df2['iteration_execution_time'].std()
print("24 Interfaces - Mean:", scorpio_mean_2)
print("24 Interfaces - Standard deviation:", scorpio_standard_deviation_2)
print("\n")

scorpio_mean_3 = scorpio_df3['iteration_execution_time'].mean()
scorpio_standard_deviation_3 = scorpio_df3['iteration_execution_time'].std()
print("36 Interfaces - Mean:", scorpio_mean_3)
print("36 Interfaces - Standard deviation:", scorpio_standard_deviation_3)
print("\n")

scorpio_mean_4 = scorpio_df4['iteration_execution_time'].mean()
scorpio_standard_deviation_4 = scorpio_df4['iteration_execution_time'].std()
print("48 Interfaces - Mean:", scorpio_mean_4)
print("48 Interfaces - Standard deviation:", scorpio_standard_deviation_4)
print("\n")

scorpio_plot1 = scorpio_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_netconf, positions=[1])

scorpio_plot2 = scorpio_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_netconf, positions=[2])

scorpio_plot3 = scorpio_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_netconf, positions=[3])

scorpio_plot4 = scorpio_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_netconf, positions=[4])

orion_df1 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_12ifaces-orion.csv')
orion_df2 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_24ifaces-orion.csv')
orion_df3 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_36ifaces-orion.csv')
orion_df4 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_48ifaces-orion.csv')

print("NETCONF performance measurements for YANG to NGSI-LD translation and materialization with Orion NGSI-LD Context Broker: \n")

orion_mean_1 = orion_df1['iteration_execution_time'].mean()
orion_standard_deviation_1 = orion_df1['iteration_execution_time'].std()
print("12 Interfaces - Mean:", orion_mean_1)
print("12 Interfaces - Standard deviation:", orion_standard_deviation_1)
print("\n")

orion_mean_2 = orion_df2['iteration_execution_time'].mean()
orion_standard_deviation_2 = orion_df2['iteration_execution_time'].std()
print("24 Interfaces - Mean:", orion_mean_2)
print("24 Interfaces - Standard deviation:", orion_standard_deviation_2)
print("\n")

orion_mean_3 = orion_df3['iteration_execution_time'].mean()
orion_standard_deviation_3 = orion_df3['iteration_execution_time'].std()
print("36 Interfaces - Mean:", orion_mean_3)
print("36 Interfaces - Standard deviation:", orion_standard_deviation_3)
print("\n")

orion_mean_4 = orion_df4['iteration_execution_time'].mean()
orion_standard_deviation_4 = orion_df4['iteration_execution_time'].std()
print("48 Interfaces - Mean:", orion_mean_4)
print("48 Interfaces - Standard deviation:", orion_standard_deviation_4)
print("\n")

orion_plot1 = orion_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf, positions=[1])

orion_plot2 = orion_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf, positions=[2])

orion_plot3 = orion_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf, positions=[3])

orion_plot4 = orion_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf, positions=[4])

ax_gnmi.legend(handles=legend_handles)
ax_gnmi.set_xlabel('Number of network interfaces')
ax_gnmi.set_ylabel('Latency (milliseconds)')
ax_gnmi.set_title('YANG to NGSI-LD translation and instantiation \n latency performance for gNMI')
ax_gnmi.set_xticks([1, 2, 3, 4], ['12', '24', '36', '48'])

ax_netconf.legend(handles=legend_handles)
ax_netconf.set_xlabel('Number of network interfaces')
ax_netconf.set_ylabel('Latency (milliseconds)')
ax_netconf.set_title('YANG to NGSI-LD translation and instantiation \n latency performance for NETCONF')
ax_netconf.set_xticks([1, 2, 3, 4], ['12', '24', '36', '48'])

plt.tight_layout()
plt.savefig("performance_measurements_translation_and_materialization_brokers.png", format="png", dpi=1500)
plt.show()