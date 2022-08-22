# build the list to take the names from the user
input_list = []
n = int(input("Enter the total number of users : "))

# take the names from the user
for i in range(0, n):
    print("Enter the name of index ", i,)
    name = str(input())
    input_list.append(name)

# build a adjacency matrix of connections nxn
rows, cols = (n, n)
matrix = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    matrix.append(col)

# take input of the connections from user
c = int(input("Enter the total number of connections : "))
for i in range(0, c):
    x, y = input("Enter the name of indexs :").split()
    # find index of x and y in the input_list
    for g in range(0, n):
        if(x == input_list[g]):
            u1 = g
        if(y == input_list[g]):
            u2 = g
    matrix[u1][u2] = 1
    matrix[u2][u1] = 1

print(matrix)

# take input of the name to find recomended friends
print("Enter the name of person you want friend suggestion for:")
example = str(input())
for g in range(0, n):
    if(example == input_list[g]):
        x1 = g
# logic for friend recomendation system
s = set()
print("Friend suggestions are :")
for i in range(0, n):
    if(matrix[x1][i] == 1):
        count = i
        for j in range(0, n):
            if(matrix[count][j] == 1 and matrix[x1][j] != 1):
                if(input_list[j] != example):
                    s.add(input_list[j])
# print(s)
for i in s:
    print(i, end=" ")
