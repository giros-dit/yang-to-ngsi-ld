import pandas as pd
import matplotlib.pyplot as plt

all_materialization_data = []
all_virtualization_data = []

df_materialization_notification = pd.read_csv('notification_performance_measurements_materialization-subs-on-change-iteration-1.csv')
all_materialization_data.append(df_materialization_notification['evaluation_time'])

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 1: \n")

mean_materialization_notification = df_materialization_notification ['evaluation_time'].mean()
standard_deviation_materialization_notification  = df_materialization_notification ['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification)
print("\n")

df_virtualization_notification = pd.read_csv('notification_performance_measurements_virtualization-subs-on-change-cs-iteration-1.csv')
all_virtualization_data.append(df_virtualization_notification['evaluation_time'])

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization -  Iteration 1: \n")

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
plt.title('Mean evaluation time per notification in \n NETCONF RPC subscription operation')
plt.savefig("notification_performance_measurements_data_integration-iteration-1.png", format="png", dpi=1500)

df_materialization_notification = pd.read_csv('notification_performance_measurements_materialization-subs-on-change-iteration-2.csv')
all_materialization_data.append(df_materialization_notification['evaluation_time'])

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 2: \n")

mean_materialization_notification = df_materialization_notification ['evaluation_time'].mean()
standard_deviation_materialization_notification  = df_materialization_notification ['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification)
print("\n")

df_virtualization_notification = pd.read_csv('notification_performance_measurements_virtualization-subs-on-change-cs-iteration-2.csv')
all_virtualization_data.append(df_virtualization_notification['evaluation_time'])

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization -  Iteration 2: \n")

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
plt.title('Mean evaluation time per notification in \n NETCONF RPC subscription operation')
plt.savefig("notification_performance_measurements_data_integration-iteration-2.png", format="png", dpi=1500)

df_materialization_notification = pd.read_csv('notification_performance_measurements_materialization-subs-on-change-iteration-3.csv')
all_materialization_data.append(df_materialization_notification['evaluation_time'])

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization - Iteration 3: \n")

mean_materialization_notification = df_materialization_notification ['evaluation_time'].mean()
standard_deviation_materialization_notification  = df_materialization_notification ['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification)
print("\n")

df_virtualization_notification = pd.read_csv('notification_performance_measurements_virtualization-subs-on-change-cs-iteration-3.csv')
all_virtualization_data.append(df_virtualization_notification['evaluation_time'])

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization -  Iteration 3: \n")

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
plt.title('Mean evaluation time per notification in \n NETCONF RPC subscription operation')
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

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization: \n")

mean_materialization_notification_all = df_materialization_notification_all ['evaluation_time'].mean()
standard_deviation_materialization_notification_all  = df_materialization_notification_all['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification_all)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_materialization_notification_all ['evaluation_time']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_materialization_notification_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
materialization_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

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

print("NETCONF RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization: \n")

mean_virtualization_notification_all = df_virtualization_notification_all ['evaluation_time'].mean()
standard_deviation_virtualization_notification_all  = df_virtualization_notification_all ['evaluation_time'].std()
print("Data virtualization - Mean subscription notification time:", mean_virtualization_notification_all)
print("Data virtualization - Subscription notification standard deviation:", standard_deviation_virtualization_notification_all)
print("\n")

# Calculate Q1, Q3, and IQR
column_data = df_virtualization_notification_all ['evaluation_time']
q1 = column_data.quantile(0.25)
q3 = column_data.quantile(0.75)
iqr = q3 - q1

# Calculate bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Determine outliers
outliers = column_data[
    (column_data < lower_bound) |
    (column_data >= upper_bound)
]

# Count outliers ocurrences
print("Outliers: ")
print(outliers)
print("Outliers ocurrences:" + str(len(outliers)))
coverage = len(outliers) / len(df_virtualization_notification_all)
print(f"Percentage of outliers: {coverage * 100:.2f}%")
virtualization_outlier_percentage = coverage * 100
outlier_counts = outliers.value_counts()
print(outlier_counts)

print("\n")

fig, ax = plt.subplots()

plot_materialization_notification_all = df_materialization_notification_all.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_notification_all = df_virtualization_notification_all.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = True, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plt.xticks([1, 2], ['Materialization', 'Virtualization_CS'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean evaluation time per notification in \n NETCONF RPC subscription operation')

# Texto estadístico
text_outliers_materialization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % materialization_outlier_percentage
))

text_outliers_virtualization = '\n'.join((
    r'$Outliers=$',
    r'$%.2f$ %%' % virtualization_outlier_percentage
))

# Estilo del recuadro
props = dict(boxstyle='round', facecolor='white', alpha=0.8)

# Añadir recuadro en esquina inferior izquierda
ax.text(0.05, 0.05, text_outliers_materialization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', horizontalalignment='left', bbox=props, color='blue')

# Añadir recuadro en esquina inferior derecha
ax.text(0.95, 0.05, text_outliers_virtualization, transform=ax.transAxes,
        fontsize=10, verticalalignment='bottom', horizontalalignment='right', bbox=props, color='grey')

plt.savefig("notification_performance_measurements_data_integration-with-outliers.png", format="png", dpi=1500)