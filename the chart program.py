import mint
func = mint.in_out

#receiving valuses from user and converting into list
plain_list = func.separate(input("enter the numbers inside the 5*5 list in order. separate using comas "), ",")
if not len(plain_list) == 25:
    exit()
core_list = []
count = 0
for i in plain_list:
    if count % 5 == 0:
        core_list.append([])
    core_list[len(core_list) - 1].append(int(i))
    count += 1

#start of main algorithm
for row in range(5):
    for column in range(5):
        surrounding = []
        #check the above rows
        for i in range(row):
            surrounding.append(core_list[i][column])
        #check the left columns
        for i in range(column):
            surrounding.append(core_list[row][i])
        #sort the list of surroundings
        surrounding = func.sort_it(surrounding)
        if not len(surrounding) == 0:
            core_list[row][column] = core_list[row][column] + surrounding[0]
print(core_list[4][4])