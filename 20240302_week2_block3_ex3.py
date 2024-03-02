#task 1
print ("----task1----")
list1 = [("name", "Elie"), ("job", "Instructor")]
d1 = {k:v for k,v in list1}
print(d1)
#task 2
print ("----task2----")
list21 = ["CA", "NJ", "RI"]
list22 = ["California", "New Jersey", "Rhode Island"]
for item in zip(list21,list22):
    print (item)
d2 = dict(zip(list21,list22))
print(d2)
#task 3
print ("----task3----")
vowels = "aeiou"
dict3 = {vowel:0 for vowel in vowels}
print(dict3)
#task 4
print ("----task4----")
dict4 = {(i-64):chr(i) for i in range(65,91)}
print(dict4)
#task 5
print ("----task5----")
given_string = 'awesome sauce'
dic5 = {k:given_string.count(k) for k in vowels}
print(dic5)
