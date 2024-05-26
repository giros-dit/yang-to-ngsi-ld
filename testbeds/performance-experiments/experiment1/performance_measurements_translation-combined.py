import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Create custom legend handles
legend_handles = [
    Patch(facecolor='grey', edgecolor='yellow', label='NETCONF'),
    Patch(facecolor='blue', edgecolor='red', label='gNMI')
]


raw_gnmi_df1 = pd.read_csv('gnmi_performance_measurements_translation_12ifaces.csv')
sum_by_12_rows = raw_gnmi_df1.groupby(raw_gnmi_df1.index // 12)['iteration_execution_time'].sum()
gnmi_df1 = pd.DataFrame({'iteration_execution_time': sum_by_12_rows})

raw_gnmi_df2 = pd.read_csv('gnmi_performance_measurements_translation_24ifaces.csv')
sum_by_24_rows = raw_gnmi_df2.groupby(raw_gnmi_df2.index // 24)['iteration_execution_time'].sum()
gnmi_df2 = pd.DataFrame({'iteration_execution_time': sum_by_24_rows})

raw_gnmi_df3 = pd.read_csv('gnmi_performance_measurements_translation_36ifaces.csv')
sum_by_36_rows = raw_gnmi_df3.groupby(raw_gnmi_df3.index // 36)['iteration_execution_time'].sum()
gnmi_df3 = pd.DataFrame({'iteration_execution_time': sum_by_36_rows})

raw_gnmi_df4 = pd.read_csv('gnmi_performance_measurements_translation_48ifaces.csv')
sum_by_48_rows = raw_gnmi_df4.groupby(raw_gnmi_df4.index // 48)['iteration_execution_time'].sum()
gnmi_df4 = pd.DataFrame({'iteration_execution_time': sum_by_48_rows})

print("gNMI performance measurements for YANG to NGSI-LD translation: \n")

gnmi_raw_mean_1 = raw_gnmi_df1['iteration_execution_time'].mean()
gnmi_raw_standard_deviation_1 = gnmi_df1['iteration_execution_time'].std()
gnmi_mean_1 = gnmi_df1['iteration_execution_time'].mean()
gnmi_standard_deviation_1 = gnmi_df1['iteration_execution_time'].std()
print("12 Interfaces - Mean (per 1 event):", gnmi_raw_mean_1)
print("12 Interfaces - Standard deviation (per 1 event):", gnmi_raw_standard_deviation_1)
print("12 Interfaces - Mean (per 12 events):", gnmi_mean_1)
print("12 Interfaces - Standard deviation (per 12 events):", gnmi_standard_deviation_1)
print("\n")

gnmi_raw_mean_2 = raw_gnmi_df2['iteration_execution_time'].mean()
gnmi_raw_standard_deviation_2 = gnmi_df2['iteration_execution_time'].std()
gnmi_mean_2 = gnmi_df2['iteration_execution_time'].mean()
gnmi_standard_deviation_2 = gnmi_df2['iteration_execution_time'].std()
print("24 Interfaces - Mean (per 1 event):", gnmi_raw_mean_2)
print("24 Interfaces - Standard deviation (per 1 event):", gnmi_raw_standard_deviation_2)
print("24 Interfaces - Mean (per 24 events):", gnmi_mean_2)
print("24 Interfaces - Standard deviation (24 events):", gnmi_standard_deviation_2)
print("\n")

gnmi_raw_mean_3 = raw_gnmi_df3['iteration_execution_time'].mean()
gnmi_raw_standard_deviation_3 = gnmi_df3['iteration_execution_time'].std()
gnmi_mean_3 = gnmi_df3['iteration_execution_time'].mean()
gnmi_standard_deviation_3 = gnmi_df3['iteration_execution_time'].std()
print("36 Interfaces - Mean (per 1 event):", gnmi_raw_mean_3)
print("36 Interfaces - Standard deviation (per 1 event):", gnmi_raw_standard_deviation_3)
print("36 Interfaces - Mean (per 36 events):", gnmi_mean_3)
print("36 Interfaces - Standard deviation (per 36 events):", gnmi_standard_deviation_3)
print("\n")

gnmi_raw_mean_4 = raw_gnmi_df4['iteration_execution_time'].mean()
gnmi_raw_standard_deviation_4 = gnmi_df4['iteration_execution_time'].std()
gnmi_mean_4 = gnmi_df4['iteration_execution_time'].mean()
gnmi_standard_deviation_4 = gnmi_df4['iteration_execution_time'].std()
print("48 Interfaces - Mean (per 1 event):", gnmi_raw_mean_4)
print("48 Interfaces - Standard deviation (per 1 event):", gnmi_raw_standard_deviation_4)
print("48 Interfaces - Mean (per 48 events):", gnmi_mean_4)
print("48 Interfaces - Standard deviation (per 48 events):", gnmi_standard_deviation_4)
print("\n")

fig, ax = plt.subplots()

gnmi_plot1 = gnmi_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])

gnmi_plot2 = gnmi_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[2])

gnmi_plot3 = gnmi_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[3])

gnmi_plot4 = gnmi_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[4])


netconf_df1 = pd.read_csv('netconf_performance_measurements_translation_12ifaces.csv')
netconf_df2 = pd.read_csv('netconf_performance_measurements_translation_24ifaces.csv')
netconf_df3 = pd.read_csv('netconf_performance_measurements_translation_36ifaces.csv')
netconf_df4 = pd.read_csv('netconf_performance_measurements_translation_48ifaces.csv')

print("NETCONF performance measurements for YANG to NGSI-LD translation: \n")

netconf_mean_1 = netconf_df1['iteration_execution_time'].mean()
netconf_standard_deviation_1 = netconf_df1['iteration_execution_time'].std()
print("12 Interfaces - Mean:", netconf_mean_1)
print("12 Interfaces - Standard deviation:", netconf_standard_deviation_1)
print("\n")

netconf_mean_2 = netconf_df2['iteration_execution_time'].mean()
netconf_standard_deviation_2 = netconf_df2['iteration_execution_time'].std()
print("24 Interfaces - Mean:", netconf_mean_2)
print("24 Interfaces - Standard deviation:", netconf_standard_deviation_2)
print("\n")

netconf_mean_3 = netconf_df3['iteration_execution_time'].mean()
netconf_standard_deviation_3 = netconf_df3['iteration_execution_time'].std()
print("36 Interfaces - Mean:", netconf_mean_3)
print("36 Interfaces - Standard deviation:", netconf_standard_deviation_3)
print("\n")

netconf_mean_4 = netconf_df4['iteration_execution_time'].mean()
netconf_standard_deviation_4 = netconf_df4['iteration_execution_time'].std()
print("48 Interfaces - Mean:", netconf_mean_4)
print("48 Interfaces - Standard deviation:", netconf_standard_deviation_4)
print("\n")

netconf_plot1 = netconf_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[1])

netconf_plot2 = netconf_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

netconf_plot3 = netconf_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[3])

netconf_plot4 = netconf_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[4])

plt.legend(handles=legend_handles)
plt.xlabel('Number of network interfaces')
plt.ylabel('Latency (milliseconds)')
plt.title('YANG to NGSI-LD translation \n performance for NETCONF and gNMI')
plt.xticks([1, 2, 3, 4], ['12', '24', '36', '48'])
plt.suptitle('')
plt.savefig("performance_measurements_translation-combined.png", format="png", dpi=1500)
plt.show()