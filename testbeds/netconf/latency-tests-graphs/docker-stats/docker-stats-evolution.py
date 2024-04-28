'''
Code based on: https://naartti.medium.com/analyse-docker-stats-with-python-pandas-2c2ed735cfcd
'''
import os
import re
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sns

# Read data and create DataFrame
df = pd.read_csv('docker-stats-netconf-testbed.csv', delimiter=r"\s\s+", engine="python")

# Remove repeating headers
df = df[df.NAME != "NAME"]

# Parse the data
def percentage_to_float(df_col):
    return df_col.apply(lambda x: float(x[0:-1]))

def split_on_slash(df_col, split_index):
    return df_col.apply(lambda x: x.split(" / ")[split_index])

def get_only_characters(string):
    return re.sub('[^a-zA-Z]+', '', string)

def get_only_numbers(string):
    return float(re.sub('[^\d\.]', '', string))

def to_bit(value):
    return int({
        "b": get_only_numbers(value) * 1,
        "kib": get_only_numbers(value) * 10e3,
        "kb": get_only_numbers(value) * 10e3,
        "mib": get_only_numbers(value) * 10e6,
        "mb": get_only_numbers(value) * 10e6,
        "gib": get_only_numbers(value) * 10e9,
        "gb": get_only_numbers(value) * 10e9,
    }.get(get_only_characters(value).lower(), 0))

df["mem_usage"] = split_on_slash(df["MEM USAGE / LIMIT"], 0).apply(to_bit)
df["mem_limit"] = split_on_slash(df["MEM USAGE / LIMIT"], 1).apply(to_bit)
df["mem_percentage"] = percentage_to_float(df["MEM %"])
df["cpu_percentage"] = percentage_to_float(df["CPU %"])
df["PIDS"] = df["PIDS"].apply(int)
df["net_in"] = split_on_slash(df["NET I/O"], 0).apply(to_bit)
df["net_out"] = split_on_slash(df["NET I/O"], 1).apply(to_bit)
df["block_in"] = split_on_slash(df["BLOCK I/O"], 0).apply(to_bit)
df["block_out"] = split_on_slash(df["BLOCK I/O"], 1).apply(to_bit)

df_kafka = df.query('NAME == "kafka" | NAME == "zookeeper"')

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_kafka.index, y="mem_percentage", hue="NAME", data=df_kafka, drawstyle="steps")
plt.legend()
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from kafka and zookeeper services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-kafka-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_kafka.index, y="cpu_percentage", hue="NAME", data=df_kafka, drawstyle="steps")
plt.legend()
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from kafka and zookeeper services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-kafka-cpu.png')
plt.close()

df_scorpio = df.query('NAME == "scorpio" | NAME == "postgres" | NAME == "context-catalog"')

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_scorpio.index, y="mem_percentage", hue="NAME", data=df_scorpio, drawstyle="steps")
plt.legend()
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from scorpio, postgres, and context-catalog services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-scorpio-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_scorpio.index, y="cpu_percentage", hue="NAME", data=df_scorpio, drawstyle="steps")
plt.legend()
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from scorpio, postgres, and context-catalog services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-scorpio-cpu.png')
plt.close()

df_gnmi_collectors = df.query('NAME.str.contains("ncclient-collector")')

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_gnmi_collectors.index, y="mem_percentage", hue="NAME", data=df_gnmi_collectors, drawstyle="steps")
plt.legend(fontsize="x-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from ncclient-collector services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-ncclient-collectors-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_gnmi_collectors.index, y="cpu_percentage", hue="NAME", data=df_gnmi_collectors, drawstyle="steps")
plt.legend(fontsize="x-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from ncclient-collector services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-ncclient-collectors-cpu.png')
plt.close()

df_notifier_tester = df[df['NAME'] == 'notifier-tester']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_notifier_tester.index, y="mem_percentage", hue="NAME", data=df_notifier_tester, drawstyle="steps")
plt.legend()
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from notifier-tester service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-notifier-tester-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_notifier_tester.index, y="cpu_percentage", hue="NAME", data=df_notifier_tester, drawstyle="steps")
plt.legend()
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from notifier-tester service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-notifier-tester-cpu.png')
plt.close()

df_notifications_parser= df[df['NAME'] == 'xml-parser-with-ngsi-ld-instantiator']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_notifications_parser.index, y="mem_percentage", hue="NAME", data=df_notifications_parser, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from xml-parser-with-ngsi-ld-instantiator service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-netconf-notifications-parser-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_notifications_parser.index, y="cpu_percentage", hue="NAME", data=df_notifications_parser, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from xml-parser-with-ngsi-ld-instantiator service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-netconf-notifications-parser-cpu.png')
plt.close()

df_xe_r1= df[df['NAME'] == 'clab-telemetry-ixiac-lab-r1']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_xe_r1.index, y="mem_percentage", hue="NAME", data=df_xe_r1, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from clab-telemetry-ixiac-lab-r1 service (Cisco XE CSR1000v)")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-xe-r1-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_xe_r1.index, y="cpu_percentage", hue="NAME", data=df_xe_r1, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from clab-telemetry-ixiac-lab-r1 service (Cisco XE CSR1000v)")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-xe-r1-cpu.png')
plt.close()

df_xe_r2= df[df['NAME'] == 'clab-telemetry-ixiac-lab-r2']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_xe_r2.index, y="mem_percentage", hue="NAME", data=df_xe_r2, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from clab-telemetry-ixiac-lab-r2 service (Cisco XE CSR1000v)")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-xe-r2-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_xe_r2.index, y="cpu_percentage", hue="NAME", data=df_xe_r2, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from clab-telemetry-ixiac-lab-r2 service (Cisco XE CSR1000v)")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-xe-r2-cpu.png')
plt.close()

df_ixia_c= df[df['NAME'] == 'clab-telemetry-ixiac-lab-ixia-c']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_ixia_c.index, y="mem_percentage", hue="NAME", data=df_ixia_c, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from IXIA-C service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-ixia-c-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_ixia_c.index, y="cpu_percentage", hue="NAME", data=df_ixia_c, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from IXIA-C service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-ixia-c-cpu.png')
plt.close()

df_clab_nodes = df.query('NAME.str.startswith("clab")')

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_clab_nodes.index, y="mem_percentage", hue="NAME", data=df_clab_nodes, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from ContainerLab services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-clab-nodes-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_clab_nodes.index, y="cpu_percentage", hue="NAME", data=df_clab_nodes, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from ContainerLab services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-clab-nodes-cpu.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df.index, y="mem_percentage", hue="NAME", data=df, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from Docker microservices")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df.index, y="cpu_percentage", hue="NAME", data=df, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from Docker microservices")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-cpu.png')
plt.close()