template = open("Input/Letters/starting_letter.txt")
letter = template.read()
glist = open("Input/Names/invited_names.txt")
invitees = glist.readlines()
#print(invitees)
for guest in invitees:
    new_letter = letter.replace("[name]", guest.strip("\n"))
    with open(f"Output/ReadyToSend/letter_to_{guest.strip("\n")}.txt", mode="w") as file:
        file.write(new_letter)
template.close()
glist.close()

