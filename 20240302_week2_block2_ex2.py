my_list1 = [1,2,3,4]
[print(val) for val in my_list1]
[print(val*20) for val in my_list1]
my_list2 = ["Elie", "Tim", "Matt"]
my_list21 = [val[0] for val in my_list2]
print(my_list21)
my_list3 = [1,2,3,4,5,6]
my_list31 = [val for val in 
                my_list3 if val%2==0]
print (my_list31)
my_list41 = [1,2,3,4]
my_list42 = [3,4,5,6]
intersection = [val for val in 
        my_list41 if val in my_list42]
print (intersection)
my_list22 = [word[::-1].lower() 
            for word in my_list2]
print (my_list22)
str51 =  "first"
str52 = 'third'
intersection2 = [letter for letter 
     in str51 if letter in str52]
print(intersection2)
#task 8
list6 = [num for num in range(1,101)
     if num%12==0]
print(list6)
#task 9
string9 = "amazing"
vowels = "AEIOUaeiou"
string9_vowels_removed = [letter for letter in string9 
     if letter not in vowels]
print(string9_vowels_removed)
#task 10
list10 = [[num for num in 
 range(3)] for i in range(3)]
print (list10)
#task 11
list11 = [[num for num in range(10)] 
   for i in range(10)]
print(list11)