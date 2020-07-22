print(" Program to check weather,the number is Prime or Not ?? \n")

number = int(input("Enter a number : \n"))
temp = number

if number > 1:
    for i in range(2,number):# Search range is from 2 to number - 1
        if(number % i) == 0:
            var = number//i
            print(f"The entered number : {temp} , is not a prime number \n")
            print(f"As {i} times {var} is {temp}")
            break
    else:
        print(f"Entered Number: {temp} is a prime number")

else:
    print(f"Entered Number: {temp} , is not a prime number")