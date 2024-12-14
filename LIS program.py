import mint
func = mint.in_out

#get the numbers and create core and alternative lists
core_list = func.separate(input("enter the subsequence. separate numbers using commas "), ",")
alternative_list = []
for i in core_list:
    alternative_list.append(0)
for i in range(len(core_list)):
    core_list[i] = int(core_list[i])

#main algorithm
for i in range(len(core_list)):
    best = 0
    for ii in range(i):
        if core_list[ii] < core_list[i] and alternative_list[ii] > best:
            best = alternative_list[ii]
    alternative_list[i] = best + 1
alternative_list = func.sort_it(alternative_list)
print(alternative_list[0])