import pandas as pd
import matplotlib.pyplot as plt

df_netconf_extraction = pd.read_csv('netconf_collector_throughput_measurements_translation.csv')
df_netconf_translation = pd.read_csv('xml_parser_throughput_measurements_translation.csv')
df_netconf_instantiation = pd.read_csv('xml_parser_throughput_measurements_instantiation.csv')
df_netconf_instantiation['throughput_records_per_second'] = (
    df_netconf_instantiation['throughput_records'] / df_netconf_instantiation['throughput_interval']
)
df_netconf_instantiation['throughput_bytes_per_second'] = (
    df_netconf_instantiation['throughput_bytes'] / df_netconf_instantiation['throughput_interval']
)

print("NETCONF telemetry notifications throughput measurements in events/second for YANG to NGSI-LD translation using data materialization: \n")

mean_netconf_extraction_records = df_netconf_extraction ['throughput_records'].mean()
standard_netconf_extraction_records  = df_netconf_extraction ['throughput_records'].std()
print("Data extraction - Mean subscription notification throughput (events/second):", mean_netconf_extraction_records)
print("Data extraction - Subscription notification throughput standard deviation (events/second):", standard_netconf_extraction_records)
print("\n")

mean_netconf_translation_records = df_netconf_translation ['throughput_records'].mean()
standard_netconf_translation_records  = df_netconf_translation ['throughput_records'].std()
print("Data translation - Mean subscription notification throughput (events/second):", mean_netconf_translation_records)
print("Data translation - Subscription notification throughput standard deviation (events/second):", standard_netconf_translation_records)
print("\n")

mean_netconf_instantiation_records  = df_netconf_instantiation ['throughput_records_per_second'].mean()
standard_netconf_instantiation_records = df_netconf_instantiation ['throughput_records_per_second'].std()
print("Data instantiation - Mean subscription notification throughput (events/second):", mean_netconf_instantiation_records)
print("Data instantiation  - Subscription notification throughput standard deviation (events/second):", standard_netconf_instantiation_records)
print("\n")

fig, (ax_netconf_1, ax_netconf_2) = plt.subplots(1, 2, figsize=(10, 5))

plot_netconf_extraction_events = df_netconf_extraction.boxplot(column = ['throughput_records'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_netconf_1, positions=[1])
plot_netconf_translation_events = df_netconf_translation.boxplot(column = ['throughput_records'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf_1, positions=[2])

ax_netconf_1.set_xticks([1, 2], ['extraction', 'translation'])
'''
ax_netconf_1.set_xlabel('Data integration phase')
ax_netconf_1.set_ylabel('Throughput (events/second)')
ax_netconf_1.set_title('Throughput for integrating \n NETCONF telemetry notifications')
'''

plot_netconf_instantiation_events = df_netconf_instantiation.boxplot(column = ['throughput_records_per_second'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax_netconf_2, positions=[1])

ax_netconf_2.set_xticks([1], ['instantiation'])
ax_netconf_2.yaxis.tick_right()
ax_netconf_2.yaxis.set_label_position("right")
'''
ax_netconf_2.set_xlabel('Data integration phase')
ax_netconf_2.set_ylabel('Throughput (events/second)')
ax_netconf_2.set_title('Throughput for integrating \n NETCONF telemetry notifications')
'''
plt.tight_layout()
fig.text(0.5, 0.04, 'Data integration phase', ha='center', fontsize=12) 
fig.text(0.04, 0.5, 'Throughput (events/second)', va='center', rotation='vertical', fontsize=12)  
fig.suptitle('Throughput for integrating NETCONF telemetry notifications', fontsize=14)

plt.subplots_adjust(left=0.12, right=0.88, top=0.88, bottom=0.12)

plt.savefig("netconf_notifications_throughput_measurements_events_join.png", format="png", dpi=1500)

print("NETCONF telemetry notifications throughput measurements in bytes/second for YANG to NGSI-LD translation using data materialization: \n")

mean_netconf_extraction_bytes = df_netconf_extraction ['throughput_bytes'].mean()
standard_netconf_extraction_bytes  = df_netconf_extraction ['throughput_bytes'].std()
print("Data extraction - Mean subscription notification throughput (bytes/second):", mean_netconf_extraction_bytes)
print("Data extraction - Subscription notification throughput standard deviation (bytes/second):", standard_netconf_extraction_bytes)
print("\n")

mean_netconf_translation_bytes = df_netconf_translation ['throughput_bytes'].mean()
standard_netconf_translation_bytes  = df_netconf_translation ['throughput_bytes'].std()
print("Data translation - Mean subscription notification throughput (bytes/second):", mean_netconf_translation_bytes)
print("Data translation - Subscription notification throughput standard deviation (bytes/second):", standard_netconf_translation_bytes)
print("\n")

mean_netconf_instantiation_bytes  = df_netconf_instantiation ['throughput_bytes_per_second'].mean()
standard_netconf_instantiation_bytes = df_netconf_instantiation ['throughput_bytes_per_second'].std()
print("Data instantiation - Mean subscription notification throughput (bytes/second):", mean_netconf_instantiation_bytes)
print("Data instantiation  - Subscription notification throughput standard deviation (bytes/second):", standard_netconf_instantiation_bytes)
print("\n")

fig, (ax_netconf_1, ax_netconf_2) = plt.subplots(1, 2, figsize=(10, 5))

plot_netconf_extraction_bytes = df_netconf_extraction.boxplot(column = ['throughput_bytes'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "red", linewidth = 1.5), boxprops = dict(facecolor = "blue"), ax=ax_netconf_1, positions=[1])
plot_netconf_translation_bytes = df_netconf_translation.boxplot(column = ['throughput_bytes'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "yellow", linewidth = 1.5), boxprops = dict(facecolor = "grey"), ax=ax_netconf_1, positions=[2])

ax_netconf_1.set_xticks([1, 2], ['extraction', 'translation'])
'''
ax_netconf_1.set_xlabel('Data integration phase')
ax_netconf_1.set_ylabel('Throughput (bytes/second)')
ax_netconf_1.set_title('Throughput for integrating \n NETCONF telemetry notifications')
'''
plot_netconf_instantiation_bytes = df_netconf_instantiation.boxplot(column = ['throughput_bytes_per_second'], vert=True, patch_artist=True, showfliers = False, medianprops = dict(color = "green", linewidth = 1.5), boxprops = dict(facecolor = "white"), ax=ax_netconf_2, positions=[1])

ax_netconf_2.set_xticks([1], ['instantiation'])
ax_netconf_2.yaxis.tick_right()
ax_netconf_2.yaxis.set_label_position("right")
'''
ax_netconf_2.set_xlabel('Data integration phase')
ax_netconf_2.set_ylabel('Throughput (bytes/second)')
ax_netconf_2.set_title('Throughput for integrating \n NETCONF telemetry notifications')
'''
plt.tight_layout()
fig.text(0.5, 0.04, 'Data integration phase', ha='center', fontsize=12) 
fig.text(0.04, 0.5, 'Throughput (bytes/second)', va='center', rotation='vertical', fontsize=12)  
fig.suptitle('Throughput for integrating NETCONF telemetry notifications', fontsize=14)

plt.subplots_adjust(left=0.12, right=0.88, top=0.88, bottom=0.12)

plt.savefig("netconf_notifications_throughput_measurements_bytes_join.png", format="png", dpi=1500)
