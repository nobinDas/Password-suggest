import random

print("Here you will be asked to enter the characters you want in your password. But the numbers are in default 0-9")

num = int(input("How many characters you want in your password?:"))
list1=input('Which lower case alphabets you want to use?:').lower()
list2=input('Which lower case alphabets you want to use?:').upper()
list3=input('Which signs you want to use?:')
list4=[0,1,2,3,4,5,6,7,8,9]
choice = input("do want any specific character to appear at the first place").upper()

a=random.randint(0,len(list1)-1)
b=random.randint(0,len(list2)-1)
c=random.randint(0,len(list3)-1)
d=random.randint(0,9)

tolist = []

if choice == "YES":
    choose = input("Which character you want at the first place: lower_letter, upper_letter, signs or a number?:")
    if choose == "lower_letter":
        ch = (list1[a])
        tolist.append(ch)
    elif choose == "upper_letter":
        ch = (list2[b])
        tolist.append(ch)
    elif choose == "signs":
        ch = (list3[c])
        tolist.append(ch)
    else:
        ch = (d)
        tolist.append(ch)

if choice == "YES":
    t = 1
else:
    t = 0


for x in range(t, num-3):
    a=random.randint(0,len(list1)-1)
    b=random.randint(0,len(list2)-1)
    c=random.randint(0,len(list3)-1)
    c=random.randint(0,9)
    t = random.randint(0,10)
    if t>5:
        ch = (list1[a])
        tolist.append(ch)
    elif t >2:
        ch = (list2[b])
        tolist.append(ch)
    elif t == 2:
        ch = (list3[c])
        tolist.append(ch)
    else:
        ch = (d)
        tolist.append(ch)



for i in range(len(list1)):
    if tolist[0] == list1[i]:
        ch = (list2[b])
        tolist.append(ch)
        ch = (list3[c])
        tolist.append(ch)
        ch = (d)
        tolist.append(ch)
        break

for i in range(len(list2)):
    if tolist[0] == list2[i]:
        ch = (list1[a])
        tolist.append(ch)
        ch = (list3[c])
        tolist.append(ch)
        ch = (d)
        tolist.append(ch)
        break

for i in range(len(list3)):
    if tolist[0] == list3[i]:
        ch = (list1[a])
        tolist.append(ch)
        ch = (list2[b])
        tolist.append(ch)
        ch = (d)
        tolist.append(ch)
        break

for i in range(len(list4)):
    if tolist[0] == list4[i]:
        ch = (list1[a])
        tolist.append(ch)
        ch = (list2[b])
        tolist.append(ch)
        ch = (list3[c])
        tolist.append(ch)
        break


for i in tolist:
    print(i,end = "")
print()
    
    
        
