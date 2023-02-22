
import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet={row.letter:row.code for (index,row) in data.iterrows()}


def convert_name():

    global alphabet
    name = input("What is your name? ")
    final_name=list(name.upper())
    try:
        final_name=[alphabet[letter] for letter in final_name ]
    except KeyError:
        print("Sorry only letters, please")
        convert_name()
    else:
        print(final_name)

convert_name()