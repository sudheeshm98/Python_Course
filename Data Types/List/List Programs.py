#sum of numbers in the list
list5 = [1,2,3,4,5,6]
s = 0
for i in list5:
    s = i+s
print(s)

#removing spaces in a list
list6 = ["cat"," ","rat","dog"," ","pig"]
for i in list6:
    if i.isspace():
        list6.remove(i)
print(list6)

#Remove repeated elements from a given list without using any built in functions
list3 = ["a","a","b","c","c","d"]
list4 = []
for i in list3:
    l = ""
    for j in i:
        if j in l:
            continue
        else:
            l = l + j
    list4.append(l)
print(' '.join(list4))