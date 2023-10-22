n = int(input('Input n:'))

def chan_le(n):
    if (n % 2 == 0):
        return True
    else:
        return False

if chan_le(n):
    print(n,'is even')
else:
    print(n,'is not even')