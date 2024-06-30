'''
Code based on: https://naartti.medium.com/analyse-docker-stats-with-python-pandas-2c2ed735cfcd
'''
import os
import re
import matplotlib.pylab as plt
import pandas as pd
import seaborn as sns

# Read data and create DataFrame
df = pd.read_csv('docker-stats-gnmi-testbed.csv', delimiter=r"\s\s+", engine="python")

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

df_gnmi_collectors = df.query('NAME == "gnmic-collector-queries" | NAME == "gnmic-collector-subscriptions"')

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_gnmi_collectors.index, y="mem_percentage", hue="NAME", data=df_gnmi_collectors, drawstyle="steps")
plt.legend(fontsize="x-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from gnmic-collector-queries and gnmic-collector-subscriptions services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-gnmi-collectors-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_gnmi_collectors.index, y="cpu_percentage", hue="NAME", data=df_gnmi_collectors, drawstyle="steps")
plt.legend(fontsize="x-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from gnmic-collector-queries and gnmic-collector-subscriptions services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-gnmi-collectors-cpu.png')
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

df_notifications_parser= df[df['NAME'] == 'gnmi-json-parser-notifications-with-ngsi-ld-instantiator']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_notifications_parser.index, y="mem_percentage", hue="NAME", data=df_notifications_parser, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from gnmi-json-parser-notifications-with-ngsi-ld-instantiator service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-notifications-parser-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_notifications_parser.index, y="cpu_percentage", hue="NAME", data=df_notifications_parser, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from gnmi-json-parser-notifications-with-ngsi-ld-instantiator service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-notifications-parser-cpu.png')
plt.close()

df_queries_parser= df[df['NAME'] == 'gnmi-json-parser-queries-with-ngsi-ld-instantiator']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_queries_parser.index, y="mem_percentage", hue="NAME", data=df_queries_parser, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from gnmi-json-parser-queries-with-ngsi-ld-instantiator service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-queries-parser-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_queries_parser.index, y="cpu_percentage", hue="NAME", data=df_queries_parser, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from gnmi-json-parser-queries-with-ngsi-ld-instantiator service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-queries-parser-cpu.png')
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

df_xrv9k= df[df['NAME'] == 'clab-telemetry-testbed-srl-srl-4hosts-r1']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_xrv9k.index, y="mem_percentage", hue="NAME", data=df_xrv9k, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from clab-telemetry-testbed-srl-srl-4hosts-r1 service (Nokia SR Linux)")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-srl1-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_xrv9k.index, y="cpu_percentage", hue="NAME", data=df_xrv9k, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from clab-telemetry-testbed-srl-srl-4hosts-r1 service (Nokia SR Linux)")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-srl1-cpu.png')
plt.close()

df_xrv9k= df[df['NAME'] == 'clab-telemetry-testbed-srl-srl-4hosts-r2']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_xrv9k.index, y="mem_percentage", hue="NAME", data=df_xrv9k, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from clab-telemetry-testbed-srl-srl-4hosts-r2 service (Nokia SR Linux)")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-srl2-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_xrv9k.index, y="cpu_percentage", hue="NAME", data=df_xrv9k, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from clab-telemetry-testbed-srl-srl-4hosts-r2 service (Nokia SR Linux)")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-srl2-cpu.png')
plt.close()

df_clab_pc_nodes = df.query('NAME.str.startswith("clab") & NAME.str.contains("pc")')

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_clab_pc_nodes.index, y="mem_percentage", hue="NAME", data=df_clab_pc_nodes, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from ContainerLab PC nodes services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-clab-pc-nodes-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_clab_pc_nodes.index, y="cpu_percentage", hue="NAME", data=df_clab_pc_nodes, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from ContainerLab PC nodes services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-clab-pc-nodes-cpu.png')
plt.close()

df_clab_ceos_nodes = df.query('NAME.str.startswith("clab") & ~NAME.str.contains("pc") & NAME != "clab-telemetry-testbed-xrv9k-ceos-4hosts-r1"')

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_clab_ceos_nodes.index, y="mem_percentage", hue="NAME", data=df_clab_ceos_nodes, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from ContainerLab Arista cEOS nodes services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-clab-ceos-nodes-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_clab_ceos_nodes.index, y="cpu_percentage", hue="NAME", data=df_clab_ceos_nodes, drawstyle="steps")
plt.legend(fontsize="xx-small")
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from ContainerLab Arista cEOS nodes services")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-clab-ceos-nodes-cpu.png')
plt.close()

df_topology_discoverer= df[df['NAME'] == 'topology-discoverer']

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_topology_discoverer.index, y="mem_percentage", hue="NAME", data=df_topology_discoverer, drawstyle="steps")
plt.legend()
plt.ylabel("RAM [%]")
plt.xlabel("Timeline")
plt.title(f"Memory [%] stats from df_topology_discoverer service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-topology-discoverer-ram.png')
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(18, 7))

sns.lineplot(x=df_topology_discoverer.index, y="cpu_percentage", hue="NAME", data=df_topology_discoverer, drawstyle="steps")
plt.legend()
plt.ylabel("CPU [%]")
plt.xlabel("Timeline")
plt.title(f"CPU [%] stats from df_topology_discoverer service")
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.grid()
plt.savefig('docker-stats-topology-discoverer-cpu.png')
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