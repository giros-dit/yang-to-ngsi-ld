import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('netconf_performance_measurements_translation_12ifaces.csv')
df2 = pd.read_csv('netconf_performance_measurements_translation_24ifaces.csv')
df3 = pd.read_csv('netconf_performance_measurements_translation_36ifaces.csv')
df4 = pd.read_csv('netconf_performance_measurements_translation_48ifaces.csv')

print("NETCONF performance measurements for YANG to NGSI-LD translation: \n")

mean_1 = df1['iteration_execution_time'].mean()
standard_deviation_1 = df1['iteration_execution_time'].std()
print("12 Interfaces - Mean:", mean_1)
print("12 Interfaces - Standard deviation:", standard_deviation_1)
print("\n")

mean_2 = df2['iteration_execution_time'].mean()
standard_deviation_2 = df2['iteration_execution_time'].std()
print("24 Interfaces - Mean:", mean_2)
print("24 Interfaces - Standard deviation:", standard_deviation_2)
print("\n")

mean_3 = df3['iteration_execution_time'].mean()
standard_deviation_3 = df3['iteration_execution_time'].std()
print("36 Interfaces - Mean:", mean_3)
print("36 Interfaces - Standard deviation:", standard_deviation_3)
print("\n")

mean_4 = df4['iteration_execution_time'].mean()
standard_deviation_4 = df4['iteration_execution_time'].std()
print("48 Interfaces - Mean:", mean_4)
print("48 Interfaces - Standard deviation:", standard_deviation_4)

fig, ax = plt.subplots()

plot1 = df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[1])

plot2 = df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plot3 = df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[3])

plot4 = df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[4])

plt.xticks([1, 2, 3, 4], ['12', '24', '36', '48'])
plt.xlabel('Number of network interfaces')
plt.ylabel('Latency (milliseconds)')
plt.title('YANG to NGSI-LD translation performance for NETCONF')
plt.suptitle('')
plt.savefig("netconf_performance_measurements_translation.png", format="png", dpi=1500)
plt.show()