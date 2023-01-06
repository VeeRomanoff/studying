import random


# coffee_prices = {'latte': 4.15, 'Cappuccino': 4.55, 'Americano': 3.55, 'Espresso': 2.95}

# coffee_prices = {
#     'latte': 4.15,
#     'cappuccino': {'Price': 4.55, "is_having_milk": True, 'hotteness': 'warm'},
#     'Americano': 3.55,
#     'Espresso': 2.95,
#     'customers': ['children', 'teenagers', 'adults']
# }
# # print(coffee_prices)

# print(coffee_prices['customers'][1])

# print(coffee_prices.keys())
# print(coffee_prices.values())
# print(coffee_prices.items())

###############
# TUPLES
###############

# tuple_1 = (1, 2, 3)
# tuple_2 = ('hello', 'one')
# tuple_3 = ('hello', 88, 22.1)

# x = y = z = 1, 2, 3

# print(x, y, z)

# print(type(tuple_1))
# print(tuple_3[2])

# person = ('Billy', 'Butcher', 'Super')
# first_name, last_name, kind = person
# print(person.count('Billy'))
# numbres = (1, 2, 1, 2, 2, 22, 2, 25, 1, 6, 1, 2, 2, 1, 1, 2, 2, 5, 5)
# # print(numbres.count(2))
# print(numbres.index(25))
# print(numbres.index(22))

###############
# SETS
###############

# rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'dark blue', 'purple'}
# print(type(rainbow_colors))

# number_list = [22, 5, 677, 12, 2, 2, 2, 2, 2, 2, 2, 2, 677, 22, 5, 7, 12]
# person_dictionary = {'Name': 'Jack', 'Age': 41}
# countries_tuple = ('Iran', 'USA', 'Morocco')

# set_from_list = set(number_list)
# set_from_person = set(person_dictionary)
# set_from_countries = set(countries_tuple) 

# set_from_list.add(500000)
# set_from_countries.add('Canada')
# set_from_person.add('hobbies')

# set_from_countries.remove('Iran')
# set_from_countries.discard('Irana')

# print(set_from_list)
# print(set_from_person)
# print(set_from_countries)

# some_set = {'fuck', 'you'}
# # print(type(some_set))
# some_set.add('bitch')
# print(some_set)

###############
# LOGICAL OPERATORS
###############

# x = 22 + 10
# y = 66 + 44

# print(x == 32 and y == 110)
# print(x == 32 or y == 110)
# print(not True) #False 

###############
# CONDITIONALS 
###############


# day_time = input('What time of day is it right now?: ')

# if day_time == 'morning':
#     print('Vee is gibing Partow good mornings / Partwo gives him Good mornings :D')
# elif day_time == 'afternoon':
#     print('Partow and Vee probably minding their own business right now')
# elif day_time == 'late afternoon':
#     print('Vee and Partow are studying right now')
# elif day_time == 'evening':
#     print('Vee and Partow are finishing their studies and about to have some dinner :D')
# elif day_time == 'night': 
#     print('Vee and Partow are about to kick off long night talkings :)')
# elif day_time == 'midnight':
#     print('Vee and Partow goodnighting each other / Vee and Partow are sleeping')
# else:
#     print('Vee and Partow are up to something')
    

# print('hello world!')


###############
# LOOPS 
###############

# number_list = [1, 2, 2, 3, 4, 5, 4, 5, 5, 6, 7, 8, 9, 10, 30, 22, 156, 67]

# for number in number_list: 
#     if number % 2 == 0:
#         print(str(number) + ' is even')
#     else:
#         print(str(number) + ' is odd')

# list_numbers_sum = 0

# for num in number_list:
#     list_numbers_sum = list_numbers_sum + num
# print(list_numbers_sum)

###############
# THIS IS HOW YOU UNPACK TUPLES IN A LOOP
###############


# tuple_list =    [('a', 'b', 1), ('c', 'd', 27), ('e', 'f', 52)]

# for letter_1, letter_2, number_1 in tuple_list:
#     print(letter_1, letter_2, number_1)
    

###############
# THIS IS HOW YOU GET KEYS:VALUES IN DICTIONARIES
###############

# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
# for item in dictionary.items():
#     print(item)



# x = 0

# while x < 10:
#     print('x is less than 10')
#     x += 1
# else:
#     print('x is not less than 10')
    



# PASS, BREAK, CONTINUE

# some_list = [1, 2, 5, 14]

# for item in some_list:
#     pass
# print('are u ok?')


# for item in some_list:
#     if item == 1:
#         break
#     print(item)

# for item in some_list:
#     if item == 5:
#         continue
#     print(item)


# my_string = 'sdfgawodpds'
# letter_index = 0
# for letter in my_string:
#     print(letter + ' is at index ' + str(letter_index))
#     letter_index += 1

# for index, letter in enumerate(my_string): 
#     print(letter + ' is at index ' + str(index))


# my_letter_list = ['a', 'b', 'c', 'bdsa', False]
# print(False in my_letter_list)




# print(min(62, 21, 2, 67, 22, 1))
# print(max(62, 21, 2, 67, 22, 1))

# my_list = [62, 21, 2, 67, 22, 1]
# print(min('That\'s probably my second programming language i\'m currently learning'))

# from random import shuffle
# from random import randint

# my_list = [62, 21, 2, 67, 22, 1]
# print(randint(1, 20))

# import this




###############
# LIST COMPREHENSION 
###############


greeting = 'hello!!'
# letter_list = []
# for letter in greeting:
#     letter_list.append(letter)

# print(letter_list)

###############
# THE SORTEST WAY >>>

# letter_list = [letter for letter in greeting]
# print(letter_list)

# number_list = [number for number in '123456789']
# number_list1 = [num for num in range(10)]
# print(number_list1)


# number_list = [1, 52, 2535, -115, 22, 66, 156, -884, 12, -33]
# new_list = [number for number in number_list if number > 0]
# print(new_list)



###############
# NESTED LIST
###############

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11]]
# print(nested_list)
# print(len(nested_list))
# print(len(nested_list[-1]))
# print(nested_list[2][3])


# for inner_list in nested_list:
#     print(inner_list)
    
    
# for inner_list in nested_list:
#     for number in inner_list:
#         print(number)



###############
# FUNCTIONS
###############



# import random

# def say_hello(name = 'stranger', ):
#     """Says hello to whatever name you pick and provides the age

#     Args:
#         name (_type_): _description_
#         age (_type_): _description_
#     """
#     print(f'Hello {name}')
    
# say_hello()


# def get_even_numbers(list):
#     """gives us all even numbers from given list of random numbers 

#     Args:
#         list (_type_): list of random numbres
#     """
#     even_list = []
#     for num in list:
#         if num % 2 == 0:
#             even_list.append(num)
#     return even_list


# numbers_list = []
# for x in range(20): # Здесь указывается СКОЛЬКО ВСЕГО ЦИФР будет в листе 
#     numbers_list.append(random.randint(0, 20)) # здесь указывается какие цифры ВООБЩЕ будут в листе (от, до)
    
# print('these are usual numbres list: ', numbers_list)
# print('these are all even numbres from this list: ', get_even_numbers(numbers_list))


# def sum_of_numbres(a = 0, b = 0):
#     """this function adds two numbres together...

#     Args:
#         a (int, optional): _description_. Defaults to 0.
#         b (int, optional): _description_. Defaults to 0.

#     Returns:
#         Sum of a & b
#     """
#     return a + b
# the_number_from_function = sum_of_numbres(a = 20, b = 40)
# print(the_number_from_function + 40)

# the_text = 'This is some toext that you probably are never gonna read. I don\'t even know what is best for us, but one thing you can\'t take away... I am Iron Man.. '

# def find_the_word_in_text(word, text):
#     if word in text.lower():
#         return True
#     else:
#         return False

# print(find_the_word_in_text('this', the_text))

## THE SORTESET WAY FOR THAT >>>



# def find_the_word_in_text(word, text):
#     return word in text.lower() # because the operator IN reutrns True or False depending on wheter there is an element in a sequence

# print(find_the_word_in_text('this', the_text))


# def greeting_depending_on_gender(name, gender):
#     if gender == 'male':
#         print('Hello ' + name + ' you look handsome ;)')
#         return gender
#     elif gender == 'female':
#         print('Hello ' + name + ' You look gorgeus! ;)')
#         return gender
#     else:
#         print('Hello ' + name + ' Wow, who the fuck are you?!')
#         return gender

# returned_value = greeting_depending_on_gender('R8chel', 'Amicagender')
# print(returned_value)



###############
# MAP, FILTER & LAMBDA
###############


###############
# M A P >>>>>

# def sum_of_two_numbers(a):
#     return a + a

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for elem in number_list:
#     print(sum_of_two_numbers(elem))
    

## THE SHORTEST WAY OF DOING THAT >>>

# result = map(sum_of_two_numbers, number_list)
# print(result)

# for item in result:
#     print(item)


# def is_a_in_string(string):
#     if 'a' in string.lower():
#         print('Yay! "a" is in string!')
#         return True
#     else:
#         print('Ops.. there is no "a" in the string :(')
#         return False
        
# string_list = ['Dimension', 'Aqua', 'Trouble', 'DNA', 'Solution']

# print(list(map(is_a_in_string, string_list)))

## ANOTHER EXAMPLE WITH MAP >>>

# import random

# list_of_numbers = []
# for x in range(15):
#     list_of_numbers.append(random.randint(0, 15))


# def turn__numbers_into_cubes(list):
#     return list ** 3

# result = turn__numbers_into_cubes
# print(list(map(result, list_of_numbers)))


###############
# F I L T E R >>>>>


# def is_number_odd(number):
#     return number % 2 == 1

# some_list = []
# for x in range(20):
#     some_list.append(x)

# for number in filter(is_number_odd, some_list):
#     print(number)

###############
# LAMBDA EXPRESSION >>>>>

# def cube(number):
#     return number ** 3


# some_list = []
# for x in range(9):
#     some_list.append(x)

# print(list(map(lambda number: number ** 3, some_list)))

# string_list = ['Hannah', 'create', 'will', 'lol', 'diego']
# print(list(map(lambda string: string[::-1], string_list)))


# son = 'Jack'
# def changin_name():
#     global son
#     print(son)
    
# changin_name()
# print(son)

# car = {
#     'brand': 'chevy',
#     'price': 17000000,
#     'color': 'yellow',
# }

# some_other_car = {
#     'price': 17000000,
#     'color': 'yellow',
#     'brand': 'chevy',
# }

# one_key = 'price'

# car[one_key] = 20000000
# print(car)


import asyncio

async def foo():
    print('what?')

foo()