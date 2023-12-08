import os

def In_Outro():    
    print("\n\nCS112: COMPUTER PROGRAMMING 1 - PRE FINAL EXAM")
    print("CREATED BY: ROGER E. BAO JR.\n")
In_Outro()    
print("PROBLEM: Create a python program that display all prime number within a range\n")
print("RULES TO CONSIDER:")
print("[1] If number[start] is a negative number, The program will promt a message: Enter a non-negative number.")
print("[2] If number[end] is less than number[start]. The program will promt a message: Enter a Greater number than number[start].")
print("[3] If the user enter the number 0, the program will terminate.\n\n\n")

            
while True:
    input("Press Enter to Continue . . .")
    os.system('cls')
    
    start = input("Enter a Number [start]\n=")    
    
    if int(start) < 0:
        print("Enter a non-negative number.")
        continue

    if int(start) == 0:
            print("Enter zero again to Exit")
            
        
    end = input("Enter a Number [end]\n=")

    if int(end) < 0:
        print("Enter a non-negative number.")
        continue

    if int(end) < int(start):
        print(f"Enter a number greather than {start}.")
        continue
    
    if int(start or end) == 0:
            In_Outro() 
            exit()
            

    print(f"\n############################\n\nPrime numbers between {start} and {end} are:")        
    for num in range(int(start), int(end) + 1):
        if num > 1:
            primeCheck = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    primeCheck = False
                    break
            if primeCheck:
                print(num)