import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Create custom legend handles
legend_handles = [
    Patch(facecolor='grey', edgecolor='yellow', label='ORION'),
    Patch(facecolor='blue', edgecolor='red', label='SCORPIO')
]

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

fig, ax = plt.subplots()

scorpio_plot1 = scorpio_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])

scorpio_plot2 = scorpio_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[2])

scorpio_plot3 = scorpio_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[3])

scorpio_plot4 = scorpio_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[4])

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

orion_plot1 = orion_df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[1])

orion_plot2 = orion_df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

orion_plot3 = orion_df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[3])

orion_plot4 = orion_df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[4])

plt.legend(handles=legend_handles)
plt.xticks([1, 2, 3, 4], ['12', '24', '36', '48'])
plt.xlabel('Number of network interfaces')
plt.ylabel('Latency (milliseconds)')
plt.title('YANG to NGSI-LD translation and materialization performance for NETCONF')
plt.suptitle('')
plt.savefig("netconf_performance_measurements_translation_and_materialization_brokers.png", format="png", dpi=1500)
plt.show()