import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Processed notifications',
            'Processing time since observedAt',
            'Iteration execution time',
            'Mean execution time']

df = pd.read_csv('xml_parser_with_ngsi_ld_instantiator_perf.csv', names = headers)
print(df.dtypes)
print(df)

df.set_index('Processed notifications').plot()

plt.title('xml-parser-with-ngsi-ld-instantiator -- Execution times per processed notification')
plt.xlabel('processed notifications')
plt.ylabel('time (in ms)')
plt.show()

plt.savefig("xml_parser_with_ngsi-ld_instantiator_perf_graph.png")

