filename = 'myfileinlongername.txt'
variable = ''
if '.' in filename:
    variable = filename[:-4]
print(variable)