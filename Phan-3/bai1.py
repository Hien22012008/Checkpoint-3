arr = [1, 2, 3, 4, 4, 5, 6, 7]

def check_arr(arr):
    if arr == sorted(arr):
        print('Increase')
    elif arr == sorted(arr, reverse = True):
        print('Decrease')
    else:
        print('None')

check_arr(arr)