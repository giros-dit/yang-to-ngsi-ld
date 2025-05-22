import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('notification_performance_measurements_virtualization_on-change_context_source.csv')

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization: \n")

mean = df['evaluation_time'].mean()
standard_deviation = df['evaluation_time'].std()
print("Mean:", mean)
print("Standard deviation:", standard_deviation)
print("\n")

fig, ax = plt.subplots()

plot1 = df.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[1])

plt.xticks([1], ['1000'])
plt.xlabel('Number of notifications')
plt.ylabel('Latency (milliseconds)')
plt.title('notifier-tester-virtualization-on-change-context-source \n Distribution evaluation time per notification until notification received')
plt.savefig("notification_performance_measurements_virtualization_on-change_context_source_distribution.png", format="png", dpi=1500)
plt.show()