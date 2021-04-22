import math
res_value_1 = [100, 180, 270, 390, 680, 1000]
res_value_2 = res_value_1
res = []
res1 = []
ind = []

'''
((1/res_value_1)+1/res_value_2))**-1
resistance for all combinations in parallel
'''
r=0
for X in res_value_1:
    c=0
    for Y in res_value_2:
        res.append(((1/X)+(1/Y))**-1)
        index = (r, c)
        ind.append(index)
        c+=1
    r+=1
'''
zipps every possible resistor combination with indexes of them
'''
for row in range(0,36):
    for column in range(0, 36):
        value = res[row]+res[column]
        row_f=ind[row]
        col_f=ind[column]
        grand_finale = [value, row_f, col_f]
        res1.append(grand_finale)
for result in res1:
    if 328<result[0]<332:
        resistor1 = res_value_1[result[1][0]], res_value_1[result[1][1]]
        resistor2 = res_value_1[result[2][0]], res_value_1[result[2][1]]
        print(result[0])
        print(resistor1,  '+', resistor2, '\n')
        