# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row['letter']:row['code'] for (index,row) in df.iterrows()}

name = input("Enter a word: ").upper()
# spelling = []
# for letter in name:
try:
    spelling = [dict[letter] for letter in name]
    # if letter in dict:
    #     spelling.append(dict[letter])
    # ANOTHER ALTERNATIVE METHOD:
    # spelling - []
    # spelling.append(dict[letter])
    print(spelling)
except KeyError:
    print("Sorry, only enter characters from the alphabet")