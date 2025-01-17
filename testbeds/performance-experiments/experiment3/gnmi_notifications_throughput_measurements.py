import pandas as pd
import matplotlib.pyplot as plt

df_gnmi_extraction = pd.read_csv('gnmi_collector_throughput_measurements_translation.csv')
df_gnmi_translation = pd.read_csv('json_parser_throughput_measurements_translation.csv')
df_gnmi_instantiation = pd.read_csv('json_parser_throughput_measurements_instantiation.csv')

print("gNMI telemetry notifications throughput measurements in events/second for YANG to NGSI-LD translation using data materialization: \n")

mean_gnmi_extraction_records = df_gnmi_extraction ['throughput_records'].mean()
standard_gnmi_extraction_records  = df_gnmi_extraction ['throughput_records'].std()
print("Data extraction - Mean subscription notification throughput (events/second):", mean_gnmi_extraction_records)
print("Data extraction - Subscription notification throughput standard deviation (events/second):", standard_gnmi_extraction_records)
print("\n")

mean_gnmi_translation_records = df_gnmi_translation ['throughput_records'].mean()
standard_gnmi_translation_records  = df_gnmi_translation ['throughput_records'].std()
print("Data translation - Mean subscription notification throughput (events/second):", mean_gnmi_translation_records)
print("Data translation - Subscription notification throughput standard deviation (events/second):", standard_gnmi_translation_records)
print("\n")

mean_gnmi_instantiation_records  = df_gnmi_instantiation ['throughput_records'].mean()
standard_gnmi_instantiation_records = df_gnmi_instantiation ['throughput_records'].std()
print("Data instantiation - Mean subscription notification throughput (events/second):", mean_gnmi_instantiation_records)
print("Data instantiation  - Subscription notification throughput standard deviation (events/second):", standard_gnmi_instantiation_records)
print("\n")

fig, ax = plt.subplots()

plot_gnmi_extraction_events = df_gnmi_extraction.boxplot(column = ['throughput_records'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_gnmi_translation_events = df_gnmi_translation.boxplot(column = ['throughput_records'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
#plot_gnmi_instantiation_events = df_gnmi_instantiation.boxplot(column = ['throughput_records'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

#plt.xticks([1, 2, 3], ['extraction', 'translation', 'instantiation'])
plt.xticks([1, 2], ['extraction', 'translation'])
plt.xlabel('Data integration phase')
plt.ylabel('Throughput (events/second)')
plt.title('Throughput for integrating \n gNMI telemetry notifications')
plt.savefig("gnmi_notifications_throughput_measurements_events.png", format="png", dpi=1500)

fig, ax = plt.subplots()

plot_gnmi_instantiation_events = df_gnmi_instantiation.boxplot(column = ['throughput_records'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[1])

plt.xticks([1], ['instantiation'])
plt.xlabel('Data integration phase')
plt.ylabel('Throughput (events/second)')
plt.title('Throughput for integrating \n gNMI telemetry notifications')
plt.savefig("gnmi_notifications_throughput_measurements_events_instantiation.png", format="png", dpi=1500)

print("gNMI telemetry notifications throughput measurements in bytes/second for YANG to NGSI-LD translation using data materialization: \n")

mean_gnmi_extraction_bytes = df_gnmi_extraction ['throughput_bytes'].mean()
standard_gnmi_extraction_bytes  = df_gnmi_extraction ['throughput_bytes'].std()
print("Data extraction - Mean subscription notification throughput (bytes/second):", mean_gnmi_extraction_bytes)
print("Data extraction - Subscription notification throughput standard deviation (bytes/second):", standard_gnmi_extraction_bytes)
print("\n")

mean_gnmi_translation_bytes = df_gnmi_translation ['throughput_bytes'].mean()
standard_gnmi_translation_bytes  = df_gnmi_translation ['throughput_bytes'].std()
print("Data translation - Mean subscription notification throughput (bytes/second):", mean_gnmi_translation_bytes)
print("Data translation - Subscription notification throughput standard deviation (bytes/second):", standard_gnmi_translation_bytes)
print("\n")

mean_gnmi_instantiation_bytes  = df_gnmi_instantiation ['throughput_bytes'].mean()
standard_gnmi_instantiation_bytes = df_gnmi_instantiation ['throughput_bytes'].std()
print("Data instantiation - Mean subscription notification throughput (bytes/second):", mean_gnmi_instantiation_bytes)
print("Data instantiation  - Subscription notification throughput standard deviation (bytes/second):", standard_gnmi_instantiation_bytes)
print("\n")

fig, ax = plt.subplots()

plot_gnmi_extraction_bytes = df_gnmi_extraction.boxplot(column = ['throughput_bytes'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax, positions=[1])
plot_gnmi_translation_bytes = df_gnmi_translation.boxplot(column = ['throughput_bytes'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax, positions=[2])
#plot_gnmi_instantiation_bytes = df_gnmi_instantiation.boxplot(column = ['throughput_bytes'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[3])

#plt.xticks([1, 2, 3], ['extraction', 'translation', 'instantiation'])
plt.xticks([1, 2], ['extraction', 'translation'])
plt.xlabel('Data integration phase')
plt.ylabel('Throughput (bytes/second)')
plt.title('for integrating \n gNMI telemetry notifications')
plt.savefig("gnmi_notifications_throughput_measurements_bytes.png", format="png", dpi=1500)

fig, ax = plt.subplots()

plot_gnmi_instantiation_bytes = df_gnmi_instantiation.boxplot(column = ['throughput_bytes'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax, positions=[1])

plt.xticks([1], ['instantiation'])
plt.xlabel('Data integration phase')
plt.ylabel('Throughput (bytes/second)')
plt.title('for integrating \n gNMI telemetry notifications')
plt.savefig("gnmi_notifications_throughput_measurements_bytes_instantiation.png", format="png", dpi=1500)
