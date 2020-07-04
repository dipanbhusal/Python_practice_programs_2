import csv 

def csv_reader(csv_file):
    with open(csv_file, newline='') as csv_data:
        csv_reader = csv.DictReader(csv_data )
        result_dict ={}
        result_list = []
        for row in csv_reader:
            result_dict['Name'] = row['Name']
            result_dict['Address'] = row['Address']
            result_dict['Age'] = row['Age']
            result_list.append(result_dict)
    print(result_list)
csv_reader('information.csv')