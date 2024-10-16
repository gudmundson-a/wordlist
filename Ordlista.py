def list_insert(words, descriptions):

    #Tar input från användaren och frågar vilket ord de vill lägga till.
    listInput = input("Word to insert: ")
    desciption = input("Description of word: ")

    #Kontrollerar ifall ordet finns med i listan.
    if listInput in words:
        print(f"{listInput} is already in the list.")

    #Om ordet inte fanns i listan, läggs det nu till i sin lista med append() metoden.
    else:
        words.append(listInput)
        descriptions.append(desciption)
        #print(f"{listInput} has been added to the list.")

#Definierar funktion som letar efter ord i listorna words, descriptions.
def list_lookup(words, descriptions):
    #Tar input och kollar vad användaren vill leta efter för ord.
    word = input("Word to lookup: ")
    #Om ordet finns, skrivs ordet och dess beskrivning ut.
    if word in words:
        index = words.index(word)                   #Lagrar index från ordet så att man ska kunna referera till beskrivning.
        print(f"Description for {word} : {descriptions[index]}")
    else:                                           #Om ordet inte fanns i listan skrivs detta ut till användaren.
        print(f"{word} is not in the list.")


def list_main():
    #Skapar listorna som ska lagra värden från list_insert funktionen.
    words = []
    descriptions = []
    #printar ut och frågar användaren vilket alternativ dom vill göra.
    while True:

        print("\nMenu for dictionary")
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program")

        choice = input("\nChoose alternative: ")
        #Beroender på vilket input användaren ger, kalla på funktion som lägger till eller letar efter ett ord/beskrivning.
        if choice == '1':
            list_insert(words, descriptions)
        elif choice == '2':
            list_lookup(words, descriptions)
        elif choice == '3':
            print(">>>")         #Avslutar programmet med break
            break
        else:                                   #För att se till att användaren ger korrekt input och programmet inte kraschar.
            print("Invalid choice, try again: ")


##### ---------------------------------------------------------------------------------------- #####



def tuple_insert(tuple_list):
    #Input från användaren.
    tupleInput = input("Word to insert: ")
    #Loopar igenom hela listan och kollar ifall ordet användaren vill lägga till redan finns, isåfall skrivs felmeddelande ut.
    for existingWord in tuple_list:
        if tupleInput == existingWord[0]:
            print(f"{tupleInput} is already in the list. ")
            return
    #Om ordet ej fanns i listan, bes användaren ge en beskrivning till ordet. Båda dessa läggs då till i listan tuple_list med append() metoden.
    description = input("Description for word: ")
    tuple_list.append((tupleInput, description))
    print(f"{tupleInput} has been added to the list.")


def tuple_lookup(tuple_list):
    #input från användaren och kollar vad dom vill leta efter.
    tupleInput = input("Word to lookup: ")

    #Loopar igenom listan och kollar ifall ordet finns. Om det fanns så skrivs ordet och beskrivningen ut.
    for existingWord, description in tuple_list:
        if tupleInput == existingWord:
            print(f"Description for {tupleInput}: {description}")
            return
    print(f"{tupleInput} is not in the list.")


def tuple_main():

    tuple_list = []

    while True:

        print("\nMenu for dictionary")
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program")

        choice = input("\nChoose alternative: ")

        if choice == '1':
            tuple_insert(tuple_list)
        elif choice == '2':
            tuple_lookup(tuple_list)
        elif choice == '3':
            print(">>>")
            break
        else:
            print("Invalid input, try again.")


##### ---------------------------------------------------------------------------------------- #####


def dict_insert(dict):

    dictInput = input("Word to insert: ")

    if dictInput in dict:
        print(f"{dictInput} is already in the list.")
    else:
        description = input("Description of word: ")
        dict[dictInput] = description
        print(f"{dictInput} has been added to the list.")

def dict_lookup(dict):

    dictInput = input("Word to lookup: ")

    if dictInput in dict:
        print(f"Description for {dictInput} : {dict[dictInput]}")
    else:
        print(f"{dictInput} is not in the list.")


def dict_main():

    dict = {}

    while True:

        print("\nMenu for dictionary")
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program")

        choice = input("\nChoose alternative: ")

        if choice == '1':
            dict_insert(dict)
        elif choice == '2':
            dict_lookup(dict)
        elif choice == '3':
            print(">>>")
            break
        else:
            print("Invalid input, try again.")

##### ---------------------------------------------------------------------------------------- #####

#list_main()
#tuple_main()
dict_main()
