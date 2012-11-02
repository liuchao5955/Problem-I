'''
Created on 2012-8-10

@author: Administrator
'''

a = 'ball'
b = ['at', '', '', '', 'ball', '', '', 'car', '', 'dad', '', '']
def method():
    for x in range(len(b)):
        if b[x] == a:
            return x
    return -1    

print method()

print method()

print method()
