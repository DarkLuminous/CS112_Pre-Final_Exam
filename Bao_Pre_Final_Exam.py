def In_Outro():    
    print("CS112: COMPUTER PROGRAMMING 1 - PRE FINAL EXAM")
    print("CREATED BY: ROGER E. BAO JR.\n")
In_Outro()    
print("PROBLEM: Create a python program that display all prime number within a range\n")
print("RULES TO CONSIDER:")
print("[1] If number[start] is a negative number, The program will promt a message: Enter a non-negative number.")
print("[2] If number[end] is less than number[start]. The program will promt a message: Enter a Greater number than number[start].")
print("[3] If the user enter the number 0, the program will terminate.\n\n\n")


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
            
while True:
    start = int(input("Enter a Number [start]"))

    if (start) == 0:
            print("Enter zero again to Exit")
        
    end = int(input("Enter a Number [end]"))

    if start < 0:
        print("Enter a non-negative number.")
    
    elif end < start:
        print("Enter a greather than number.")
    
    elif (start or end) == 0:
            In_Outro() 
            exit()
    else:
        display_primes(start, end)