array = [0, 1, 2, 3, 4, 5]
sum = 0
number = 1

if len(array) <= 0:
     print(0)
else:
     for number in range(len(array)):
         if number % 2 != 0:
            sum = sum + array[number]
     result = sum * array[-1]
     print(result)
