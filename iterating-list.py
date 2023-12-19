emails =['jasol@hotmail.com','da@simplegreet.com','de3145u@att.com','anika4563@gmail.com','otto.martin@superblueg.com','jessica353gd@gmail.com','wang.chung@facebrook.com','oattt32@yahoo.com']


for email_list in emails:
    print("***********Sending emails to addresses ****************")
    print(email_list)
print("***********THAT WAS USING 'FOR' LOOP ****************")    
print("***********\n")
print("***********\n")

i = 0
while i < len(emails):
    print("***********Sending emails to addresses ****************")
    print(emails[i])
    i += 1

    f1race_lando2021_results =[4,3,5,8,3,5,5,5,3,4,14,10,2,7,7,8,10,10,9,10,7]

race_rank_total= 0
for r in f1race_lando2021_results:
    race_rank_total += r
race_ave = race_rank_total/len(f1race_lando2021_results)
print ("His Average Ranking is : " ,race_ave)

