# Jobs = []

# for i in range(100):
#     Jobs.append([i,""])

# NumberOfJobs = 0
# print(Jobs)  

# def initilize():
#     global Jobs, NumberOfJobs
#     for i in range(100):
#         Jobs[i][0] = -1 
#         Jobs[i][1] = -1 
#     NumberOfJobs = 0 

# initilize()
# print(Jobs)
# def AddJob(jobNubmer,jobPriorty):
#     global Jobs,NumberOfJobs    
#     if NumberOfJobs < 100:
#         Jobs[NumberOfJobs][0]=jobNubmer
#         Jobs[NumberOfJobs][1]=jobPriorty
#         NumberOfJobs +=1
#         print("job added")
#     else:
#         print("job is not added")
        
# AddJob(12, 10)
# AddJob(526, 9)
# AddJob(33, 8)
# AddJob(12, 9)
# AddJob(78, 1)            
# print(Jobs)
            
            
# def insertionSor(arr):
#     for i in range(1,len(arr)):
#         j = i
#         while arr[j-1] > arr[j] and j > 0:
#             arr[j-1], arr[j] = arr[j] , arr[j-1]
#             j -= 1 
        
        
# arr = [5, 2, 4, 6, 1, 3]
# print("before sorting = ",arr)
# insertionSor(arr)        
# print("after sorting = ",arr)


# def insertion_sort_2d(arr):
#     for i in range(1, len(arr)):
#         j = i
#         # Compare the second column (priority)
#         while j > 0 and arr[j-1][1] > arr[j][1]:
#             arr[j-1], arr[j] = arr[j], arr[j-1]  # Swap the rows
#             j -= 1


# jobs = [
#     [12, 10],[526, 9],[33, 8],[78, 1],[12, 9]
# ]

# print("Before Sorting:")
# for job in jobs:
#     print(job)

# insertion_sort_2d(jobs)

# print("\nAfter Sorting by Priority:")
# for job in jobs:
#     print(job)


# Jobs = []  #[[0, ''], [1, ''], [2, ''], [3, ''], [4, ''], [5, '']]
# NumberOfJobs = 0
# for i in range(100):
#     Jobs.append([i,""])

# print(Jobs)

# def initialize():
#     global Jobs ,NumberOfJobs
#     for i in range(100):
#         Jobs[i][0] = -1
#         Jobs[i][1] = -1
#     NumberOfJobs = 0  
      
# initialize()    
# print(Jobs)

# def AddJob(jobNumber,priority):
#     global Jobs, NumberOfJobs
#     if NumberOfJobs < 100:
#         Jobs[NumberOfJobs][0] =jobNumber 
#         Jobs[NumberOfJobs][1] =priority 
#         NumberOfJobs += 1
#         print("job are added ")
#     else:
#         print("job not added ")    

# AddJob(12, 10)
# AddJob(526, 9)
# AddJob(33, 8)
# AddJob(12, 9)
# AddJob(78, 1)        

# print(Jobs)    

# def insertionSort(arr):
#     for i in range(1,len(arr)):
#         j = i 
#         while arr[j-1][1] > arr[j][1] and j > 0 :
#             arr[j -1 ], arr[j] = arr[j] , arr[j-1]
#             j -= 1
            
# arr = [[10,1],[10,3],[10,5],[10,2],[10,4]]
# print(arr)
# insertionSort(arr)
# print(arr)

class Character:
    def __init__(self, name , x ,y):
        self.__name = name
        self.__XCoordinate = x
        self.__YCoordinate = y
    
    def GetName(self):
        return self.__name 
       
    def GetX(self):
        return self.__XCoordinate 
       
    def GetY(self):
        return self.__YCoordinate  
    
    def ChangePosition(self,Xchange , Ychange):
        self.__XCoordinate += Xchange
        self.__YCoordinate += Ychange

def main():
    characters = []
    try:
      fileData = open("Characters.txt")
      lines = fileData.readline()
      for i in range(0,len(lines),3):
          name = lines[i].strip()
          x = lines[i + 1].strip()
          y = lines[i + 2].strip()
          character = Character(name ,x ,y)
          characters.append(character)
    except:
      print('An exception occurred')
# main()

list = [1,2,3,4,5,6,7]

for i , j in enumerate(list):
    print(i ,j)