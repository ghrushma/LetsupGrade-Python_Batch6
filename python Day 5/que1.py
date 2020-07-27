print("Sorting Assignment-1\n")

data = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]

data.sort(key=lambda v:v == 0)

print(f"Sorted List : \n{data}")