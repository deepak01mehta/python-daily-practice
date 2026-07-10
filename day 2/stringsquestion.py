char = input("enter the String")
counter =0
for i in char:
    counter +=1
print(counter)


gmail = input("Enter you email")

pos =gmail.index("@")
print(gmail[0:pos])


# count the frequeny of a particular character in a provide string 

char = input("Enter the number")

term = input("What wouid you like to serch for ")

counter =0
for i in char:
    if i== term:
        counter +=1


print("frequny ",counter)

# write the programe wgich can remove a particular charter from a string 

char = input("Enter the string")

term = input("What wouid you like to rmove ")

result =""

for i in char:
    if i != term:
        result =result + i
print(result)


# write the proggrme check the palinfrome or not 

word = input("check the palindrom or not ")
start =0
end = len(word)-1
for i in range(start,end-1):

    if word[start] != word[end]:
        print("not a paildrome") 
        break
    
    start+=1
    end -=1
else:
    print("this is plainfrome")

    
