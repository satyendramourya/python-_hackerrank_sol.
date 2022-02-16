
'''
a = "this is a string"
a = a.split(" ") # a is converted to a list of strings. 
print a
['this', 'is', 'a', 'string']
Joining a string is simple:

a = "-".join(a)                                 sting.join('in list')
print a
this-is-a-string 
'''
def split_and_join(line):
    # line = line.split(' ')
    # line = '-'.join(line)

    line = '-'.join(line.split(' '))
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)