num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #strings, number, boolean
fruit = ('blueberry', 'strawberry', 'banana')#strings
print(type(fruit)) #type check
print(pizza_toppings[1]) # log statemnet
pizza_toppings.append('Mushrooms')
print(person['name']) # log statemnet
person['name'] = 'George' #strings
person['eye_color'] = 'blue'# strings
print(fruit[2]) # log statemnet

if num1 > 45: # if
    print("It's greater")# log statemnet
else: #else
    print("It's lower")# log statemnet

if len(string) < 5: #if
    print("It's a short word!")# log statemnet
elif len(string) > 15: #else if 
    print("It's a long word!") # log statemnet
else: #else
    print("Just right!")# log statemnet

for x in range(5): #for loop , start=0, stop=5, inc=1
    print(x)# log statemnet
for x in range(2,5): #for loop, start=2, stop=5, inc=1
    print(x)# log statemnet
for x in range(2,10,3):#for loop, start=2, inc=3
    print(x)# log statemnet
x = 0 #var statement
while(x < 5): #while loop, start=x, stop=5
    print(x) # log statemnet
    x += 1 #increment

pizza_toppings.pop() #function
pizza_toppings.pop(1)#function

print(person)# log statemnet
person.pop('eye_color')#function
print(person)# log statemnet

for topping in pizza_toppings: #for loop, start=pizza_topping[0], stop=pizza_topping[pizza_topping.length-1] 
    if topping == 'Pepperoni':# if 
        continue # continue
    print('After 1st if statement')# log statemnet
    if topping == 'Olives': #if
        break #break

def print_hello_ten_times(): #function
    for num in range(10): #for, 
        print('Hello')# log statemnet

print_hello_ten_times()# log statemnet

def print_hello_x_times(x):#function
    for num in range(x):#for
        print('Hello')# log statemnet

print_hello_x_times(4)# log statemnet

def print_hello_x_or_ten_times(x = 10):#function
    for num in range(x):#for
        print('Hello')# log statemnet

print_hello_x_or_ten_times()# log statemnet
print_hello_x_or_ten_times(4)# log statemnet


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)