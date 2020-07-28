print("Python Program To Convert A Given List into Dictionary")

list1 = [1,2,3,4,5,6,7,8]

list2 = ["a" , "b" , "c" , "d" , "e"]

merged_List = {
    list1[i] : list2[i] for i in range(len(list2))
}

print("\nCombined List:\n",merged_List)
