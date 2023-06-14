"""
Search for a string in search files
"""
#Using for loop
with open("samplefile.txt","r") as fp:
    f5=fp.read()
    for i in f5:
        if 'python' in f5:
            print("Present")
            break
        else:
            print("Not Present")
            break

#Using Function

