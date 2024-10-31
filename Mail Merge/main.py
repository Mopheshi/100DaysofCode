# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def read_letter():
    with open("Input/Letters/starting_letter.txt") as letter:
        return letter.read()


def read_names():
    with open("Input/Names/invited_names.txt") as names:
        return names.readlines()


def write_letter(name, letter):
    name = name.strip()
    with open(f"Output/ReadyToSend/{name}'s_letter.docx", mode="w") as file:
        file.write(letter.replace("[name]", name))


def send_letters():
    letter = read_letter()
    names = read_names()

    for name in names:
        write_letter(name, letter)


if __name__ == "__main__":
    send_letters()
