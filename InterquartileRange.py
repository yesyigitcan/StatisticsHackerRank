#########################################################################################
# Calculate interquartile range (Q1 - Q3) by using a frequency table                    #
# Sample input                                                                          #
# 6                                                                                     #
# 6 12 8 10 20 16                                                                       #
# 5 4 3 2 1 5                                                                           #
# Sample output                                                                         #
# 9.0                                                                                   #
# Solution sort given table, calculate new cumulative frequency value, calculate median #
#########################################################################################
def cumulate(arr, length):
    arr2 = list()
    arr2.append((arr[0][0], arr[0][1]))
    for i in range(1, length):
        arr2.append((arr[i][0] , (arr[i][1] + arr2[i-1][1])))
    return arr2

def median(arr, start, end):
    mid = int((end + start) / 2)
    if (end-start) % 2 == 1:
        prev = None
        for row in arr:
            if row[1] < mid:
                continue
            elif row[1] >= mid + 1:
                if prev == None:
                    return row[0]
                else:
                    return (row[0] + prev) / 2.0
            elif row[1] >= mid:
                prev = row[0]
            
        
                
    else:
        for row in arr:
            if row[1] < mid:
                continue
            elif row[1] >= mid:
                return row[0]

    
            

def interquartileRange(arr, length):
    arr2 = cumulate(arr, length)
    num = arr2[-1][1]
    
    if num % 2 == 0:
        mid = int(num / 2)    
        q1 = median(arr2, 1, mid)
        q3 = median(arr2, mid+1, num)
    else:
        mid = int(num / 2) + 1
        q1 = median(arr2, 1, mid-1)
        q3 = median(arr2, mid+1, num)
    return (q3 - q1)
    


if __name__ == '__main__':
    length = int(input())
    arr = list(zip(map(int, input().split(' ')), map(int, input().split(' '))))
    arr = sorted(arr)
    
    rang = interquartileRange(arr, length)
    print("{:.1f}".format(rang))
