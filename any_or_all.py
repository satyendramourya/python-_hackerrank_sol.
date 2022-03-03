a = input()
check = list(input().split())
print(all([int(i)>0 for i in check]) and any(j==j[::-1] for j in check))

# positive no. - int(i)>0 
# j==j[::-1]  -- checks for palindromic integer