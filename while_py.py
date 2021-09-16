#!/usr/bin/python3

# 1, 3, 5, 9
# 2, 4, 6, 8

counter = 1

FIFTEEN = 15
print ('\nDigit prog v0.01\n')

#num = int(input("Enter number: "))
num2 = int(input("Set var: "))
print ("\n")


line = ("15 - " + str(num2) + " =\t")
print (line)

num2 = num2 + 1

while (counter <= FIFTEEN):
    print ('The count is:', counter)
    counter = counter + 1
    
    if (counter == num2):
        break
        print ('skip counting')

print ('\n\tremaining: >', FIFTEEN - num2 + 1)

print ("\nEnd Program\n")
