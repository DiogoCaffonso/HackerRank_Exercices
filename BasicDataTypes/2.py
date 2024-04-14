n = int(input())
x = input().split()
X = []
for i in x:
    X.append(int(i))
X.sort()
s = X[len(X) - 2]
j = 2
while s == X[len(X) - 1]:
    s = X[len(X) - j]
    j+=1
print(s)