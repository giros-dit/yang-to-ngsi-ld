import pandas as pd
import matplotlib.pyplot as plt

df_materialization_notification = pd.read_csv('notification_performance_measurements_materialization_on-change.csv')
df_materialization_instantiation = pd.read_csv('notification_instantiation_performance_measurements_materialization_on-change.csv')

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data materialization: \n")

mean_materialization_notification = df_materialization_notification ['evaluation_time'].mean()
standard_deviation_materialization_notification  = df_materialization_notification ['evaluation_time'].std()
print("Data materialization - Mean subscription notification time:", mean_materialization_notification)
print("Data materialization - Subscription notification standard deviation:", standard_deviation_materialization_notification)
print("\n")

mean_materialization_instantiation = df_materialization_instantiation ['iteration_execution_time'].mean()
standard_deviation_materialization_instantiation  = df_materialization_instantiation ['iteration_execution_time'].std()
print("Data materialization - Mean subscription notification instantiation time:", mean_materialization_instantiation)
print("Data materialization - Subscription notification instantiation standard deviation:", standard_deviation_materialization_instantiation)
print("\n")

df_virtualization_notification = pd.read_csv('notification_performance_measurements_virtualization_on-change_context_source.csv')
df_virtualization_instantiation = pd.read_csv('notification_instantiation_performance_measurements_virtualization_on-change_context_source.csv')

print("gNMI RPC Subscription performance measurements for YANG to NGSI-LD translation using data virtualization: \n")

mean_virtualization_notification = df_virtualization_notification ['evaluation_time'].mean()
standard_deviation_virtualization_notification  = df_virtualization_notification ['evaluation_time'].std()
print("Data virtualization (on-change Context Source) - Mean subscription notification time:", mean_virtualization_notification)
print("Data virtualization (on-change Context Source) - Subscription notification standard deviation:", standard_deviation_virtualization_notification)
print("\n")

mean_virtualization_instantiation = df_virtualization_instantiation ['iteration_execution_time'].mean()
standard_deviation_virtualization_instantiation  = df_virtualization_instantiation ['iteration_execution_time'].std()
print("Data virtualization (on-change Context Source) - Mean subscription notification instantiation time:", mean_virtualization_instantiation)
print("Data virtualization (on-change Context Source) - Subscription notification instantiation standard deviation:", standard_deviation_virtualization_instantiation)
print("\n")

df_virtualization_notification_periodic = pd.read_csv('notification_performance_measurements_virtualization_periodic.csv')

mean_virtualization_notification_periodic = df_virtualization_notification_periodic ['evaluation_time'].mean()
standard_deviation_virtualization_notification_periodic  = df_virtualization_notification_periodic ['evaluation_time'].std()
print("Data virtualization (periodic Context Broker) - Mean subscription notification time:", mean_virtualization_notification_periodic)
print("Data virtualization (periodic Context Broker) - Subscription notification standard deviation:", standard_deviation_virtualization_notification_periodic)
print("\n")

fig, ax = plt.subplots()

plot_materialization_notification = df_materialization_notification.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_notification = df_virtualization_notification.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
plot_virtualization_notification_periodic = df_virtualization_notification_periodic.boxplot(column = ['evaluation_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

plt.xticks([1, 2, 3], ['materialization', 'virtualization_CS', 'virtualization_CB'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean evaluation time per notification in \n gNMI RPC subscription operation')
plt.savefig("notification_performance_measurements_data_integration_with_virtualization_periodic.png", format="png", dpi=1500)

fig, ax = plt.subplots()

plot_materialization_instantiation = df_materialization_instantiation.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_virtualization_instantiation = df_virtualization_instantiation.boxplot(column = ['iteration_execution_time'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])

plt.xticks([1, 2], ['materialization', 'virtualization_CS'])
plt.xlabel('Data integration approach')
plt.ylabel('Latency (milliseconds)')
plt.title('Mean instantiation time per notification in \n gNMI RPC subscription operation')
plt.savefig("notification_instantiation_performance_measurements_data_integration.png", format="png", dpi=1500)