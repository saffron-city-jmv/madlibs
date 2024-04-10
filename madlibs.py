'''
Mad Libs is a phrasal template word game created by Leonard Stern[1][2] 
and Roger Price.[3] It consists of one player prompting others 
for a list of words to substitute for blanks in a story before 
reading aloud. The game is frequently played as a party game or as a pastime.
-- Wikepedia
'''


# Project:
    # Create a history with blanks spaces where the user types a word to be filled
    # give a word to be fill in the blank


madlib = "There was a time when I was [0] no place to go, nowhere to call [1]. My only friend was [2]..."
print(madlib)

zero = str(input("Say a word"))

madlib = f"There was a time when I was {zero} no place to go, nowhere to call [1]. My only friend was [2]..."
print(madlib)