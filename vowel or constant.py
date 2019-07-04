h=input()
if(h>='a' and h<='z'):
    l=['a','e','i','o','u']
    if h in l:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid')
