#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"


print ("printing the word using FOR loop ..................")
# Write a for loop that prints out each character in the above "word" variable
for x in word:
    print(x)
    
print ("printing the word using WHILE loop ................")    
# Write a while loop that does the same thing!
y = len(word)
z = 0
while y > 0:
    print (word[z])
    y -= 1
    z += 1

#  ----------
#    PART 2
#  ----------

print ("printing the word using WHILE loop prints even numbers of letters from 100 to 140 including 140........")   
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
n = 100
while n <= 140:
    print(n)
    n += 2


# Write a for loop that does the same thing (with range())
print ("printing the word using WHILE loop prints even numbers of letters from 100 to 140 including 140...this time with RANGE.")   

for n1 in range (100,142,2):
    print(n1)
 


#  ----------
#    PART 3
#  ----------
print ("printing a loop to keep on asking people to enter exactly'sillygoos' ... or looping ") 
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:


wordy = input("Please enter exactly the word 'sillygoose' ....... : ")

while wordy != "sillygoose":
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    wordy = input("Please enter EXACTLY the word 'sillygoose' ....... : ")
    
    
print("You HAVE ENTERED exactly the word 'sillygoose' ....... : ")

