#count vovels in a sentence

word = input("Enter the sentence:\n")

Updated_word = word.lower()

vowels = ['a','e','i','o','u']

count = 0
for i in Updated_word:
    if i in vowels:
        count = count + 1


print(f"Total vowels:{count}")
