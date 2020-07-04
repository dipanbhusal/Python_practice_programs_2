friends_list = ['MAdan', 'Bija']
print('Before Sort')
print(id(friends_list[0]))
friends_list.append('Dipan')
friends_list.append('Jack')
friends_list.append('Ram')
friends_list.append('Ana')

friends_list.sort()
print('After sort')
print(id(friends_list[0]))
print(f'First item after sort: {friends_list[0]}')
print(f'Second item after sort: {friends_list[1]}')