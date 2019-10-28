
### Grading Program ###

print("----- Grading Program -----\n")

grade = int(input("Enter the grade scored in programming class (0-100): "))

if grade > -1 and grade < 101:
    if grade == 100:
        print("You got a perfect score! ") 

    elif grade > 90 and grade < 101:  #*
        print("You scored an A.")
        
    elif grade > 79 and grade < 90:  #**
        print("You scored a B.")
        
    elif grade > 69 and grade < 80:  #**
        print("You scored a C.")
        
    elif grade > 59 and grade < 70:  #**
        print("You scored a D.")
        
    elif grade > -1 and grade < 60:  #**
        print("You scored an F.")
else:
    print("I think you need ENGLISH classes to read the question properly!\a")  #***
    
    
### Cola Machine ###

print("\n----- Cola Machine -----\n")

print("Choose your favorite drink:\n1 - Water\n2 - Coke\n3 - Orange\n4 - Sprite\n5 - Root Beer")
# print("1 - Water, 2 - Coke, 3 - Orange, 4 - Sprite, 5 - Root Beer")
# print("1 - Water\n2 - Coke\n3 - Orange\n4 - Sprite\n5 - Root Beer")
choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    print("You chose Water.")
    
elif choice == 2:
    print("You chose Coke.")
    
elif choice == 3:
    print("You chose Orange.")

elif choice == 4:
    print("You chose Sprite.")
    
elif choice == 5:
    print("You chose Root Beer.")
    
else:
    print("Error. choice was not valid, here is your money back.\a")  #**
    

### While( user == gullible ) ###

print("\n----- While( user == gullible ) -----\n")

 # Write a program that ccontinues to asks the user to enter any number other than 5 until the user enters the number 5.
 # Then tell the user "Hey! you weren't supposed to enter 5!" and exit the program.
"""
number = 0

while number != 5:
   number = int(input("Enter any number OTHER than 5: "))
print("Hey! you weren't supposed to enter 5!")  #else: ??
exit()
"""

 #★ Modify the program so that after 10 iterations if the user still hasn't entered 5 will tell the user "Wow, you're more patient then I am, you win." and exit.
""" 
for count in range(10):
    number = int(input("Enter any number OTHER than 5: "))
    
    if number == 5:
        print("Hey! you weren't supposed to enter 5!")
        exit()
   
print("Wow, you're more patient then I am, you win.")  #else: ??
exit()
"""

 #★★ Modify the program so that it asks the user to enter any number other than the number equal to the number of times they've been asked to enter a number. (i.e on the first iteration "Please enter any number other than 0" and on the second iteration "Please enter any number other than 1"m etc. etc. The program must behave accordingly exiting when the user enters the number they were asked not to.)
 
count = 0
userInput = int(input('Please enter any number OTHER than ' + str(count) + '\n'))

while userInput != count:
    userInput = int(input('Please enter any number OTHER than ' + str(count + 1) + '\n'))
    count += 1
print('I asked you NOT to enter the number', count,'...Bye!\a')  #else: ??
#raise ValueError('I asked you NOT to enter the number', count,'...Bye!\a')
exit()

"""With Boolean and break:
count = 0
while True:
    userInput = int(input('Please enter any number OTHER than ' + str(count) + '\n'))
    if count == userInput:
        break
    count += 1
print('I asked you NOT to enter number', count,'...Bye!\a')  #else: ??
exit()
"""