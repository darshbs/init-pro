def fizzBuzz(n):
    if n > 0:
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                print("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                print("Buzz")
            elif i % 3 != 0 and i % 5 != 0:
                print(i)



fizzBuzz(15)