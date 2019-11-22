"""I/O Experiments."""
import os

filepath = os.path.realpath(__file__)
dirpath = os.path.dirname(filepath)
print(f'filepath = {filepath} dirpath= = {dirpath}')
os.chdir(dirpath)

myfile = open('myfile.txt')
content = myfile.read()
print(f'myfile read\n{content}')

myfile.seek(0)
content = myfile.read()
print(f'read\n{content}')

myfile.seek(0)
lines = myfile.readlines()
for l in lines:
    print(f'myfile read line: {l}')
myfile.close()

with open('myfile.txt') as withfile:
    withcontent = withfile.read()
    print(f'withfile read\n{withcontent}')

with open('myfileout.txt', mode='w') as myfileout:
    myfileout.write('ONE ON FIRST\n')
    myfileout.write('TWO ON SECOND')