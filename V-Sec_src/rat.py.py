import mysql.connector as ms
import random
def get_key(a):
    key={1:"2718",2:"32@#182371*",3:"3748.915",4:"19822171",5:"A2AB1",6:"%12@9",7:"%052",8:"32@#182371",9:"32#"}
    if a==1:
        return(key[a])
    elif a==2:
        return(key[a])
    elif a==3:
        return(key[a])
    elif a==4:
        return(key[a])
    elif a==5:
        return(key[a])
    elif a==6:
        return(key[a])
    elif a==7:
        return(key[a])
    elif a==8:
        return(key[a])
    elif a==9:
        return(key[a])
    else:
        return(key[2])
def encrypt(password,key):
    new_pass=""
    length_key=len(key)
    count=0
    for i in password:
        if count>=length_key:
            count=0
        ch = chr(ord(i) + ord(key[count]) % 256)
        new_pass+=ch
        count+=1
    return(new_pass)
def decrypt(encoded,key):
    decoded_pass=""
    length_key=len(key)
    count=0
    for i in encoded:
        if count>=length_key:
            count=0
        ch = chr(ord(i) - ord(key[count]) % 256)
        decoded_pass+=ch
        count+=1
    return(decoded_pass)
def generate_random_key():
    new_k=""
    for i in range(0,5):
        a=random.randint(1,9)
        new_k+=str(a)
    return(new_k)
def multiple_encrypt(password,key):
    encode_password=password
    for i in key:
        current_key=get_key(int(i))
        encode_password=encrypt(encode_password,current_key)
    return(encode_password)
def multiple_decrypt(encoded,key):
    decoded_password=encoded
    for i in key:
        current_key=get_key(int(i))
        decoded_password=decrypt(decoded_password,current_key)
    return(decoded_password)


conn=ms.connect(host="vsec-db.cvuikus8i27i.us-east-1.rds.amazonaws.com",user='coderboys',passwd='hello123',database="vsec1")
cur=conn.cursor()
title="testing1"
usr_input=str(input("Enter your password :")) #Change to the password from user
main_key=generate_random_key()
cur.execute("INSERT INTO Key_Data VALUES((%s,%s))",(title,main_key)) #Upload to server
coded_password=multiple_encrypt(usr_input,main_key) #Upload this to the server
cur.execute("INSERT INTO Data VALUES((%s,%s))",(title,coded_password))
print(coded_password)
cur.execute("SELECT Encrypted_Code FROM Data WHERE Title=title")
result=cur.fetchall()
for row in result:
    pw_coded=row[0]
cur.execute("SELECT Key_Set FROM Key_Data WHERE Title=title")
result=cur.fetchall()
for row in result:
    key_coded=row[0]
print(multiple_decrypt(pw_coded,key_coded)) #Decrypt the password

