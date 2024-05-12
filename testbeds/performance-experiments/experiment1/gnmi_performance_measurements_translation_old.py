import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('gnmi_performance_measurements_translation_12ifaces.csv')
df2 = pd.read_csv('gnmi_performance_measurements_translation_24ifaces.csv')
df3 = pd.read_csv('gnmi_performance_measurements_translation_36ifaces.csv')
df4 = pd.read_csv('gnmi_performance_measurements_translation_48ifaces.csv')

print("gNMI performance measurements for YANG to NGSI-LD translation: \n")

mean_1 = df1['iteration_execution_time'].mean()
standard_deviation_1 = df1['iteration_execution_time'].std()
print("12 Interfaces - Mean (1 event):", mean_1)
print("12 Interfaces - Standard deviation (1 event):", standard_deviation_1)
print("12 Interfaces - Mean (12 events):", mean_1 * 12)
print("12 Interfaces - Standard deviation (12 events):", standard_deviation_1 * 12)
print("\n")

mean_2 = df2['iteration_execution_time'].mean()
standard_deviation_2 = df2['iteration_execution_time'].std()
print("24 Interfaces - Mean:", mean_2)
print("24 Interfaces - Standard deviation:", standard_deviation_2)
print("24 Interfaces - Mean (24 events):", mean_2 * 24)
print("24 Interfaces - Standard deviation (24 events):", standard_deviation_2 * 24)
print("\n")

mean_3 = df3['iteration_execution_time'].mean()
standard_deviation_3 = df3['iteration_execution_time'].std()
print("36 Interfaces - Mean:", mean_3)
print("36 Interfaces - Standard deviation:", standard_deviation_3)
print("36 Interfaces - Mean (36 events):", mean_3 * 36)
print("36 Interfaces - Standard deviation (36 events):", standard_deviation_3 * 36)
print("\n")

mean_4 = df4['iteration_execution_time'].mean()
standard_deviation_4 = df4['iteration_execution_time'].std()
print("48 Interfaces - Mean:", mean_4)
print("48 Interfaces - Standard deviation:", standard_deviation_4)
print("48 Interfaces - Mean (48 events):", mean_4 * 48)
print("48 Interfaces - Standard deviation (48 events):", standard_deviation_4 * 48)

df1['iteration_execution_time'] *= 12
df2['iteration_execution_time'] *= 24
df3['iteration_execution_time'] *= 36
df4['iteration_execution_time'] *= 48

fig, axes = plt.subplots()

plot1 = df1.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), ax=axes, positions=[1])

plot2 = df2.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), ax=axes, positions=[2])

plot3 = df3.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), ax=axes, positions=[3])

plot4 = df4.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), ax=axes, positions=[4])

plt.xticks([1, 2, 3, 4], ['12', '24', '36', '48'])
plt.tight_layout()
plt.xlabel('Number of network interfaces')
plt.ylabel('Latency (milliseconds)')
plt.title('YANG to NGSI-LD translation performance for gNMI')
plt.suptitle('')
plt.savefig("gnmi_performance_measurements_translation_old.png", format="png", dpi=1500)
plt.show()