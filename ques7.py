
friends_list = [('Henry', 'Smith', 22),('Bishwo', 'Poudel', None),('Nawaraj', 'Poudel', 19),('Dipan', 'Bhusal', 21),('Rita', 'KC', 25),('Hari', 'Khadka', None)]
sum_age = 0
count = 0
for i in friends_list:
    if i[2] != None:
        count += 1
        sum_age += i[2]
avg_age = sum_age//count

for i in friends_list:
    
    if i[2] != None:
        print(i[0],  end=':-')
        if i[2] > avg_age:
            print('Old')
        else: 
            print('Young')
