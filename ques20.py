class Validity:
    def check(self, list_of_number):
        list_of_number.sort()
        result_list = []
        for first in list_of_number:
            for second in list_of_number:
                for third in list_of_number:       
                    summ = first + second + third 
                    numbers = [first, second, third]
                    if summ == 0:
                        numbers.sort()           
                        if numbers not in result_list:
                            result_list.append(numbers)
        return result_list
obj = Validity()
result = obj.check([-25, -10, -7, -3, 2, 4, 8, 10, -5,-5])
print(result)