import csv 

def csv_writer(filename, info_tuple):
    with open(filename+'.csv', mode = "w") as csv_data:
        header = ['Name', 'Address', 'Age']
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(header)
        for row in info_tuple:
            csv_writer.writerow(row)
        csv_data.close()

csv_writer('information', [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)])