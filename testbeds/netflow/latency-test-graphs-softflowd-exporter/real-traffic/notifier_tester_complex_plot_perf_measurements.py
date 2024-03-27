import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['notifications_received', 'evaluation_time', 'mean_evaluation_time']

df = pd.read_csv('notifier_tester_complex_performance_measurements.csv')

selected_df = df[headers]

print(selected_df.dtypes)
print(selected_df)

selected_df.set_index('notifications_received').plot()

plt.title('notifier-tester (complex) - Evaluation times per notification received')
plt.xlabel('notification index')
plt.ylabel('time (in ms)')
plt.savefig('notifier_tester_complex_performance_measurements.png')
plt.show()