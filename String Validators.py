if __name__ == '__main__':
    s = input()
    # alphanumeric characters.           str.isalnum()
    # alphabetical characters.           str.isalpha()
    # digits                             str.isdigit()
    # lowercase characters               str.islower()
    # uppercase characters               str.isupper()

    print (any( f.isalnum() for f in s))
    print (any( f.isalpha() for f in s))
    print (any( f.isdigit() for f in s))
    print (any( f.islower() for f in s))
    print (any( f.isupper() for f in s))