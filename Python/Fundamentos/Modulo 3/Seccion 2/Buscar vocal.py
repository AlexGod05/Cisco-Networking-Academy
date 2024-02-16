print("Ingrese una palabra: ")
user_word = input().upper()

for letter in user_word:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    print(letter)
