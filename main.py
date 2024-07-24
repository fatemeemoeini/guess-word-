import random

# list of namee
# select one name randomly
# get user char
# check => show feedback
# guess >0 =>win /loss

names = ["ali", "arshia", "ghasem ", "mohsen "]

selected_name = random.choice(names)

guess_count = len(selected_name)
guessed_list =['-'] * len(selected_name)

while guess_count > 0:
    guessed_char = input('Enter a char :\n ')

    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print('you have guessed befor , try new character ')
            else:
                for idx,char in enumerate(selected_name ):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                current_guess = "" .join(guessed_list)
                print(f"perfect => (current_guess)")
                if not "-" in guessed_list:
                    print("you won !")
                    braak
        else:
            guess_count -= 1
            print(f"wrong! =>remained guesses :{guess_count}")
    else:
        print("please enter a valid character")
