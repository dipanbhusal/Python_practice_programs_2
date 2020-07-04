def is_prime(number):
    if number <= 1: 
        return False
    for i in range(3,number):
        if number % i == 0:
            return False 
    return True

print(is_prime(199))