import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['notifications_received', 'evaluation_time', 'mean_evaluation_time']

df = pd.read_csv('performance_measurements_materialization_on-change.csv')

selected_df = df[headers]

print(selected_df.dtypes)
print(selected_df)

selected_df.set_index('notifications_received').plot()

plt.title('notifier-tester-materialization-on-change \n Evaluation times per notification until entity created')
plt.xlabel('notification index')
plt.ylabel('time (in ms)')
plt.savefig("notifier_tester_materialization_on-change_perf_graph_entity_created.png")
plt.show()


headers = ['notifications_received', 'evaluation_time', 'mean_evaluation_time']

df = pd.read_csv('notification_performance_measurements_materialization_on-change.csv')

selected_df = df[headers]

print(selected_df.dtypes)
print(selected_df)

selected_df.set_index('notifications_received').plot()

plt.title('notifier-tester-materialization-on-change \n Evaluation times per notification until notification received')
plt.xlabel('notification index')
plt.ylabel('time (in ms)')
plt.savefig("notifier_tester_materialization_on-change_perf_graph_notification_received.png")
plt.show()