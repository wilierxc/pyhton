#open a file in write mode
f = open('test1.txt', 'w')
#use print to write string in to file
print('lift is short, I use Python', file=f)
#close the file
f.close()