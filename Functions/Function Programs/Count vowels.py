#Q.Define a function which counts vowels and consonant in a a word

def count(val):
    v = 0
    c = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            v = v+1
        else:
            c = c+1
    print(f'The count of vowels is {v}')
    print(f'The count of consonants id {c}')

x = input("Enter a Word : ")
count(x)

