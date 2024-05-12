import pandas as pd
import matplotlib.pyplot as plt

gnmi_df1 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_12ifaces.csv')
gnmi_df2 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_24ifaces.csv')
gnmi_df3 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_36ifaces.csv')
gnmi_df4 = pd.read_csv('gnmi_performance_measurements_translation_and_materialization_48ifaces.csv')

print("gNMI performance measurements for YANG to NGSI-LD translation and materialization: \n")

gnmi_mean_1 = gnmi_df1['iteration_execution_time'].mean()
gnmi_standard_deviation_1 = gnmi_df1['iteration_execution_time'].std()
print("12 Interfaces - Mean (1 event):", gnmi_mean_1)
print("12 Interfaces - Standard deviation (1 event):", gnmi_standard_deviation_1)
print("12 Interfaces - Mean (12 events):", gnmi_mean_1 * 12)
print("12 Interfaces - Standard deviation (12 events):", gnmi_standard_deviation_1 * 12)
print("\n")

gnmi_mean_2 = gnmi_df2['iteration_execution_time'].mean()
gnmi_standard_deviation_2 = gnmi_df2['iteration_execution_time'].std()
print("24 Interfaces - Mean:", gnmi_mean_2)
print("24 Interfaces - Standard deviation:", gnmi_standard_deviation_2)
print("24 Interfaces - Mean (24 events):", gnmi_mean_2 * 24)
print("24 Interfaces - Standard deviation (24 events):", gnmi_standard_deviation_2 * 24)
print("\n")

gnmi_mean_3 = gnmi_df3['iteration_execution_time'].mean()
gnmi_standard_deviation_3 = gnmi_df3['iteration_execution_time'].std()
print("36 Interfaces - Mean:", gnmi_mean_3)
print("36 Interfaces - Standard deviation:", gnmi_standard_deviation_3)
print("36 Interfaces - Mean (36 events):", gnmi_mean_3 * 36)
print("36 Interfaces - Standard deviation (36 events):", gnmi_standard_deviation_3 * 36)
print("\n")

gnmi_mean_4 = gnmi_df4['iteration_execution_time'].mean()
gnmi_standard_deviation_4 = gnmi_df4['iteration_execution_time'].std()
print("48 Interfaces - Mean:", gnmi_mean_4)
print("48 Interfaces - Standard deviation:", gnmi_standard_deviation_4)
print("48 Interfaces - Mean (48 events):", gnmi_mean_4 * 48)
print("48 Interfaces - Standard deviation (48 events):", gnmi_standard_deviation_4 * 48)
print("\n")

gnmi_df1['iteration_execution_time'] *= 12
gnmi_df2['iteration_execution_time'] *= 24
gnmi_df3['iteration_execution_time'] *= 36
gnmi_df4['iteration_execution_time'] *= 48

fig, (ax_gnmi, ax_netconf) = plt.subplots(1, 2, figsize=(10, 5))

gnmi_plot1 = gnmi_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), ax=ax_gnmi, positions=[1])

gnmi_plot2 = gnmi_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), ax=ax_gnmi, positions=[2])

gnmi_plot3 = gnmi_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), ax=ax_gnmi, positions=[3])

gnmi_plot4 = gnmi_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), ax=ax_gnmi, positions=[4])


netconf_df1 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_12ifaces.csv')
netconf_df2 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_24ifaces.csv')
netconf_df3 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_36ifaces.csv')
netconf_df4 = pd.read_csv('netconf_performance_measurements_translation_and_materialization_48ifaces.csv')

print("NETCONF performance measurements for YANG to NGSI-LD translation and materialization: \n")

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

plot1 = netconf_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf, positions=[1])

plot2 = netconf_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf, positions=[2])

plot3 = netconf_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf, positions=[3])

plot4 = netconf_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf, positions=[4])

ax_gnmi.set_xlabel('Number of network interfaces')
ax_gnmi.set_ylabel('Latency (milliseconds)')
ax_gnmi.set_title('YANG to NGSI-LD translation and materialization \n performance for gNMI')
ax_gnmi.set_xticks([1, 2, 3, 4], ['12', '24', '36', '48'])

ax_netconf.set_xlabel('Number of network interfaces')
ax_netconf.set_ylabel('Latency (milliseconds)')
ax_netconf.set_title('YANG to NGSI-LD translation and materialization \n performance for NETCONF')
ax_netconf.set_xticks([1, 2, 3, 4], ['12', '24', '36', '48'])

plt.tight_layout()

plt.savefig("performance_measurements_translation_and_materialization_old.png", format="png", dpi=1500)
plt.show()