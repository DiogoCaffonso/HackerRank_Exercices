x = int(input())
y = int(input())
z = int(input())
n = int(input())
K = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                m = [i, j, k]
                K.append(m)
print(K)