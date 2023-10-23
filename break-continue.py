for char in "pickleDUDEfaceisyou":
    if char == "f":
        break
    print(char)
    
    
print("done looooping .....")    



print("have to say 'hi' or looping.....using while and break loop...")

message = input("please say 'hi':  ")

while True:
        if message =="hi":
            break
        message = input("please REALLY DO say 'hi':  ")
        
print("Good ... you have said 'hi'") 
      
       
print("....using while and continue in the loop...skipping any instance(s) of 'A' ")
    
for x in "FATCATFLYINGPIGWALKINGBIRD":
        if x == "A":
            continue
        print(x)
        
print("we are out of the loop ....")    
print("...........................")    

print("....using while and continue in the loop...skipping any instance(s) of 'aeiou' vows ")

for xy in "supercalifragilisticexpialidocioustdurskipjoinkeyweputiiu":
        if xy == "a" or xy =="e" or xy =="i" or xy =="o" or xy == "u":
            continue
        print(xy)
        
print("we are out of the loop ....")   