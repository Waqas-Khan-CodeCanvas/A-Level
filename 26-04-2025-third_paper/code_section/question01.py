# Part (a)
# Global 2D array declaration
Jobs = []  # Empty list initially
for i in range(100):
    Jobs.append([-1, -1])  # Add a list with two elements for each job

NumberOfJobs = 0

# Part (b)
def Initialise():
    global Jobs, NumberOfJobs
    for i in range(100):
        Jobs[i][0] = -1
        Jobs[i][1] = -1
    NumberOfJobs = 0

# Part (c)
def AddJob(jobNumber, priority):
    global Jobs, NumberOfJobs
    if NumberOfJobs < 100:
        Jobs[NumberOfJobs][0] = jobNumber
        Jobs[NumberOfJobs][1] = priority
        NumberOfJobs += 1
        print("Added")
    else:
        print("Not added")
    
    print(Jobs)    

# Part (e)
def InsertionSort():
    global Jobs, NumberOfJobs
    for i in range(1, NumberOfJobs):
        position = i
        while Jobs[position - 1][1] > Jobs[position][1] and position > 0:
            Jobs[position - 1],Jobs[position] = Jobs[position],Jobs[position - 1]
            position -= 1
        

# Part (f)
def PrintArray():
    global Jobs, NumberOfJobs
    for i in range(NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")

# Part (d) and (g)(i)
def main():
    Initialise()

    # Add the given jobs
    AddJob(12, 10)
    AddJob(526, 9)
    AddJob(33, 8)
    AddJob(12, 9)
    AddJob(78, 1)

    # Sort and print
    InsertionSort()
    PrintArray()

# Run the main program
if __name__ == "__main__":
    main()

print(Jobs)
"""
1(a) Declaring

1(b) Initialise()

1(c) AddJob()

1(d) Adding sample jobs

1(e) InsertionSort()

1(f) PrintArray()

1(g)(i) Calling sort and print from main()


"""