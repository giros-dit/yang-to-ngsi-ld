import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['processed_notifications', 'processing_time_since_observed_at', 'iteration_execution_time', 'mean_execution_time']

df = pd.read_csv('gnmi_json_parser_notifications_with_ngsi_ld_instantiator_performance_measurements.csv')

selected_df = df[headers]

print(selected_df)

selected_df.set_index('processed_notifications').plot()

plt.title('notifier-tester -- Evaluation times per notification received')
plt.xlabel('gnmi-json-parser-notifications-with-ngsi-ld-instantiator index')
plt.ylabel('time (in ms)')
plt.show()