#########################################################################################
# Find quartiles (Q1, Q2, Q3) by using a number collection                              #
# Sample input (legth of list, list)                                                    #
# 9                                                                                     #
# 3 7 8 5 12 14 21 13 18                                                                #
# Sample output                                                                         #
# 6                                                                                     #
# 12                                                                                    #
# 16                                                                                    #
# Solution use a median function to calculate each subset iteratively                   #
#########################################################################################

def median(arr):
    length = len(arr)
    mid = int(length/2)
    if length % 2 == 0:
        return ( arr[mid-1] + arr[mid] ) / 2
    else:
        return arr[mid]

def quartiles(arr, length):
    mid = int(length/2)
    q2 = median(arr) 
    if length % 2 == 0:
        q1 = median(arr[:mid])
        q3 = median(arr[mid:])
    else:
        q1 = median(arr[:mid])
        q3 = median(arr[mid+1:])
    return q1, q2, q3
    




if __name__ == '__main__':
    length = int(input())
    arr = sorted(list(map(int, input().split(' '))))

    q1, q2, q3 = quartiles(arr, length)
    print(int(q1))
    print(int(q2))
    print(int(q3))
