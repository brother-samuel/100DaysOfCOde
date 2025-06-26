#TODO: Create a letter using starting_letter.txt
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


#print(template.read())
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp