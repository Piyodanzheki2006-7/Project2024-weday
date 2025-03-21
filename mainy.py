import time
def bubble_sort(arr):
    d = len(arr)
    for p in range(d):
        for w in range(0, d-p-1):
            if arr[w] > arr[w+1]:
                arr[w], arr[w+1] = arr[w+1], arr[w]

def insertion_sort(arr):
    for e1 in range(1, len(arr)):
        ist = arr[e1]
        e2 = e1 - 1
        while e2 >= 0 and arr[e2] > ist:
            arr[e2 + 1] = arr[e2]
            e2 -= 1
        arr[e2 + 1] = ist

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        oe = arr[len(arr) // 2]  
        le = [x for x in arr if x < oe] 
        me = [x for x in arr if x == oe]  
        rt = [x for x in arr if x > oe] 
        return quick_sort(le) + me + quick_sort(rt) 

arr = [
    [64, 34, 25, 12, 6],
    [11.634, 90.535, 5.43534534553, 3.563, 45.5353464645],
    ['redqueen', 'madhatter', 'whiterabbit', 'alisa', 'cheshir'],
]


for bubble in range(len(arr)):
    st= time.time()
    bubble_sort(arr[bubble])
    et = time.time()
    print("Bubbles", arr[bubble], et-st)
    
for i in range(len(arr)):  
    st= time.time()
    insertion_sort(arr[i])
    et = time.time()
    print("Insertion", arr[i], et-st)
    
for rabbit in range(len(arr)):
    st= time.time()
    quick_sort(arr[rabbit])
    et = time.time()
    print("Quicksort", arr[rabbit], et-st)