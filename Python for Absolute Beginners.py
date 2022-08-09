# ____basic data types

# integer = 7
# float_num = 2.718
# bool_val = False
# integer = 10

#_______Exponentiation, Floor Division, and Modulo
# exponentiation = 4 ** 4  # 256
# floor_division = 20 // 6  # 3
# modulo = 20 % 6  # 2

# #___Assignment operator
# add_assign = 5
# add_assign += 7  # 12
# print(exponentiation,  floor_division, modulo, add_assign)

# _____Math_____
# print(2.977 * 3.533)  # 10.517741
#
# slice = "Just do it!"
# print(slice[10]) # print "!"

# ____type() and str()_________
# ex_1 = False
# ex_2 = 29
# ex_3 = 4.123
# print(type(ex_1))  # boolean
# print(type(ex_2))  # integer
# print(type(ex_3))  # float

# ex_4 = str(False)
# ex_5 = str(29)
# ex_6 = str(4.123)
# print(type(ex_4))  # <class 'str'>
# print(type(ex_5))  # <class 'str'>
# print(type(ex_6))  # <class 'str'>
#
# ________ escape sequences (\t, \n, \) ____________ 
# print('This\tis\ta\tlot\tof\tspace.')  # \t (tab)
# print(' line one,\n line two')  # \n (new line)
# print('"When i said \'immediately\', I meant today!" said King Saul.')  # \'
# print("\"Do or do not. There is no try.\"")  # \"
# print("All escape sequences contain a \\.")  # \\
# ______________________________________________
#
# var = 3.4335
#
# print(type(var))  # float
# print(str(var) + " is a float")
# print("\"Hello, I`m Pavlo, it`s nice to meet you!\"")
# print('*******\n *****\n  ***\n   *')

# _________input()____________
# name = input('Please enter your name.')
# print("Your name is" + name + ".")
# print(type(name))
#
# fav_num = input("What is your favourite number?")
# print("Your favourite number is " + fav_num + ".")
# print(type(fav_num))
# _________________
# name = input("What is your name?")
# quest = input("What is your quest?")
# color = input ("What is your favourite color?")
# print("So your name is " + name + ", your quest is " + quest + ", and your favourite color is " + color + ".")
#
# _______________________________
#
# number = input("Enter an integer!")
# print(10 + int(number))
#
# ________FUNCTIONS______________________
#
# def function_name(parameter):
#    print(parameter + 2)


# function_name(8) # 10
#  _________________
#
# first_str = "The number "


# def integer(p1, p2, p3, p4):
#  print(p1 + str(p2) + p3 + p4)


# integer(first_str, 16, " is an integer", "!")  # The number 16 is an integer!
#
# ______________________________________
#
# def example(num1=7, num2=8):
#   print(num1 * num2)
#
#
# example()  # 56
#
# ________________---
#
# def example(num1=7, num2=8):
#  return num1 * num2
#
# print(example() + 44) # 100
# ________________________
#
# def hello_world_printer():
#  print("hello world")


# hello_world_printer()  # hello world
# __________________________________
# name = input("What is your name?")


# def name_printer(p1):
#    print(p1)


# name_printer(name)
# ___________________________
# 
# length = int(input("Type length:"))
# width = int(input("Type width:"))
# height = int(input("Type height:"))


# def formula(l, w, h):
#    return l * w * h


# print("The volume of the rectangular prism is " + str(formula(length, width, height)) + " cubic feet.")
# __________________________________
#
# celsius = int(input("Enter an integer value of temperature in celsius:"))
#
#
# def fahrenheit(c):
#    return 1.8 * c + 32
#
#
# print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(float(fahrenheit(celsius))))

# ______MODULES_____________________________
#
# import random
#
# print(random.randint(1, 10))
# __________________________
#
# from random import randint
#
# print(randint(10, 20))
#
# ___________________________________
#
# from random import *
#
# print(random())  #  0 < random number < 1
# ___________________________________
#
# import random
# gallons_gas = random.randint(10, 25)
# miles = random.randint(200, 400)
# mpg = miles // gallons_gas
# print(mpg)
# print(gallons_gas)
# print(miles)
#
# ____variable scope (global, local)_______________________________
#
# example = "hello world"  # global


# def loc_ex():
#     example = "this is a string"  # local
#     return example 

# print(example)  # hello world
# print(loc_ex() ) # this is a string
#________________
# def loc_ex1():
#     fruit = "pear"
#     print(fruit)

# def loc_ex2():
#     fruit = "banana"
#     print(fruit)
    
# fruit = "apple"
# loc_ex1()  # pear
# loc_ex2()  # banana
# print(fruit)  # apple

#_____if statements________________________________________

# veg = input("Type the name of a vegetable:")
#
# if veg == "corn":
#     print("The vegetable is corn.")
#     else:
#     print("The vegetable is not corn.")
# _____________
#
# gpa = float(input("What was the applicant's grade point average?"))
#
# if gpa >= 3.7:
#     inst_app = input("Is the student going to be educated at an approved institution?")
#     if inst_app == "yes" or "y":
#         print("The applicant qualifies for a low APR student loan.")
#     else:
#         print("The application does not qualify since they have not been accepted into an approved institution.")
# else:
#     print("The applicant did not have high enough grades to qualify.")

# _____________elif_______

# user_num = int(input("Please enter an integer."))

# if user_num < 0:
#     print("The number you entered is less tnan 0.")
# elif user_num == 0:
#     print("The number you entered is 0.")
# elif 0 < user_num <= 100:
#     print("The number you entered can be 1, 100, or anything in between.")
# else:
#     print("The number you entered is greater tnan 100.")
#________________________________________________

# score = int(input("Input student's score:"))
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# elif 0 < score < 60:
#     print("F")
# ____________import module__________________
#
# import random
#
# num = random.randint(1, 10)
#
# if num == 1:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is I.")
# elif num == 2:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is II.")
# elif num == 3:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is III.")
# elif num == 4:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is IV.")
# elif num == 5:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is V.")
# elif num == 6:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is VI.")
# elif num == 7:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is VII.")
# elif num == 8:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is VIII.")
# elif num == 9:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is IX.")
# else:
#     print("Number is " + str(num) + "." + "The roman numeral equivalent is X.")

# _______loops____________________________

# _______while loop______________________
# counter = 10

# while counter >= 1:
#     print(counter)
#     counter -= 1
# __________________________________

# user_num = int(input("Please enter your positive integer:"))
# num_sum = user_num
# summed = 0

# while user_num > 0:
#     summed += user_num
#     user_num -= 1


# print(num_sum)
# print(summed)
# ______for loop_________________

# word = "hello world"
#
# for letter in word:
#     print(letter)
# ____________________

# words = input("Please type any text message:")
# count = 0
#
# for char in words:
#     count +=1
#
# print(words)
# print("The number of characters would be " + str(count) + ".")

# _______range()__________________________

# one_input = range(10)
# for num in one_input:
#     print(num)
# _________________________________

# two_inputs = range(5, 10)
# for num in two_inputs:
#     print(num)
# _________________________________
# three_inputs = range(20, 1, -4)
# for num in three_inputs:
#     print(num)
# _________________________________

# for num in range(1, 51):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)
# _________________________________

# def factorial(fac_num):
#     returned = 1
#     for item in range(fac_num, 1, -1):
#         returned *= item

#     return returned
# print(factorial(3))    # 6
# print(factorial(4))    # 24
# print(factorial(5))    # 120

# _______________________ sting methods________
# ____.upper(), .lower()_______________
# all_low = "there are no capitals here."
# print(all_low.upper())
# all_up = "THIS IS SHOUTING TEXT!"
# print(all_up.lower())

# ______.isalpha(), .isalnum(), .isdecimal(), .isspace(), .startswith(), .endwith()______
# print("Batman".isalpha())  # True
# print("Batman123".isalpha())  # False
# print("Batman123".isalnum())  # True
# print("123".isdecimal())  # True (integer)
# print("1,23".isdecimal())  # False (float)
# print("      ".isspace())  # True (space)
# print("not just spaces".isspace())  # False (spaces and letters)
# print(" The Empire Strikes Back".istitle())  # True
# print("this is a string".startswith("this is"))  # True
# print("this is a string".endswith("string"))  # True
# print(" ".join(["one", "two", "three"]))  # one two three
# print("... ".join(["one", "two", "three"]))  # one... two... three
# print("Eggs, Milk, Waffles, Bacon".split(","))  # ['Eggs', 'Milk', 'Waffles', 'Bacon']
# _______________________________

from re import T


mixed_case = "A Song of Ice and Fire"
# print(mixed_case.isupper())  # False
# print(mixed_case.islower())  # False
# print(mixed_case.upper())  # A SONG OF ICE AND FIRE
# print(mixed_case.lower())  # a song of ice and fire
# print(mixed_case.istitle())  # False

# title_case = mixed_case
# print(title_case)  # A Song of Ice and Fire
# print(mixed_case.startswith("A"))  # True
# print(mixed_case.endswith("e"))  # True

# words = mixed_case.split()
# print(words)  # ['A', 'Song', 'of', 'Ice', 'and', 'Fire']

# print(", ".join(words))  # A, Song, of, Ice, and, Fire

# ___________________________________.rjust() and .ljust() and .center()________

# print("hello world".rjust(15, "_"))  # ____hello world
# print("hello world".ljust(15, "*"))  # hello world****
# print("hello world".center(15, "*"))  # **hello world**

# _____________.strip(), .rstrip(), and .lstrip()________
# print("I had an exciting trip!!!111111")  # I had an exciting trip!!!111111
# print("I had an exciting trip!!!111111".strip("1"))  # I had an exciting trip!!!
# print("I had an exciting trip!!!111111".rstrip("1"))  # I had an exciting trip!!!
# print("I had an exciting trip!!!111111".lstrip("1"))  # I had an exciting trip!!!111111

# print("juice, bread, cheese, beef, bread".rstrip(", bread"))  # juice, bread, cheese, beef
# print("blueblueyellowblue".strip("eulb"))  # yellow
# print("Good morning.".replace("morning", "afternoon"))  # Good afternoon.
# _________________________________________________________

# the_string = "North Dakota"
# print(the_string.rjust(17))  #      North Dakota
# print(the_string.ljust(17, "*"))  # North Dakota*****

# center_plus = the_string.center(16, "+")
# print(center_plus)  # ++North Dakota++
# print(the_string.lstrip("North"))  #  Dakota
# print(center_plus.rstrip("+"))  # ++North Dakota
# print(center_plus.strip("+"))  # North Dakota
# print(the_string.replace("North", "South"))  # South Dakota
# _____________________len()___________

# print(len("tree"))  # 4
# print("This" + " " + "is a " + "string.")
# print(len("This" + " " + "is a " + "string."))  # 17
# print('antidisestablishmentarianism'[7:20])  # establishment
# print(len('antidisestablishmentarianism'[7:20]))  # 13

# ___________________________the string reverse________

# user_str = input("Please enter a string:")
# reversed = ""
#
# for user in range(len(user_str) -1, -1, -1):
#     reversed += user_str[user]
#
# print(reversed)
# ___________________________________________-

# user_str = input("Please enter some string:")  # James Bond is 007

# print(user_str.split())  # ['James', 'Bond', 'is', '007']
# print(len(user_str.split()))  # 4

# spaces_and_letters = ""

# for char in user_str:
#     if char.isalnum() or char.isspace() or char == "-" or char == "'":
#         spaces_and_letters += char

# words = spaces_and_letters.split()
# number_of_words = len(words)

# print(words)  # ['James', 'Bond', 'is', '007']
# print(number_of_words)  # 4

# ___________________using.format()______________
# name = input('What is your name?')
# degree = input('What did they major in at college?')
# job = input('What is their current occupation?')
# experience = input('How many years have they been working it their field?')
#
# print(name + " majored in" + degree + ", works as a " + job + ", and has " + experience + " years of experience.")
# print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))

# ______________________list()_________________

# example_list_1 = [5, 4, 3, 2, 1]
# example_list_2 = [2.7443, 3.3433]
# example_list_3 = ["blue", "green", "red", "yellow", "purple", "orange"]
# example_list_4 = [True, False, False, True, False, True, True, False, True]
# example_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# example_list_6 = [10, 3.1456, "tree", False, [1, 2, 3]]

# print(list("blah"))  # ['b', 'l', 'a', 'h']
#
# checked_list = [1, 2, 3, 4]
# print(1 in checked_list)  # True
# print(1 not in checked_list)  # False

# int_list = [3, 3.14, True, "Pavlo", [1, 3, 4]]
# str_arg = int_list[3]

# print("e" in str_arg)  # False
# print("a" not in str_arg)  # False
# ____________________________indexes

# indexes_example = [[1, 3, 4], [6, 7, 8], [19, 34, 54]]
# print(indexes_example[2] [2])  # 54

# ___________________________negative

# negative = [1, 2, 3, 4, 5]
# print(negative[-1])  # 5
#
# mixed = [False, 365, 4.24, "this is a string"]
# print(mixed[2] + 1.76)  # 6.0
# print("I have used \"" + mixed[-1] + "\" as an example too many times.")  # I have used "this is a string" as an example too many times.

#_______list slicing_________________
# sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sliced[:4])  # [1, 2, 3, 4]
# print(sliced[3:8])  # [4, 5, 6, 7, 8]
# print(sliced[6:])  # [7, 8, 9]

#___reassigning a list's items____________
# example = [2, 4, 6, 8, 0]
# print(example)
# example[3] = 10
# print(example)  # [2, 4, 6, 10, 0]
# example[0:2] = [3, 2, 1]
# print(example)  # [3, 2, 1, 6, 10, 0]
#_________________________________________
# var_list = [[0, 2], [4, 6], [8, 10], [12, 14]]
# print(var_list[0])  # [0, 2]
# print(var_list[3] [1])  # 14
#
# str_list = ["chair", "table", "desk", "lamp", "bed"]
# print(str_list[-5])  # chair
# print("Most people own at least {} {}s.".format(var_list[0][1], str_list[0]))  # Most people own at least 2 chairs.
#
# float_list = [0.98, 8.76, 6.54, 4.32]
# print(float_list[1:])  # [8.76, 6.54, 4.32]
# print(float_list[1:3])  # [8.76, 6.54]
# print(float_list[:2])   # [0.98, 8.76]

# ______________del vs.remove()____________-

# str_list = ["chair", "table", "desk", "lamp", "bed"]
# del str_list[0]
# print(str_list)  # ['table', 'desk', 'lamp', 'bed']

# str_list = ["chair", "table", "desk", "lamp", "bed"]
# str_list.remove("lamp")
# print(str_list)  # ['chair', 'table', 'desk', 'bed']

# ___________________.append() and .insert()______________________

# str_list = ["chair", "table", "desk", "lamp", "bed"]
#
# str_list.append("sofa")  
# print(str_list)  # ['chair', 'table', 'desk', 'lamp', 'bed', 'sofa']

# str_list = ["chair", "table", "desk", "lamp", "bed"]
# str_list.insert(2, "sofa")
# print(str_list)  # ['chair', 'table', 'sofa', 'desk', 'lamp', 'bed']

# ________________.sort()_______________
# num_list = [2.145, 4, -23, 0, 1000]
# print(num_list)  # [2.145, 4, -23, 0, 1000]
# num_list.sort()
# print(num_list)  # [-23, 0, 2.145, 4, 1000]
# num_list.sort(reverse=True)
# print(num_list)  # [1000, 4, 2.145, 0, -23]
#
# str_list = ["Pavlo", "Volodymyr", "Olha", "Elmira", "Margaryta"]
# print(str_list)  # ['Pavlo', 'Volodymyr', 'Olha', 'Elmira', 'Margaryta']
# str_list.sort()
# print(str_list)  # ['Elmira', 'Margaryta', 'Olha', 'Pavlo', 'Volodymyr']
# str_list.sort(reverse=True)
# print(str_list)  # ['Volodymyr', 'Pavlo', 'Olha', 'Margaryta', 'Elmira']

# mixed = [False, 4,3342, -3]
# mixed.sort()
# print(mixed)  # [-3, False, 4, 3342] # False = 0 

# ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
# ASCIIbetical.sort()
# print(ASCIIbetical)  # ['Andy', 'Brian', 'Karen', 'apple', 'banana', 'kiwi']
# ASCIIbetical.sort(key=str.lower)
# print(ASCIIbetical)  # ['Andy', 'apple', 'banana', 'Brian', 'Karen', 'kiwi']

# ___________________.index() and .pop()___________________
# str_list = ["Pavlo", "Volodymyr", "Olha", "Elmira", "Margaryta"]
# print(str_list.index("Olha"))  # 2
#
# pop_method = str_list.pop(2)
# print(str_list)  # ['Pavlo', 'Volodymyr', 'Elmira', 'Margaryta']
# print(pop_method)  # Olha

# arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# del arctic_animals[4]
# print(arctic_animals)  # ['penguin', 'elephant', 'polar bear', 'walrus', 'reindeer']
# arctic_animals.remove("elephant")
# print(arctic_animals)  # ['penguin', 'polar bear', 'walrus', 'reindeer']
# arctic_animals.append("arctic fox")
# print(arctic_animals)  # ['penguin', 'polar bear', 'walrus', 'reindeer', 'arctic fox']
# arctic_animals.insert(2, "snow owl")
# print(arctic_animals)  # ['penguin', 'polar bear', 'snow owl', 'walrus', 'reindeer', 'arctic fox']
# arctic_animals.sort()
# print(arctic_animals)  # ['arctic fox', 'penguin', 'polar bear', 'reindeer', 'snow owl', 'walrus']
# print(arctic_animals.index("reindeer"))  # 3
# the_last = arctic_animals.pop()
# print(the_last)  # walrus

# __________Lists vs. Strings__________________________

# ex_1 = [1, 2, 3]
# ex_1[1] = 5
# print(ex_1)  # [1, 5, 3]
#
# ex_2 = "No, you can't."
# ex_3 = "Yes," + ex_2[3:11] + "!"
# print(ex_3)  # Yes, you can!
#
# ex_4 = 3.14
# ex_5 = "coconut"
# ex_6 = ex_4
# ex_7 = ex_5
# print(ex_6)  # 3.14
# print(ex_5)  # coconut

# ex_8 = [1, 2, 3, 4, 5]
# ex_9 = ex_8
# ex_9[2] = 4
# print(ex_8)  # [1, 2, 4, 4, 5] 
# print(ex_9)  # [1, 2, 4, 4, 5]

# _______copy module and deepcopy()_______________________________________

# import copy
# ex_1 = [1, 2, 3, 4, 5]
# ex_2 = copy.deepcopy(ex_1)
# ex_2[2] = 4
# print(ex_1)  # [1, 2, 3, 4, 5]
# print(ex_2)  # [1, 2, 4, 4, 5]

# ex_list = ["bush",
#            "fern",
#            "tree",
#            "moss"]
# print(ex_list)  # ['bush', 'fern', 'tree', 'moss']

#_________\line continuation_______________
# ex_16 = 2 + \
#         4 + \
#         1
# print(ex_16)  # 7

# ex_17 = "The Emp" \
#         "ire Strikes " \
#         "Back"
# print(ex_17)  # The Empire Strikes Back
#
# ex_18 = "hello " + \
#         "world"
# print(ex_18)  # hello world

# ________________dictionaries________________
# consoles = {"nintendo": "wii",
#             "microsoft": "xbox",
#             "sony": "playstation"}
# print(consoles["microsoft"])  # xbox
# val = consoles["microsoft"]  # xbox
# print(val)
# print("The " + consoles["sony"] + " 4 is Sony's newest gaming console.")  # The playstation 4 is Sony's newest gaming console.

# more_hardness = {9: "corundum", 10: "diamond"}
# floats = {1.23: 1000, 3.14159: 10000, 2.718: 100000}
# mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}

# print([2, 4, 6] == [2, 4, 6])  # True
# print([2, 4, 6] == [6, 4, 2])  # False

# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}
# print(first == second)  # True
# print(0 in first)  # True

# family = {"father": "Pavlo",
#            "mother": "Olha",
#            "son": "Pavlyk",
#            "first_daughter": "Margaryta",
#            "second_daughter": "Elmira"}
# print(family["first_daughter"])  # Margaryta
# print("mother" in family)  # True
# print("mother" not in family)  # False

# _______________________dictionary .key(), .values(), .items() and .get()___
# birth_years = {1983: "Olha", 1987: "Pavlo", 2008: "Pavlyk", 2014: "Margo", 2016: "Elya"}
# print(birth_years.keys())  # ([1983, 1987, 2008, 2014, 2016])
# print(birth_years.values())  # (['Olha', 'Pavlo', 'Pavlyk', 'Margo', 'Elya'])
# print(birth_years.items())  # dict_items([(1983, 'Olha'), (1987, 'Pavlo'), (2008, 'Pavlyk'), (2014, 'Margo'), (2016, 'Elya')])
# print("Pavlo" in birth_years.values())  # True
#
# for key, value in birth_years.items():
#     print(key, value)

# if 1987 in birth_years:
#     print(birth_years[1987])
# else:
#     print("1975 is not a key in birth_years.")
#
# print(birth_years.get(1987, "Nothing"))

# birth_years = {1983: "Olha", 1987: "Pavlo", 2008: "Pavlyk", 2014: "Margo", 2016: "Elya"}
# print(birth_years)
# people = birth_years
# people[1983] = "Olga"
# print(birth_years)  # {1983: 'Olga', 1987: 'Pavlo', 2008: 'Pavlyk', 2014: 'Margo', 2016: 'Elya'}

# birth_years = {1983: "Olha",
#                1987: "Pavlo",
#                2008: "Pavlyk",
#                2014: "Margo",
#                2016: "Elya"
#                }
# print(len(birth_years))  # 5

# rock_groups = {"Queen": "Bohemian Rhapsody",
#                "Bee Gees": "Stayin' Alive",
#                "U2": "One",
#                "Michael Jackson": "Billie Jean",
#                "The Beatles": "Hey Jude",
#                "Bob Dylan": "Like A Rolling Stone"
#                }
# print(len(rock_groups))  # 6
#
# for key in rock_groups.keys():
#     print(key)
#
# print(rock_groups.values())
#
# for key, values in rock_groups.items():
#     print(key, values)
#
# print(rock_groups.get("Promise of the Real", "That is not a key."))

# ___________dictionary .fromkeys(), .pop(), and .popitem()_______

# ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
# print(ex_1)  # {'address': '1600 Pennsylvania Avenue NW'}
#
# ex_2 = {"make": "Honda", "model": "civic", "year": 2016}
# popped = ex_2.pop("model")
# print(ex_2)  # {'make': 'Honda', 'year': 2016}
# print(popped)  # civic
#
# ex_3 = {"name": "bob", "age": 38, "occupation": "accountant", "workplace": "H&R block"}
# ex_3.popitem()
# print(ex_3)  # {'name': 'bob', 'age': 38, 'occupation': 'accountant'}

# for key, value in {}.fromkeys("abcdefg", "consonant").items():
#     print(key, value)

# ______________.clear(), .copy(), and .update()_________
# birth_years = {1983: "Olha", 1987: "Pavlo", 2008: "Pavlyk", 2014: "Margo", 2016: "Elya"}
# print(birth_years)
# birth_years.clear()
# print(birth_years)  # {}
#
# birth_years = {1983: "Olha", 1987: "Pavlo", 2008: "Pavlyk", 2014: "Margo", 2016: "Elya"}
# granny = {1964: "Tanya"}
# birth_years.update(granny)
# print(birth_years)  # {1983: 'Olha', 1987: 'Pavlo', 2008: 'Pavlyk', 2014: 'Margo', 2016: 'Elya', 1964: 'Tanya'}
# birth_years["Tanya"] = "16.03.1963"
# print(birth_years)

# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# internet_celebrities.update(another_one)
# copy = internet_celebrities.copy()
# internet_celebrities.clear()
# print(internet_celebrities)
# print(copy)

# _________.setdefault()____________

# computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}
# computers.setdefault("Lenovo", "ThinkPad")
# print(computers)  # {'Google': 'ChromeBook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad'}

# if "Lenovo" not in computers:
#     computers["Lenovo"] = "ThinkPad"
# print(computers)  # {'Google': 'ChromeBook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad'}

# ___________________dict()_____________
# empty = dict()
# print(empty)  # {}
# with_values = dict(a=1, b_=2, c_3=3)
# print(with_values)  # {'a': 1, 'b_': 2, 'c_3': 3}

# ________________ tuples _________________________

# tuple_1 = ("a", "b", "c", "d", "e")
# tuple_2 = (2.718, False, [1, 2, 3])
# tuple_3 = (1, 1, 0, 0, 0)
# tuple_4 = (5, 4, 3, 2, 1)
# tuple_5 = tuple([3.14, 2.205, 10])
# tuple_6 = tuple("edcba")
# print(tuple_5)  # (3.14, 2.205, 10)
# print(tuple_6)  # ('e', 'd', 'c', 'b', 'a')
# tuple_7 = tuple({"a": 1, "b": 2, "c": 3})
# print(tuple_7)  # ('a', 'b', 'c') only key
# tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(tuple_8[2])  # 3
# print(tuple_8[:8])  # (1, 2, 3, 4, 5, 6, 7, 8)
# print(tuple_8[2:7])  # (3, 4, 5, 6, 7)
# print(tuple_8[3:])  # (4, 5, 6, 7, 8, 9, 10)
# tuple_9 = (1, 3, 5)
# list_1 = [1, 3, 5]
# print(tuple_9.__sizeof__())  # 48 (bytes)
# print(list_1.__sizeof__())  # 72 (bytes)

# occupation = {("Angus", "Young"): "musician",
#               ("Narendra", "Modi"): "prime minister",
#               ("Richard", "Branson"): "enterpreneur",
#               ("Quentin", "Tarantino"): "filmaker"            
#             }
# print(occupation)  # {('Angus', 'Young'): 'musician', ('Narendra', 'Modi'): 'prime minister', ('Richard', 'Branson'): 'enterpreneur', ('Quentin', 'Tarantino'): 'filmaker'}

#____________tuple looping and step___________________


# major_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

# for city in major_cities:
#     print(city)
#
# count = 0
# while count < len(major_cities):
#     print(major_cities[count])
#     count += 1

# backwards = len(major_cities) - 1
# while backwards >= 0:
#     print(major_cities[backwards])
#     backwards -= 1


# ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(ints[::3])  # (1, 4, 7, 10)
# print(ints[1::2])  # (2, 4, 6, 8, 10)
# print(ints[7::-1])  # (8, 7, 6, 5, 4, 3, 2, 1)
# print(ints[8::-2])  # (9, 7, 5, 3, 1)

# _____________tuple methods __________________
# nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
# print(nested[4])  # (7, 8, 9)
# print(nested[5][1])  # 11

# _______.count()_____________
# repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
# print(repeat.count(7))  # 2
# print(repeat.count(3))  # 3
# print(repeat.count(0))  # 4

# ____________.index()____________
# ints = (1, 1, 7)
# print(ints.index(7))  # 2
# print(ints.index(1))  # 0

# _______________sets_________________
# set_1 = {9, 8, 7, 6}
# set_2 = set({"a", "b", "c", "d", "e"})
# print(set_1)  # {8, 9, 6, 7}
# print(set_2)  # {'b', 'e', 'a', 'd', 'c'}
#
# set_3 =set(range(1, 12, 2))
# print(set_3)  # {1, 3, 5, 7, 9, 11}
# set_4 = {"a", 3.14, 18, True}
# print(set_4)  # {True, 18, 3.14, 'a'}
# set_5 = {3, 6, 9, 12, 15}
#
# for num in set_5:
#     print(num)
#
# print(12 in set_5)  # True

# ______set methods______
# .add()
# scifi = {"star trek", "star wars", "halo"}
# scifi.add("mass effect")
# print(scifi)  # {'star wars', 'star trek', 'mass effect', 'halo'}

# .remove()
# scifi = {"star trek", "star wars", "halo"}
# scifi.remove("star wars")
# print(scifi)  # {'halo', 'star trek'}
# scifi.remove("cosmos")
# print(scifi)  # keyError

# .discard()
# scifi = {"star trek", "star wars", "halo"}
# scifi.discard("cosmos")
# print(scifi)  # {'star trek', 'star wars', 'halo'}

# .clear()
# scifi = {"star trek", "star wars", "halo"}
# print(scifi)
# scifi.clear()
# print(scifi)  # set()

# .copy()
# scifi = {"star trek", "star wars", "halo"}
# set_2 = scifi.copy()
# print(set_2 is scifi)  # False
# print(set_2)  # {'star trek', 'star wars', 'halo'}

# .union()
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {6, 7, 8, 9, 10}
# set_3 = set_1.union(set_2)
# print(set_3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set_4 = set_1 | set_2
# print(set_4)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# .intersection()
# set_1 = {4, 5, 6, 7, 8}
# set_2 = {6, 7, 8, 9, 10}
# set_3 = set_1.intersection(set_2)
# print(set_3)  # {8, 6, 7}
# set_4 = set_1 & set_2
# print(set_4)  # {8, 6, 7}

# subtraction and .difference()
# set_1 = {4, 5, 6, 7, 8}
# set_2 = {6, 7, 8, 9, 10}
# set_3 = set_2 - set_1  # as like set_1.difference(set_2)
# set_4 = set_1 - set_2  # as like set_2.difference(set_1)
# print(set_3)  # {9, 10}
# print(set_4)  # {4, 5}

# set copmprehensions
# comp_1 = {even+2 for even in range(2, 11, 2)}
# print(comp_1)  # {4, 6, 8, 10, 12}

# comp_2 = {char.lower() for char in "ALLCAPS"}
# print(comp_2)  # {'a', 'p', 'c', 's', 'l'}
