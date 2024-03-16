import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Notifications received', 'Notification evaluation time', 'Mean evaluation time']

df = pd.read_csv('notifier_tester_perf.csv', names = headers)
print(df.dtypes)
print(df)

df.set_index('Notifications received').plot()

plt.title('notifier-tester -- Evaluation times per notification received')
plt.xlabel('notification index')
plt.ylabel('time (in ms)')
plt.show()