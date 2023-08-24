def fizzbuzz(numero):
    num = numero
    
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
       return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    return num




assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(6) == 'Fizz'
assert fizzbuzz(4) == 4
assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz(10) == 'Buzz'
assert fizzbuzz(15) == 'FizzBuzz'

for numero in range(1,100):
    print(fizzbuzz(numero))
