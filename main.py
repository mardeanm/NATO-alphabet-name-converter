
import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet={row.letter:row.code for (index,row) in data.iterrows()}


def convert_name(name):
    global alphabet
    name=list(name.upper())
    name=[alphabet[letter] for letter in name ]
    for n in name:
        print(n)
convert_name(input("What is your name? "))