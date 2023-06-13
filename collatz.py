def collatz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

num = int(input("Enter an integer: "))

while num != 1:
    num = collatz(num)
