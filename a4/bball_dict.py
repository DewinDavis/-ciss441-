import csv
import json 
bball_2019 = []
row_count = 0

with open('complete.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for bball_row_dic in reader:
        row_count += 1
        bball_2019.append(bball_row_dic)
        if row_count <=10 or row_count % 10000 ==0:
            print('{0:>5}) team: {1:<20} conference: {2:<15} seed: {3}'.format(
                row_count, bball_row_dic['TEAM'], bball_row_dic['CONF'],
                bball_row_dic['SEED']))
            print(bball_row_dic['TEAM'])

print('found this many rows: ' + str(len(bball_2019)))

with open('bball_data.json', 'w') as fp:
    json.dump(bball_2019, fp, sort_keys=True, indent=4, separators=(',', ': '))

print('The CSV has been converted to json')
