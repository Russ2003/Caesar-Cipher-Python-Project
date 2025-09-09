def encryptMessage(userInput, caesarShift):
    encryptedMessage = ""

    for char in userInput:
        if char.isalpha():
            if char.isupper():
                char_code = (ord(char) - 65 + caesarShift) % 26 + 65
            else:
                char_code = (ord(char) - 97 + caesarShift) % 26 + 97
            encryptedMessage += chr(char_code)
        elif char.isnumeric():
            num_code = (int(char) + caesarShift) % 10
            encryptedMessage += str(num_code)
        else:
            encryptedMessage += char
    return encryptedMessage


def decryptMessage(userInput, caesarShift):
    decrypted_message = ""

    for char in userInput:
        if char.isalpha():
            if char.isupper():
                char_code = (ord(char) - 65 - caesarShift) % 26 + 65
            else:
                char_code = (ord(char) - 97 - caesarShift) % 26 + 97
            decrypted_message += chr(char_code)
        elif char.isnumeric():
            num_code = (int(char) - caesarShift) % 10
            decrypted_message += str(num_code)
        else:
            decrypted_message += char
    return decrypted_message

tryagain = "Y"
while tryagain == "Y":
    print("This program allows you to encrypt and decrypt messages using Caesar Cipher.")
    print("-----------------------------------")
    print("What would you like to do?")
    print("1. Encrypt a Message")
    print("2. Decrypt a Message")
    print("-----------------------------------")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n")
        print("You have chosen to encrypt a message.")
        print("-----------------------------------")
        message = input("Enter a message: ")
        caesarShift = int(input("Enter the number of caesarShifts: "))
        result = encryptMessage(message, caesarShift)
        print("-----------------------------------")
        print("Encrypted Message: " + str(result))

    elif choice == 2:
        print("")
        print("You have chosen to decrypt a message.")
        print("-----------------------------------")
        message = input("Enter a message: ")
        caesarShift = int(input("Enter the number of caesarShifts: "))
        result = decryptMessage(message, caesarShift)
        print("-----------------------------------")
        print("Decrypted Message: " + str(result))

    print("-----------------------------------")
    tryagain = input("Do You Want to Try Again (Y/N)? ")
    print("-----------------------------------")
print("Thank you for using this program!")
