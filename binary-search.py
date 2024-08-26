def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
        
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < [midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else: #target > midpoint
        return binary_search(l, target, midpoint + 1, high)
    
if __name__ == '__main__':
    l = [1, 2, 4, 5, 10, 4]
    target = 10

    print(binary_search)



