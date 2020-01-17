#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
import math
import os
import sys


#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
[pow(i,2) for i in range(0,20)]


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
power_of_two = [pow(i,2) for i in range(0,50)]
print(power_of_two)



#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
[math.sqrt(i) for i in range(0,100)]



#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
# Remember to use list comprehensions and to print your results
my_list = [n for n in range(-10,1)]
print(my_list)



#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
[n for n in range(1,100) if n % 2 != 0]


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
divisible_by_seven = [n for n in range(1,1000) if n%7 == 0]
print(divisible_by_seven)



#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
vowels = ['a','e','i','o','u']
result = ''.join([n for n in teststring if n not in vowels])

teststring2 = 'Find all of the words in a string that are monosyllabic'
result2 = ''.join([i for i in teststring2 if i not in ['a','e','i','o','u']])

print(result)
print(result2)


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
string = 'The Quick Brown Fox Jumped Over The Lazy Dog'
[n for n in string if n.isupper()]



#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
string = 'The Quick Brown Fox Jumped Over The Lazy Dog'
[n for n in string if n not in ['a','e','i','o','u'] ]



#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.



#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
random_lists = [[random.randrange(0,100) for n in range(10)] for n in range(4)]
print(random_lists)



#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

flatten_list = [i for n in list_of_lists for i in n]
print(flatten_list)


#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [float(i) for n in list_of_lists for i in n]
print(floats)


#14. Handle the exception thrown by the code below by using try and except blocks. 


for i in ['a','b','c']:
    try:
        print (i**2)
    except Exception as e:
        print(e)


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("All done")



#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]

try:
    print(abc[3])
except Exception as e:
    print(e)


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 
x = 3
y = 'f'

try:
    print(x/y)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("Numero invalido")



#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print("No se encuentra el archivo")



#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('../myfile.txt')
    line = fp.readline()
    i = int(i.strip())
except FileNotFoundError:
    print("No se encuentra el archivo")
except NameError:
    print("Error en el nombre del archivo")
except ValueError:
    print("No se puede convertir un string a un int")



#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    try:
        assert ('linux' in sys.platform) 
    except Exception as e:
        print("Function can only run on Linux systems.")
    finally:
        print('Doing something.')


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.
def square():
    
    while(True):
        try:
            numero = int(input("Escriba un número: "))
            print(int(numero)**2)
            break
        except Exception as e:
            print(e)
square()



# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 


{num : j for num in range(1,200) for j in range(2,9) if num % j == 0}


# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

def pidenumero():
    try:
        Total_Marks = int(input("Enter Total Marks Scored: ")) 
        Num_of_Sections = int(input("Enter Num of Sections: "))
        if Num_of_Sections < 2 :
            print('Num of sections no puede ser menor de 2')
        elif(Num_of_Sections > 2):
            print(Total_Marks,Num_of_Sections)
        else:
            raise MiError
    except MiError:
        print('Error al introducir numero')
    except:
        print('Hubo un error inesperado.')
pidenumero()
