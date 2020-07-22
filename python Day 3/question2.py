
print(" Sum_Of_Natural_Numbers\n")

#taking input from the user
natural_Number = int(input("Enter a natural number: \n"))
# I have stored this to display the actual number !!
temp = natural_Number
sum = 0
condition = 0

while (condition < natural_Number):
    sum += natural_Number
    natural_Number -= 1
    print(natural_Number , "-->" , sum)

print(f"\nSum of natural numbers for the number {temp} is found out to be : {sum}")