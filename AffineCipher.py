import random


def gcd(x,y):               # υπολογισμός μέγιστου κοινού διαιρέτη
    while(y):
        x,y = y,x % y
    return x



def modInverse(a, m) :      # υπολογισμός αντίστροφου αριθμού
    a = a % m
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

def encrypt(plaintext):     # κρυπτογράφηση κειμένου
    letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
               'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
               'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    list=[]
    list2=[]
    list3=[]

    for key in plaintext:
        if key in letters:
            list.append(letters[key])
    for x in list:
        list2.append((key1*x + key2) % 26)
    for num in list2:
        for key, value in letters.items():
            if value == num:
                list3.append(key)


    return list3

def decrypt(encrypted):     # αποκρυπτογράφηση κειμένου
    letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
               'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
               'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    list=[]
    list2=[]
    list3=[]


    for let in encrypted:
        for key, value in letters.items():
            if key == let:
                list.append(value)
    for x in list:
        list2.append((antistrofos * x - (antistrofos * key2) % 26) % 26)
    for letter in list2:
        for key, value in letters.items():
            if value == letter:
                list3.append(key)
    return list3



key1 = random.randint(1,100)
key2 = random.randint(1,100)
print('to kleidi 1 einai:',key1)
print('to kleidi 2 einai:',key2)

print('\nYpologismos MKD(GCD) :',(key1,26), '= ', gcd(key1, 26))
print()
repeat_gcd=0
while gcd !=1 and repeat_gcd !=1:
    key1 = random.randint(1, 100)
    repeat_gcd = gcd(key1, 26)
    print('To kleidi 1 den exei antistrofo sto Z26\nYpologismos MKD(GCD) ksana:',(key1,26), '= ',repeat_gcd)
print('\nto neo kleidi 1  einai:',key1)
print('to kleidi 2 einai:',key2)
if gcd ==1:
    result = gcd
else:
    result = repeat_gcd
print('MKD(GCD):',result)
antistrofos =modInverse(key1, 26)
print('o antistrofos tou',key1, ' sto mod 26 einai:',antistrofos)
print()
text = input('eisagete ena keimeno pros kruptografisi(me latinikous xaraktires):')
text = text.lower()
print('\nkruptografisi keimenou',text,'...')
print('To kruptografimeno keimeno einai: ',encrypt(text))
encrypted = encrypt(text)
print('\napokruptografisi keimenou',text, '...')
print('To apokruptografimeno keimeno einai:', decrypt(encrypted))

