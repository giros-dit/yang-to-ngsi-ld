import pandas as pd
import matplotlib.pyplot as plt

all_materialization_data = []
all_virtualization_data = []

df_materialization_notification = pd.read_csv('notification_performance_measurements_materialization-subs-on-change-iteration-1.csv')
all_materialization_data.append(df_materialization_notification['evaluation_time'])

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 1: \n")

mean_materialization_notification = df_materialization_notification ['evaluation_time'].mean()
standard_deviation_materialization_notification  = df_materialization_notification ['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification)
print("\n")

df_virtualization_notification = pd.read_csv('notification_performance_measurements_virtualization-subs-on-change-cs-iteration-1.csv')
all_virtualization_data.append(df_virtualization_notification['evaluation_time'])

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization -  Iteration 1: \n")

mean_virtualization_notification = df_virtualization_notification ['evaluation_time'].mean()
standard_deviation_virtualization_notification  = df_virtualization_notification ['evaluation_time'].std()
print("Data virtualization - Mean subscription notification time:", mean_virtualization_notification)
print("Data virtualization - Subscription notification standard deviation:", standard_deviation_virtualization_notification)
print("\n")

fig, ax = plt.subplots()

plot_materialization_notification = df_materialization_notification.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_notification = df_virtualization_notification.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plt.xticks([1, 2], ['materialization', 'virtualization_CS'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean notification time in \n gNMI RPC subscription operation')
plt.savefig("notification_performance_measurements_data_integration-iteration-1.png", format="png", dpi=1500)

df_materialization_notification = pd.read_csv('notification_performance_measurements_materialization-subs-on-change-iteration-2.csv')
all_materialization_data.append(df_materialization_notification['evaluation_time'])

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 2: \n")

mean_materialization_notification = df_materialization_notification ['evaluation_time'].mean()
standard_deviation_materialization_notification  = df_materialization_notification ['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification)
print("\n")

df_virtualization_notification = pd.read_csv('notification_performance_measurements_virtualization-subs-on-change-cs-iteration-2.csv')
all_virtualization_data.append(df_virtualization_notification['evaluation_time'])

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization -  Iteration 2: \n")

mean_virtualization_notification = df_virtualization_notification ['evaluation_time'].mean()
standard_deviation_virtualization_notification  = df_virtualization_notification ['evaluation_time'].std()
print("Data virtualization - Mean subscription notification time:", mean_virtualization_notification)
print("Data virtualization - Subscription notification standard deviation:", standard_deviation_virtualization_notification)
print("\n")

fig, ax = plt.subplots()

plot_materialization_notification = df_materialization_notification.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_notification = df_virtualization_notification.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plt.xticks([1, 2], ['materialization', 'virtualization_CS'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean notification time in \n gNMI RPC subscription operation')
plt.savefig("notification_performance_measurements_data_integration-iteration-2.png", format="png", dpi=1500)

df_materialization_notification = pd.read_csv('notification_performance_measurements_materialization-subs-on-change-iteration-3.csv')
all_materialization_data.append(df_materialization_notification['evaluation_time'])

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 3: \n")

mean_materialization_notification = df_materialization_notification ['evaluation_time'].mean()
standard_deviation_materialization_notification  = df_materialization_notification ['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification)
print("\n")

df_virtualization_notification = pd.read_csv('notification_performance_measurements_virtualization-subs-on-change-cs-iteration-3.csv')
all_virtualization_data.append(df_virtualization_notification['evaluation_time'])

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization -  Iteration 3: \n")

mean_virtualization_notification = df_virtualization_notification ['evaluation_time'].mean()
standard_deviation_virtualization_notification  = df_virtualization_notification ['evaluation_time'].std()
print("Data virtualization - Mean subscription notification time:", mean_virtualization_notification)
print("Data virtualization - Subscription notification standard deviation:", standard_deviation_virtualization_notification)
print("\n")

fig, ax = plt.subplots()

plot_materialization_notification = df_materialization_notification.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_notification = df_virtualization_notification.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plt.xticks([1, 2], ['materialization', 'virtualization_CS'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean notification time in \n gNMI RPC subscription operation')
plt.savefig("notification_performance_measurements_data_integration-iteration-3.png", format="png", dpi=1500)


materialization_files = [
    'notification_performance_measurements_materialization-subs-on-change-iteration-1.csv',
    'notification_performance_measurements_materialization-subs-on-change-iteration-2.csv',
    'notification_performance_measurements_materialization-subs-on-change-iteration-3.csv'
]

df_materialization_notification_all = pd.concat(
    [pd.read_csv(file) for file in materialization_files],
    ignore_index=True
)

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization: \n")

mean_materialization_notification_all = df_materialization_notification_all ['evaluation_time'].mean()
standard_deviation_materialization_notification_all  = df_materialization_notification_all['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification_all)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification_all)
print("\n")

virtualization_files = [
    'notification_performance_measurements_virtualization-subs-on-change-cs-iteration-1.csv',
    'notification_performance_measurements_virtualization-subs-on-change-cs-iteration-2.csv',
    'notification_performance_measurements_virtualization-subs-on-change-cs-iteration-3.csv'
]

df_virtualization_notification_all = pd.concat(
    [pd.read_csv(file) for file in virtualization_files],
    ignore_index=True
)

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization: \n")

mean_virtualization_notification_all = df_virtualization_notification_all ['evaluation_time'].mean()
standard_deviation_virtualization_notification_all  = df_virtualization_notification_all ['evaluation_time'].std()
print("Data virtualization - Mean subscription notification time:", mean_virtualization_notification_all)
print("Data virtualization - Subscription notification standard deviation:", standard_deviation_virtualization_notification_all)
print("\n")

fig, ax = plt.subplots()

plot_materialization_notification_all = df_materialization_notification_all.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_notification_all = df_virtualization_notification_all.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plt.xticks([1, 2], ['Materialization', 'Virtualization_CS'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean notification time in \n gNMI RPC subscription operation')

# Texto estadístico
text_materialization = '\n'.join((
   # r'Materialization',
    r'$\mu=%.2f$ ms' % mean_materialization_notification_all,
    r'$\sigma=%.2f$ ms' % standard_deviation_materialization_notification_all
))

text_virtualization = '\n'.join((
   # r'Virtualization_CS',
    r'$\mu=%.2f$ ms' % mean_virtualization_notification_all,
    r'$\sigma=%.2f$ ms' % standard_deviation_virtualization_notification_all
))

# Estilo del recuadro
props = dict(boxstyle='round', facecolor='white', alpha=0.8)

# Añadir ambos recuadros en esquinas opuestas
ax.text(0.05, 0.05, text_materialization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', bbox=props, color='blue')

ax.text(0.95, 0.95, text_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', horizontalalignment='right', bbox=props, color='grey')

plt.savefig("notification_performance_measurements_data_integration.png", format="png", dpi=1500)