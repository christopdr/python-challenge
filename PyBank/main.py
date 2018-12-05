#main
import pandas as pd

file_path = 'budget_data.csv'
data_frame = pd.read_csv(file_path, encoding='utf-8')

total_months = data_frame['Date'].count()
total_amount = data_frame['Profit/Losses'].sum()
average_change = data_frame['Profit/Losses'].mean()

great_increase = data_frame['Profit/Losses'].max()
great_decrease = data_frame['Profit/Losses'].min()

increase_month = data_frame[data_frame['Profit/Losses'] == great_increase]
decrease_month = data_frame[data_frame['Profit/Losses'] == great_decrease]

delta = []
profit_list = data_frame['Profit/Losses'].tolist()
for counter in range(1,len(data_frame['Profit/Losses'])):
	delta.append(profit_list[counter] - profit_list[counter - 1])

print(sum(delta)/ len(delta))


print('Financial Analysis')
print('------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average_change}')

print(f"Greatest Increase in Profits: {increase_month['Date'].to_string(index=False)} ({increase_month['Profit/Losses'].to_string(index=False)})")
print(f"Greatest Decrease in Profits: {decrease_month['Date'].to_string(index=False)} ({decrease_month['Profit/Losses'].to_string(index=False)})")

_file = open('Financial Analysis.txt', 'w')
_file.write('Financial Analysis\n')
_file.write('------------------\n')
_file.write('Total Months: ' + str(total_months))
_file.write('\nTotal: $'+ str(total_amount))
_file.write('\nAverage Change: $'+ str(average_change))
_file.write('\nGreatest Increase in Profits: '+ str(increase_month['Date'].to_string(index=False)) + '(' +str(increase_month['Profit/Losses'].to_string(index=False))+')')
_file.write('\nGreatest Decrease in Profits: '+ str(decrease_month['Date'].to_string(index=False)) + '(' +str(decrease_month['Profit/Losses'].to_string(index=False))+')')

_file.close()