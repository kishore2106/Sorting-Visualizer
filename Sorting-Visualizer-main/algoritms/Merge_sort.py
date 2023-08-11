import time

def merge_sort(lst,l,r,drawrectangle,delay):
    if(l<r):
        m = l + (r-l) // 2
        merge_sort(lst,l,m,drawrectangle,delay)
        merge_sort(lst,m+1,r,drawrectangle,delay)
        merge(lst,l,m,r,drawrectangle,delay)

def merge(lst,l,m,r,drawrectangle,delay):
    n1 = m-l+1
    n2 = r-m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0,n1):
        L[i] = lst[l+i]

    for j in range(0,n2):
        R[j] = lst[m+1+j]

    i = 0
    j = 0
    k = l

    while i<n1 and j<n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            drawrectangle(lst, ['blue' if x == j else 'green' if x == k else 'black' for x in range(len(lst))] )
            time.sleep(delay)
            i+=1
        else:
            lst[k] = R[j]
            drawrectangle(lst, ['blue' if x == j else 'green' if x == k else 'black' for x in range(len(lst))] )
            time.sleep(delay)
            j+=1
        k += 1

    while i<n1:
        lst[k] = L[i]
        drawrectangle(lst, ['blue' if x == i else 'green' if x == k else 'black' for x in range(len(lst))] )
        time.sleep(delay)
        i+=1
        k+=1

    while j<n2:
        lst[k] = R[j]
        drawrectangle(lst, ['blue' if x == j else 'green' if x == k else 'black' for x in range(len(lst))] )
        time.sleep(delay)
        j+=1
        k+=1
    drawrectangle(lst, ['blue' for x in range(len(lst))])

# lst=[12,2,33,4,14,4]
# n = len(lst)