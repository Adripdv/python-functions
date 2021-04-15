# def greet():
#   return "Hello Adriana"

# print(greet())

'''Functions with parameters'''

# def greet(name):

#     '''
#     Greets a person passed in as an argument
#     name: a name of a person to greet
#     '''  

#     return f"Hello {name}, Good morning"
    
# print(greet('Adriana', 'Jose')) # TypeError: greet() takes 1 positional argument but 2 were given
# print(greet('Felix'))
# print(greet('Kinglsey'))

# help(greet)

#==============================================

'''Arbitray parameters (*args)'''

# def fruits(*name):
#   ''' 
#   Accepts unknown number of fruit names and prints each of them
#   *name: list of fruits 
#   ''' 
#   #names are tuple 
#   for fruit in name:
#     print(fruit)

# fruits('Orange', 'Banana', 'Apple', 'Grapes')

#==============================================

'''keyword parameters'''

# def greet(name, msg):
#   '''
#   This function greets a person with a given message
#   name: person to greet 
#   msg: message to greet person with
#   '''
#   return f'Hello {name}, {msg}'

# # print(greet('Adriana', 'Good morning!'))
# # print(greet('Good morning', 'Adriana!'))

# # Using keyword the order of the parameters won't matter 
# print(greet(name='Adriana', msg='Good morning!'))
# print(greet(msg='Good morning', name='Adriana!'))

#==============================================

'''Arbitray keyword (**Kwargs)'''

# def person(**student):

#   # print(type(student)) # Dictionary
#   # print(student)
#     for key in student:
#       print(student[key])

# person(Fname='Adriana', Lname='Oliveira', subject='Python')

#==============================================

'''default parameter values'''

# def greet(name='Dear'):
#   return f'Hello, {name}'

# print(greet()) # TypeError: greet() missing 1 required positional argument: 'name' (add name place holder e.g. (def greet(name='Dear'))
# print(greet('Adriana'))

# '''pass statment'''

# def greet(): 
#   pass 

#==============================================

'''Recursion'''

# def factorial_recursive(n):
#     '''
#     Multiply a given number by every number less than it downt to 1 in a factorial way
#     e.g if n is 5 then calculate 5*4*3*2*1 = 120
#     n: is the highest starting number
#     '''
#     if n == 1:
#         return True
#     else:
#         return n * factorial_recursive(n -1)

# print(factorial_recursive(5))

#==============================================
'''Variable scope'''

# # outside the function (out of the function scope)
# total = 10

# def add_nums (arg1, arg2):
#   # inside the function 
#     total = arg1 + arg2
#     print(total)
    
# # add_nums(3, 3)
# # print(total)
# add_nums(total, 2)

#==============================================
'''Function return keyword'''

def add_nums (arg1, arg2):
    total = arg1 + arg2
    
    return total
    
# print(add_nums(2,2))
# print(add_nums(2,2) * 3)
# newTotal = add_nums(2,2)
# print(newTotal)


