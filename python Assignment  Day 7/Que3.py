original_Tuple = [(1,2,3) , [1,2] , ['a' , 'hit' , 'less']]

op = [x[0] for x in original_Tuple]

op1 = [i[1] for i in original_Tuple]

op2 = [j[-1] for j in original_Tuple]

new_List = op + op1 + op2

print(new_List)