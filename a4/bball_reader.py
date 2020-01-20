import csv

with open ('complete.csv', 'r') as csvfile:
    bball_stream = csv.reader(csvfile, quotechar='"')
    for bball_row_list in bball_stream:
        print(', '.join(bball_row_list))
    
