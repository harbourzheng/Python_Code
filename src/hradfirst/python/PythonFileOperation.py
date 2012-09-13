'''
Created on Sep 13, 2012
Python code for file operation 
@author: Bo
'''
f = open('\\temp\\wave1_new.csv', 'r')
output = open('\\temp\\abc.txt','w')
for line in f:
    output.write (line.rstrip())
f.close() 
print "Ok"
