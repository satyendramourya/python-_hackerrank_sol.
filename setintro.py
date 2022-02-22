def average(array):

    # array= set(array)
    # no = len(array)
    # array = sum(array)
    # print(array/no)
    
    return sum(set(array))/len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)