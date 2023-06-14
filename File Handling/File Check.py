"""
To check if the file is exist or not
"""
import os.path

file_path = r'C:\Users\Sudheesh M\PycharmProjects\PythonCource\File Handling\\samplefile.txt'

flug = os.path.exists(file_path)
if flug:
    print(f'The file {file_path} exists')
else:
    print(f'The file {file_path} does not exists')

#File Size
size = os.path.getsize(file_path)
print(f'The {file_path} size is' , size , 'bytes')

#Delete lines from a file
