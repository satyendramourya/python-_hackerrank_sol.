# substrings
# Stuart ------> consonants
# Kevin -------> vowels - aeiou

def minion_game(string):
    vowels = 'AEIOU'
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if string[i] in vowels :
            
            Kevin += len(string)-i
            #print( f' kevin -- {i , len(string)-i, Kevin }')
            
        else :
            Stuart += len(string)-i
            #print( f' Stuart -- {i , len(string)-i, Stuart }')
            

    if Kevin < Stuart :
        print( f'Stuart {Stuart}')
    elif Kevin > Stuart :
        print( f'Kevin {Kevin}')
    else : print('Draw')
    


if __name__ == '__main__':
    s = input()
    minion_game(s)