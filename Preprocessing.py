import pandas as pd

file_path = 'Datasets\BPI_Challenge_2012_csvfile.csv'
data = pd.read_csv(file_path)


filtered_data = data[['case:concept:name', 'concept:name', 'time:timestamp']]
sequence_lengths = filtered_data.groupby('case:concept:name').size()
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(sequence_lengths, bins=25, edgecolor='black')
plt.title('Histogram of Sequence Lengths')
plt.xlabel('Sequence Length')
plt.ylabel('Count')
plt.show()

sequence_lengths = data.groupby('case:concept:name').size().reset_index(name='Sequence Length')
print(sequence_lengths)