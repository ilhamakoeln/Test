# Row = int(input("Enter the number of rows:"))
# Column = int(input("Enter the number of columns:"))
 
# # Initialize matrix
# matrix = []
# print("Enter the entries row wise:")
 
# # For user input
# # A for loop for row entries
# for row in range(Row):    
#     a = []
#     # A for loop for column entries
#     for column in range(Column):   
#         a.append(int(input()))
#     matrix.append(a)


# # For printing the matrix
# for row in range(Row):
#     for column in range(Column):
#         print(matrix[row][column], end=" ")
#     print()

# n, row, column = map(int, input().split())
# matrix = [[0]*n for _ in range(n)]
# num = 1
# layer = 0


# while num <= n*n:
#     for i in range(layer, n-layer):
#         matrix[layer][i] = num
#         num += 1
#     for i in range(layer+1, n-layer):
#         matrix[i][n-layer-1] = num
#         num += 1
#     if num <= n*n:
#         for i in range(n-layer-2, layer-1, -1):
#             matrix[n-layer-1][i] = num
#             num += 1
#     if num <= n*n:
#         for i in range(n-layer-2, layer, -1):
#             matrix[i][layer] = num
#             num += 1
#     layer += 1


# class PerimeterArea:
#     def __init__(self,x, y) :
#         self.x = x
#         self.y = y
#     def  Area(self):
#        return self.x * self.y
    
#     def Perimeter(self):
#        return 2 * (self.x + self.y)
    
# test = PerimeterArea(4,5)

# test_area , test_perimeter = print(test.Area(),  print(test.Perimeter) )

## IMPORTANT

# class OddEven:
#     def __init__(self, x):
#         self.x = x
#     def division(self):
#         if self.x % 2 == 0:
#             return "This number is even"
#         return "This number is odd"



# num1 = int(input("Provide the number : "))   
# test= OddEven(num1)
# print(test.division())

## A. `greet_with_message`

def greet_with_message(username, message = " Hello"):
    print(username + message)


greet_with_message("Ilhama")

## B. `calculate_discount`

def calculate_discount(price, DiscountRate = 10 ):
    DiscountedPrice = price - (price * (DiscountRate/100))
    return DiscountedPrice


# calculate_discount(200)

print(calculate_discount(200))


## C. `sum_all`

def sum_all(*args):
    total = 0
    for number in args:
        total += number
    return total

print(sum_all(4,3,5,6,7))

## D. `calculate_product`

def calculate_product(*args):
    multiplication = 1
    for num in args:
        multiplication *= num
    return multiplication

print(calculate_product(4,5,6,7,8,0))


## E. `sum_of_numbers`

def sum_of_numbers(*args):
    total = 0
    for number in args:  # Loop through each item in args
        if isinstance(number, int):  # Check if the item is an integer
            total += number  # Sum only integer values
    return total

print(sum_of_numbers(4, 3, 5, 6, 7, "Hello World"))  # The string "Hello World" will be ignored


## F. `calculate_power`

def calculate_power(base, exponent):
    return base ** exponent


print(calculate_power(5,3))


## G. `greet_user`

def greet_user(username):
    print("Hello," + username + "!")

greet_user("Ilhama")


## H. `calculate_area`

def calculate_area(radius):
    return radius ** 2


print(calculate_area(5))


## I. `average`

def average(*args):
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1
    return total / count

print(average(10,20,30,40))


## J. `maximum_number`

def maximum_number(*args):
    max_num = args[0] 
    for num in args:
        if num > max_num:
            max_num = num  # Update max_num if current num is larger
    return max_num

print(maximum_number(4,5,6,7))


## K. `greet_with_salutation`

def greet_with_salutation(username, salutation = " Miss "):
    print("Hello" + salutation +  username + "!")

greet_with_salutation("Ilhama")


## L. `calculate_cost`

def calculate_cost(quantity, unitprice, taxrate = 5):
    TotalCost = (quantity * unitprice) + (quantity *unitprice* taxrate / 100)
    return TotalCost


print(calculate_cost(4,100))



## M. `concatenate_strings`

def concatenate_strings(*strings):
    empty = strings[0]
    for i in strings[1:]:
        empty +=" " + i
    return empty

print(concatenate_strings("Ilhama", "Safura", "Sarkhan"))


## N. `calculate_sum_and_product`

def calculate_sum_and_product(*args):
    total = 0
    product = 1
    for i in args:
        total += i
    for i in args:
        product *= i
    return total , product

print(calculate_sum_and_product (4,5))





## O. `find_max_min`

def find_max_min(*args):
    max1 = args[0]
    min1 = args[0]
    for i in args:
        if i > max1:
           max1 = i
    for i in args:
        if i < min1:
           min1 = i 
    return max1, min1


print(find_max_min(3,4,5,6,7))

## P. `calculate_grade`

def calculate_grade(NumericalScore):
    if NumericalScore >= 90 and NumericalScore <= 100:
        grade = "A"
    elif NumericalScore >= 80 and NumericalScore < 90:
        grade = "B"
    elif NumericalScore >= 70 and NumericalScore < 80:
        grade = "C"
    elif NumericalScore >= 60 and NumericalScore < 70:
        grade = "D"
    grade = "E"
    return grade

print(calculate_grade(30))











class Person:
    def __init__(self, age, name):
        self.age = int(age)
        self.name = str(name)

    def greeting(self):
        print("Hello" + self.name)
    def sleep(self):
        print(self.name + " is going to sleep.")

class Animal:
    def __init__(self, name, age, color):
        self.name = str(name)
        self.age = int(age)
        self.color = str(color)

    def eat(self):
        print(self.name + " is going to eat.")
    def run(self):
        print(self.name + " is running.")



Ilhama = Person(28, "Ilhama")

test_ilhama1 = Ilhama.greeting()
test_ilhama2 = Ilhama.sleep()


Toby = Animal("Toby", 2, "blue")

test_toby1 = Toby.eat()
test_toby2 = Toby.run()




