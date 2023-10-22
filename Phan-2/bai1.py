i = int(input('Input i:'))

def giai_thua(i):
    if (i == 0):
        return 1
    else:
        return i * giai_thua(i - 1)
print('5! = ',giai_thua(i))