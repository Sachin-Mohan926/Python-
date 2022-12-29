print()
print("               =============================================================================")
print("               |                       FIBONACCI NUMBER VERIFIER!                          |")
print("               |   In mathematics, the Fibonacci numbers, commonly denoted Fn, form a      |")
print("               |   sequence, the Fibonacci sequence, in which each number is the sum       |")
print("               |   of the two preceding ones. The sequence commonly starts from 0 and 1,   |")
print("               |   although some authors start the sequence from 1 and 1 or sometimes      |")
print("               |   (as did Fibonacci) from 1 and 2.                                        |")
print("               |   The Fibonacci numbers may be defined by the recurrence relation.        |")
print("               |   It so happens that 0 and 1 are the first two members of this series,    |")
print("               |   when 0 and 1 are added it gives 1, and 1 is now added to the sequence   |")
print("               |                                0,1                                        |")
print("               |                                0+1=1                                      |")
print("               |                                0,1,1                                      |")
print("               |                                1+1=2                                      |")
print("               |                                0,1,1,2                                    |")
print("               |                                1+2=3                                      |")
print("               |                                2+3=5                                      |")
print("               |                                0,1,1,2,3,5.......                         |")
print("               |                                                                           |")
print("               |   Now that you have learnt about Fibonacci Series!!                       |")
print("               |   We provide you with a very simple tool to check whether a number        |")
print("               |   belongs to fibonacci series or not.                                     |")
print("               =============================================================================")
print()
while True:
    x=int(input("Press 1 to check or 2 to exit: \n"))
    if x==1:
        n=int(input("How many numbers you want to check: \n"))
        for i in range(n):
            l1=[0,1]
            j=int(input("Enter the number you wish to verify: \n"))

           # Add new fibonacci terms until the user_input is reached
            while l1[-1] <= j:
                l1.append(l1[-1] + l1[-2])
            if j in l1:
                print(f'Yes. {j} is a fibonacci number.')
            else:
                print(f'No. {j} is NOT a fibonacci number.')
    elif x==2:
        print("Thankyou for using FIBONACCI NUMBER VERIFIER,\nHave a nice day!!")
        break
    else:
        print("invalid input")
















