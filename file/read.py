stream = open('./demo.txt', 'rt')
print('\n Is this readable ? '+ str(stream.readable()))
print('\n Read one character: ' +  stream.read(1))
print('\n Read to end of line : ' + stream.readline())
print('\n Read all lines to end of file : \n'+ str(stream.readlines()))
