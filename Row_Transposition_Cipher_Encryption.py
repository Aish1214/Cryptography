#Author :Aishwarya Funaguskar 

import math


def row(s,key):
    
    # to remove repeated alphabets in key
    temp=[]
    for i in key:
        if i not in temp:
            temp.append(i)
    k=""
    for i in temp:
        k+=i
    print("The key used for encryption is: ",k)
    b=math.ceil(len(s)/len(k))
    print(b)
    alphList = ['a','b','c','d','e','f','g','h','i','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    arr=[['_' for i in range(len(k))]
         for j in range(b)]
    i=0
    j=0
    # arranging the message into matrix
    for h in range(len(s)):
        arr[i][j]=s[h]
        j+=1
        if(j>len(k)-1):
            j=0
            i+=1
    for i in range(b):
        for j in range(len(key)):
            if arr[i][j] == '_':
                arr[i][j] = alphList[-1]
                alphList.pop()

    print("The message matrix is: ")
    for i in arr:
        print(i)

    cipher_text=""
    # To get indices as the key numbers instead of alphabets in the key, according
    # to algorithm, for appending the elementsof matrix formed earlier, column wise.
    kk=sorted(k)
    
    for i in kk:
        # gives the column index
        h=k.index(i)
        for j in range(len(arr)):
            cipher_text+=arr[j][h]
    print("The cipher text is: ",cipher_text)
        
msg=input("Enter the message: ")
key=input("Enter the key in alphabets: ")
row(msg,key)