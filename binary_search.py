#!env/bin/python
def binarySearch(number,arr):
    left = 0
    right = len(arr)-1
    
    while left <= right:
        m = (left+right)/2
        if number==arr[m]:
            return m
        elif number<arr[m]:
            right = m-1
        elif number>arr[m]:
            left = m+1

    return -1

def main():
    print "Insert the number:"
    n = input()
    print "Insert the array list:"
    arr = map(int, raw_input().split())

    result = 0

    result = binarySearch(n,arr)

    print "The number is in the position:"
    print result

if __name__ == "__main__":
    main()
