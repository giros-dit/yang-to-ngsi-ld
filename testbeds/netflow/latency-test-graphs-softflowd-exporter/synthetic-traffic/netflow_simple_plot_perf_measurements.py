import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['processed_notifications', 'iteration_execution_time', 'mean_execution_time']

df = pd.read_csv('netflow_simple_performance_measurements.csv')

selected_df = df[headers]

print(selected_df.dtypes)
print(selected_df)

selected_df.set_index('processed_notifications').plot()

plt.title('netflow-json-parser-with-ngsi-ld-instantiator (simple) - Execution times per processed notification')
plt.xlabel('netflow-json-parser-with-ngsi-ld-instantiator index')
plt.ylabel('time (in ms)')
plt.savefig('netflow_simple_performance_measurements.png')
plt.show()