
print(" Program to extract Substrings !! \n")

sentence = input("Enter a sentence of your choice: \n").lower()

search_letter = input("\nEnter a Search Letter: ").lower()

length = len(sentence)
index = 0

if length > 0:
    if search_letter in sentence:
        count = sentence.count(search_letter)
        index = sentence.index(search_letter)
        print(f"\nSubstring count: {count} \n")
        print(f"Length = {length} \n")
        print(f"Index of the Sub_String : {index} \n")

    else:
        print("\nEnter a valid Search Letter !?! \n")