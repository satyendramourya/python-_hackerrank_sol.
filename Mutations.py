"""
One solution is to convert the string to a list and then change the value.
Example

string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print string
abrackdabra

                            _________________________________________


Another approach is to slice the string and join it back.
Example

string = string[:5] + "k" + string[6:]
print string
abrackdabra

abracadabra
5 k  

"""
#               Sol 1  by list 
# def mutate_string(string, position, character):
#     string = list(string)
#     string[position] = character
#     string = ''.join(string)
#     return string

            #   Sol 2  by slicing
def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1 :]
    return string





if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)