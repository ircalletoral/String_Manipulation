#Code 3 String Manipulation

#Problem 1
name = input("Greetings! What is your name?: ")
print("Hello: " + name + "! Nice to meet you")


# Problem 2
word = input("Please enter a word: ")
drow = word[::-1]
print(f"Your word in reverse is: {drow}! ")

#Problem 3
sentence = input("How's the weather today?")
char_count = len(sentence)
print(f"Interesting! Did you know your phrase had {char_count} characters in it?")

#Problem 4
vowel_word = input("What is your phrase?: ")
vowel_lower = vowel_word.lower()
a_count = vowel_lower.count("a")
e_count = vowel_lower.count("e")
i_count = vowel_lower.count("i")
o_count = vowel_lower.count("o")
u_count = vowel_lower.count("u")

vowel_sum = a_count + e_count + i_count + o_count + u_count
print(f"The phrase '{vowel_word}' has {vowel_sum} vowels in it!")

#Problem 5

pos_palindrome = input("PLease provide a word: ")
lower_pospdrome = pos_palindrome.lower()

if lower_pospdrome == lower_pospdrome[::-1]:
    print("This is a palindrome!")
else:
    print("THis word is not a palindrome :( ")

#Problem 6
secret_message = input("Please input your secret message... : ")
encrypted = secret_message.upper().replace(" ", "_")
print(encrypted)

#Thank you! Everything should work properly