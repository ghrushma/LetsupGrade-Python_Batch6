print("Python Program To Convert A Given List into Dictionary")

list1 = [1,2,3,4,5,6,7,8]

list2 = ["a" , "b" , "c" , "d" , "e"]

list_Dictionary = {}

for lists in list1:
    for listing in list2:
        list_Dictionary[lists] = listing
        list2.remove(listing)
        break

print("\nCombined List:\n",list_Dictionary)