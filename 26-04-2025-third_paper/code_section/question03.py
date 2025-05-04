# Part (a)
Queue = [0] * 100  # Array to hold up to 100 integers
HeadPointer = 0  # Points to first element
TailPointer = 0  # Points to next free space

# Part (b)
def Enqueue(value):
    global Queue, HeadPointer, TailPointer
    if TailPointer < 100:
        Queue[TailPointer] = value
        TailPointer += 1
        return True
    else:
        return False

# Part (d)
def RecursiveTotal(start):
    global Queue, HeadPointer
    if start <= HeadPointer:
        return 0
    else:
        return Queue[start - 1] + RecursiveTotal(start - 1)

# Part (c) and (e)(i)
def main():
    successful = True

    # Enqueue numbers 1 to 20
    for i in range(1, 21):
        if not Enqueue(i):
            successful = False
            break

    if successful:
        print("Successful")
    else:
        print("Unsuccessful")

    # Call recursive total function
    total = RecursiveTotal(TailPointer)
    print("Total of all values in queue:", total)

# Run main program
if __name__ == "__main__":
    main()


"""
Enqueue() checks if there's space and inserts number.

RecursiveTotal() adds numbers from end to start recursively.

Main program enqueues numbers 1 to 20 and prints success/fail.

Afterward, it calls the recursive function to calculate and show the total sum.
"""