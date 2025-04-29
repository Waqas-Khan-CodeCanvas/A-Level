# def IterativeVowels(Value):
#     Total = 0
#     for X in range(0, len(Value)):
#         FirstCharacter = Value[0]
#         if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
#             Total = Total + 1
#             Value = Value[1:len(Value)] 
#     return Total

# print(IterativeVowels("hello"))

def IterativeVowels(values):
    count = 0
    for vowel in values: # hello
        if vowel in "aeiou":
            count += 1
    return count        
print(IterativeVowels("hello"))


def v(str):
    total = 0 
    if str == "":
        return total
    if str in  "aeiou":
        total+=1
        v(str[1:len(str)])
    else:
        v(str[1:len(str)])

print(v("hello") )       