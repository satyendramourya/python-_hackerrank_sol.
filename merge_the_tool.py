def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        word = string[i:i+k]                           #--> slicing the word 
        seen = set()                           #--> creating the new set 
        for i in word :
            if i  not in seen:                           #--> checking the word is already present or not 
                print(i,end='')                           #-->printing the letter without the space 
                seen.add(i)                           #--> adding the letter if not present in the string 
        print()                           #-->printing the space for the net line
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)