# class node:
#     def __init__(self,data,nextNode):
#         self.data = data
#         self.nextNode = nextNode
        
# linkedList = [
#     node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2),
#     node(-1,6), node(-1,7), node(56,3), node(-1,9), node(-1,-1)
# ]
# startPointer = 0
# emptyList = 5


# def outputNodes(linkedList, startPointer):
#     while startPointer != -1:
#         print(f"{linkedList[startPointer].data}" )
#         startPointer = linkedList[startPointer].nextNode
        
# outputNodes(linkedList,startPointer)

# def addNode(linkedList,startPointer,emptyList):
#     dataToAdd = int(input("Enter a your data to add to the list :"))
#     newNode = node(dataToAdd,-1)
#     linkedList[emptyList]=newNode
    
#     lastNodeIndex = 0   # 3
#     while startPointer != -1: # startPointer = 
#         lastNodeIndex = startPointer    
#         startPointer = linkedList[startPointer].nextNode   # -1
    
#     linkedList[lastNodeIndex].nextNode=emptyList
    
# addNode(linkedList,startPointer,emptyList)    



# def addNode(linkedList, currentPointer, emptyList):
#     dataToAdd = int(input("Enter the data to add: "))
#     if emptyList < 0 or emptyList > 9:
#         return False


#     newNode = node(dataToAdd, -1)
#     linkedList[emptyList] = newNode

#     previousPointer = 0
#     while currentPointer != -1:
#         previousPointer = currentPointer
#         currentPointer = linkedList[currentPointer].nextNode

#     linkedList[previousPointer].nextNode = emptyList
#     # Update emptyList (not global, to keep function pure)
#     return True

        
        
# outputNodes(linkedList, sp)        
# addNode(linkedList, sp, emptyList)        
# outputNodes(linkedList, sp)        


# class insane:
#     def __init__(self,name,friend):
#         self.name= name
#         self.friend = friend
        
# hamza = insane("hamza","sufyan")
# sufyan = insane("sufyan","waqas")
# waqas = insane("waqas","zaryab")

# friendList = [hamza,sufyan,waqas ]
# print(friendList[0].name)

# for i in range(len(friendList)):
#     print(f"[ {friendList[i].name} | {friendList[i].friend} ]  " , end=" -> ")

        
# def linearSearch(arrayData,searchValue):
#     for i in range(len(arrayData)):
#         if arrayData[i] == searchValue:
#             return True
    
#     return False          

# arrayData = [10,5,6,1,12,13,15,21,8]
# searchValue = int(input("Enter a value to search in list"))

# result=linearSearch(arrayData,searchValue)

# if result:
#     print("It was  found")
# else:
#     print("It was not found") 



# arrayData = [10,5,6,1,12,13,15,21,8] 
# # print(arrayData)
# def bubleSort(arrayData):
#     for i in range(len(arrayData)):
#         for j in range(len(arrayData)-1):
#             if arrayData[j] > arrayData[j + 1 ]:
#                 arrayData[j],arrayData[j + 1] = arrayData[j + 1 ], arrayData[j]
                  
# # bubleSort(arrayData)
# # print(arrayData)


# class TreasureChest:
#     def __init__(self, question, answer, points):
#         # private attributes
#         self.__question = question
#         self.__answer = answer
#         self.__points = points
        
#     def GetQuestin(self):
#         return self.__question    
        
# def readData(): 
#     try:
#       fileData = open("TreasureChestData.txt" )
#       line  = fileData.read()
#       print(line)


      
#     except:
#       print('An exception occurred')       
     


# def division(a,b):
#   try:
#     result = a /b
#     return result

#   except ZeroDivisionError:
#     print("you can't divide a number by zero ")

# print(division(10,0))


# user_name = input("what is your name : ")
# print(user_name)

class TreasureChest:
    def __init__(self, question, answer, points):
        # private attributes
        self.__question = question
        self.__answer = answer 
        self.__points = points

    # --- getQuestion() method ---
    def getQuestion(self):
        return self.__question

    # --- checkAnswer(userAnswer) method ---
    def checkAnswer(self):
        return self.__answer
    

q1 = TreasureChest("2 * 2" , 4 ,10)    
q2 = TreasureChest("5 + 7", 12 ,10)    
q3 = TreasureChest("10 - 3" , 7 ,10)    
q4 = TreasureChest("3 * 5" , 15 ,10)    
q5 = TreasureChest("9 + 6" , 15 ,10) 

arr = [ q1 , q2 , q3 , q4 , q5]  

user_choice = int(input("Enter a number (1 to 5 ) : "))

print(arr[user_choice - 1].getQuestion())
user_anwer= int(input("Enter your answer for the given question "))

attempts = 0
while True:
    attempts += 1
    if user_anwer == arr[user_choice - 1].checkAnswer():
        print("your answer is correct")
        break
    else:
        print("your answer is not correct")
        user_anwer= int(input("Enter your answer for the given question "))
print(attempts)