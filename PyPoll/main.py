#main
import pandas as pd

def summary(x):
	return str(round((x/ total_votes)*100))+'%  (' + str(x) +')'


file_path = 'election_data.csv'
data_frame = pd.read_csv(file_path)

total_votes = len(data_frame['Voter ID'])
candidate_value = data_frame['Candidate'].value_counts()
winner = candidate_value.max()

new_frame = pd.DataFrame(candidate_value)
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------')
print(candidate_value.apply(summary))
print('-------------------------')
print('Winner: ' + str(new_frame[new_frame['Candidate'] == winner]['Candidate']))
print('-------------------------')

_file = open('Election Summary.txt', 'w')
_file.write('Election Results\n')
_file.write('-------------------------\n')
_file.write('Total Votes: ' + str(total_votes))
_file.write('\n-------------------------\n')
_file.write(candidate_value.apply(summary).to_string(index=False))
_file.write('\n-------------------------\n')
_file.write('Winner: ' + str(new_frame[new_frame['Candidate'] == winner]['Candidate'].to_string(index=False)))
_file.write('\n-------------------------\n')


_file.close()

