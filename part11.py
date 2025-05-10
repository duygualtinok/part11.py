"""numbers=list(range(1,10))
print(numbers)
yeni_number=[number*10 for number in numbers]
print(yeni_number)"""
#----------------------------

"""import math
def square_roots(numbers:list):
    return [ math.sqrt(number) for number in numbers]
dize=square_roots([1,2,3,4,9])
for i in dize:
    print(i)"""
#----------------------------

"""def  rows_of_starts(numbers:list):
    return  ["*"*number for number in numbers ]
rows=rows_of_starts([1,2,3,4,5])
for i in rows:
    print(i)
print()
rows=rows_of_starts([5,4,3,2,1])
for y in rows:
    print(y)"""

#---------------------------------

"""class ExamResult:
    def __init__(self,ad:str,sınıf1:int,sınıf2:int,sınıf3:int):
        self.ad=ad
        self.sınıf1=sınıf1
        self.sınıf2=sınıf2
        self.sınıf3=sınıf3
   
def best_results(results:list):
    return [max([result.sınıf1,result.sınıf2,result.sınıf3]) for result in results]

result1 = ExamResult("Peter",5,3,4)
result2 = ExamResult("Pippa",3,4,1)
result3 = ExamResult("Paul",2,1,3)
results = [result1, result2, result3]
print(best_results(results))"""

#----------------------------------------

"""def lengths(lists: list):
    return [ len(i) for i in lists]
lists = [[1,2,3,4,5], [324, -1, 31, 7],[2,7]]
print(lengths(lists))"""


#-----------------------------------------
"""def remove_smaller_than(numbers: list, limit: int):
    return [number for number in numbers if number>limit ]
numbers = [1,65, 32, -6, 9, 11]
print(remove_smaller_than(numbers, 10))

print(remove_smaller_than([-4, 7, 8, -100], 0))"""
#-------------------------------------------------

"""def begin_with_vowel(words: list):
    return [word for word in words if word[0].lower() in ["a","e","i","o","u"]]

word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)"""

#--------------------------------------------

"""class LotteryNumbers:
    def __init__(self,week:int,numbers:list):
        self.week=week
        self.numbers=numbers

    def number_of_hits(self,numbers: list):
        return len( [number for number in numbers if number in self.numbers])
       
    def hits_in_place(self, numbers: list) -> list:
        return [num if num in self.numbers else -1 for num in numbers]
week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
my_numbers = [1,4,7,11,13,19,24]

print(week5.number_of_hits(my_numbers))"""

#----------------------------------------------------

"""def filter_forbidden(string: str, forbidden: str):
    return [harf for harf in string if harf not in forbidden  ]
sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
for i in filtered :
    print(i,end="")"""


def add_numbers_to_list(numbers: list):
    
        if len(numbers)% 5 !=0:
            no=numbers[-1]+1
            numbers.append(no)
            add_numbers_to_list(numbers)
numbers = [1,3,4,5,10,11]
add_numbers_to_list(numbers)
print(numbers)









