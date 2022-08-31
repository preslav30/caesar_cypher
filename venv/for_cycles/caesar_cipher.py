import string

alphabet = string.ascii_lowercase
action = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n")
text = input("Type your message:\n").lower()
key = int(input("Type the shift number:\n"))
stop_loop = False

def caesar_cipher(beginning_text, key, direction):
    result = ""
    for letter in beginning_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encrypt":
                new_index = (index + key) % 26
            elif direction == "decrypt":
                new_index = (index - key) % 26
            new_letter = alphabet[new_index]
        else:
            new_letter = letter
        result += new_letter
    print(f"The {direction}ed text is: {result}")

while stop_loop == False:
    caesar_cipher(beginning_text=text, key=key, direction=action)
    go_again = input("\nDo you want to go again? Type 'yes' or 'no':\n")
    
    if go_again == "yes":
        action = input("\nType 'encrypt' to encrypt, type 'decrypt' to decrypt:\n")
        text = input("Type your message:\n").lower()
        key = int(input("Type the shift number:\n"))
    else:
        stop_loop = True
        print("\nThanks for using the program!")
        break



