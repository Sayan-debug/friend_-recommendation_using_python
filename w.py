#implementation of friend recommendation system using graph data structure in the form of adjacency matrix
# build the list to take the names from the user
input_list = []
# total number of users = n
n = int(input("Enter the total number of users : "))

# take the names from the user
for i in range(0, n):
    print("Enter the name of index ", i,)
    name = str(input())
    input_list.append(name)

# build a adjacency matrix of connections nxn
# where rows and columns are equal to total number of users
rows, cols = (n, n)
matrix = []  # initializing a 1d list here
for i in range(rows):
    col = []  # initializing a 1d list here
    for j in range(cols):
        col.append(0)  # put 0 for all the columns
    matrix.append(col)
# matrix of size nxn is build with all values initialize to 0


# take input of the connections from user
c = int(input("Enter the total number of connections : "))
for i in range(0, c):
    # give two names at a time who are friends seperated by space
    x, y = input("Enter the name of indexs :").split()
    # find index of x and y in the input_list
    for g in range(0, n):
        if(x == input_list[g]):
            u1 = g  # index of first friend in input_list is stored in u1
        if(y == input_list[g]):
            u2 = g  # index of second friend in input_list is stored in u2
    # initialize the value with 1
    matrix[u1][u2] = 1
    matrix[u2][u1] = 1

print(matrix)  # printing the adjacency matrix here

# take input of the name to find recomended friends
print("Enter the name of person you want friend suggestion for:")
example = str(input())
for g in range(0, n):
    if(example == input_list[g]):
        x1 = g  # storing the index of the name from input_list to whom i need friend suggestion
# logic for friend recomendation system
s = set()  # creating set so that no duplicate values are stored
print("Friend suggestions are :")
for i in range(0, n):
    if(matrix[x1][i] == 1):
        count = i  # storing colum of the friends of the user
        for j in range(0, n):
            # 1)if the friends of user have any friends(x)
            # 2)is that friend(x) is already a friend of the user
            if(matrix[count][j] == 1 and matrix[x1][j] != 1):
                # to check that the user is not getting friend suggestion of himself
                if(input_list[j] != example):
                    s.add(input_list[j])  # add that user to the set container
# print(s)
for i in s:
    print(i, end=" ")
