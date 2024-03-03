#task1
print("---task1---")
def difference (a:int, b:int):
    '''This function takes in two parameters and returns the difference berween the two'''
    return a-b
print(difference (2,2))
print (difference(0,2))
#task2
print("---task2---")

def print_day(a):
    if (a<1) or (a>7):
        print (None)
        return None
    days = {1:"Sunday", 2:"Monday", 
            3:"Tuesday", 4:"Wensday", 
            5:"Thursday", 6:"Friday",
            7: "Saturday"}
    print(days[a])
    return days[a]
print_day(4)
print_day(41)
#task3
print("---task3---")
def last_element(my_list):
    if len(my_list)==0:
        print (None)
        return None
    else :
        print (my_list[-1])
        return my_list[-1]
last_element([1,2,3,4])
last_element([])
#task4
print("---task4---")
def number_compare(a,b):
    if a>b :
        return "First is greater"
    elif b>a:
        return "Second is greater"
    else:
        return "Numbers are equal"
print (number_compare(1,1))
print (number_compare(1,2))
print (number_compare(2,1))
#task5
print("---task5---")
def single_letter_count(str1, str2):
    return str1.lower().count(str2.lower())
print(single_letter_count('amazing','A'))
#task6
print("---task6---")
def multiple_letter_count(str1):
    str1_keys=[]
    for key in str1:
        if key not in str1_keys:
            str1_keys.append(key)
    return {key:str1.lower().count(key.lower())
            for key in str1_keys}
print (multiple_letter_count("hello"))
print (multiple_letter_count("person"))
#task7
print("---task7---")
def list_manipulation(ls,comm,*loc):
    if comm == "remove":
        if loc[0] == "end":
            if ls:
                return ls.pop()
            else:
                return None
        elif loc[0] == "beginning":
            if ls:
                return ls.pop(0)
            else:
                return None
    elif comm == "add":
        if loc[0] == "beginning":
            ls.insert(0, loc[1])
            return ls
        elif loc[0] == "end":
            ls.append(loc[1])
            return ls
    else:
        return None
print(list_manipulation([1,2,3], "remove", "end")) 
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20)) 
print(list_manipulation([1,2,3], "add", "end", 30))
#task8
print("---task8---")
def is_palindrome(str1):
    str1=str1.lower().replace(" ", "")
    for i in range(0,len(str1)//2):
        if str1[i] != str1[-i-1]:
            return False
    return True
print(is_palindrome('testing'))
print(is_palindrome('tacocat'))
print(is_palindrome('hannah'))
print(is_palindrome('robert'))
print(is_palindrome('a man a plan a canal Panama'))
#task9
print("---task9---")
def frequency(ls,s_t):
    count=ls.count(s_t)
    print(count)
    return count
frequency([1,2,3,4,4,4], 4)
frequency([True, False, True, True], False)
#task10
print("---task10---")
def flip_case(inp_str, let):
    res = ""
    for char in inp_str:
        if char.lower() == let.lower():
            if char.islower():
                res += char.upper()
            else:
                res += char.lower()
        else:
            res += char
    print (res)
    return res
flip_case("Hardy har har", "h")
#task11
print("---task11---")
def multiply_even_numbers(ls):
    prod=1
    for num in ls:
        if num%2==0:
            prod*=num
        
    print (prod)
    return prod
multiply_even_numbers([2,3,4,5,6])
#task12
print("---task12---")
def mode(ls):
    count_dict = {}
    for num in ls:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    count_max = 0
    value_max = None
    for num, count in count_dict.items():
        if count > count_max:
            count_max = count
            value_max = num
    print(value_max)
    return value_max
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])
#task13
print("---task13---")
def capitalize(str1):
    return str1.capitalize()
print(capitalize("tim"))
print(capitalize("matt"))
#task14
print("---task14---")
def compact(ls):
    return [val for val in ls if val]
print (compact([0,1,2,"",[], False, {}, None, "All done"]))
#task15
print("---task15---")
def partition (ls,c_b):
    t_list = []
    f_list = []
    
    for el in ls:
        if c_b(el):
            t_list.append(el)
        else:
            f_list.append(el)
    return [t_list,f_list]
def is_even(num):
    return num % 2 == 0

print(partition([1,2,3,4], is_even))
#task16
print("---task16---")

def intersection(list_2d):
    return [val for val in list_2d[0] if val in list_2d[1]]
print(intersection([[1,2,3], [2,3,4]]))
#task17
print("---task17---")
def once(func_ext):
    def func_int(*args, **kwargs):
        if not func_int.invoked:
            func_int.invoked = True
            return func_ext(*args, **kwargs)
        else:
            return None
    func_int.invoked=False
    return func_int
    
def add(a,b):
    return a + b
one_addition = once(add)

print(one_addition(2,2))
print(one_addition(2,2))
print(one_addition(12,200))

#superbonus
print("---superbonus---")
@once
def add(a,b):
    return a + b

print(add(2,2))
print(add(2,20))
print(add(12,20))