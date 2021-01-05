from collections import Counter
def TypingKeyboard(mat,rows,cols,w):
    lst = []
    lst1 = [1,2,3,4,5]
    print(len(lst1))
    a = 'YES'
    b = 'NO'
    c = 0
    for i in range(0,rows):
        for j in range(0,cols):
            if mat[i][j] in w:
                lst.insert(c,1)
                print(mat[i][j],True)
                c +=1
    print(len(w))
    print(sum(lst))
    if len(w) == sum(lst):
        return a
    else:
        return b


rows ,cols = map(int,input().split())
mat = []
for i in range(rows):
    mat.append(input())
w = input()
print(TypingKeyboard(mat,rows,cols,w))
