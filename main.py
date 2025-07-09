import string

password=input("enter password")
length = len(password)

upper_case = any([1 if c in string.ascii_uppercase else 0  for  c in password])
loswer_case = any([1 if c in string.ascii_lowercase else 0  for c in password])
digits = any([1 if c in string.digits else 0  for  c in password])
speacialCHAR = any([1 if c in string.punctuation else 0  for  c in password])

score = 0 

charecters =[upper_case,digits,speacialCHAR,loswer_case]

with open('10-million-password-list-top-1000000.txt' ) as f:
    common = f.read().splitlines()
    
if password in common:
    print("password was found in a common list USE A BETTER PASSOWRD -_-")
    exit()
    
if length > 8 :
    score += 1
if length > 12:
    score+=1

if length > 16:
    score+=1
    
if length > 20:
    score+=1

if sum(charecters) >1:
    score +=1
    
if sum(charecters) >2:
    score +=1
    
if sum(charecters) >3:
    score +=1
    
print(f"password has {str(sum(charecters))} diff charecter types, adding {str(sum(charecters)-1)} points!")

if score < 4 :
    print("pass is weak")
elif score == 4:
    print(f"PASS IS ok, score: {str(score)}/7 ")
    
if score > 4 and score < 6 :
    print(f"pass is decent , score: {str(score)}/7")
    
if score > 6 :
    print(f"pass is decent , score: {str(score)}/7")
