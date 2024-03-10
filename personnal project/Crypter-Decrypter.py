import os
from time import *


Trad = True

options_cryptage = ["1","2","3","4","5","6","7","8","9","10","23","32"]


#Les dictionnaires de cryptage / décryptage :

binaire = {
    "a": "01100001",
    "b": "01100010",
    "c": "01100011",
    "d": "01100100",
    "e": "01100101",
    "f": "01100110",
    "g": "01100111",
    "h": "01101000",
    "i": "01101001",
    "j": "01101010",
    "k": "01101011",
    "l": "01101100",
    "m": "01101101",
    "n": "01101110",
    "o": "01101111",
    "p": "01110000",
    "q": "01110001",
    "r": "01110010",
    "s": "01110011",
    "t": "01110100",
    "u": "01110101",
    "v": "01110110",
    "w": "01110111",
    "x": "01111000",
    "y": "01111001",
    "z": "01111010",

    " ": "00100000",
    ".": "00101110",
    ",": "00101100",
    "!": "00100001",
    "?": "00111111",
    "/": "00101111",

    "1": "00110001",
    "2": "00110010",
    "3": "00110011",
    "4": "00110100",
    "5": "00110101",
    "6": "00110110",
    "7": "00110111",
    "8": "00111000",
    "9": "00111001",
    "0": "00110000",
}

octal = {
    "a": "141",
    "b": "142",
    "c": "143",
    "d": "144",
    "e": "145",
    "f": "146",
    "g": "147",
    "h": "150",
    "i": "151",
    "j": "152",
    "k": "153",
    "l": "154",
    "m": "155",
    "n": "156",
    "o": "157",
    "p": "160",
    "q": "161",
    "r": "162",
    "s": "163",
    "t": "164",
    "u": "165",
    "v": "166",
    "w": "167",
    "x": "170",
    "y": "171",
    "z": "172",

    " ": "040",
    '"': "042",
    "'": "047",
    ".": "056",
    ",": "054",
    "!": "041",
    "?": "077",
    "/": "057",

    "1": "061",
    "2": "062",
    "3": "063",
    "4": "064",
    "5": "065",
    "6": "066",
    "7": "067",
    "8": "070",
    "9": "071",
    "0": "060",
}

decimal = {
    "a": "097",
    "b": "098",
    "c": "099",
    "d": "100",
    "e": "101",
    "f": "102",
    "g": "103",
    "h": "104",
    "i": "105",
    "j": "106",
    "k": "107",
    "l": "108",
    "m": "109",
    "n": "110",
    "o": "111",
    "p": "112",
    "q": "113",
    "r": "114",
    "s": "115",
    "t": "116",
    "u": "117",
    "v": "118",
    "w": "119",
    "x": "120",
    "y": "121",
    "z": "122",

    " ": "032",
    '"': "034",
    "'": "039",
    ".": "046",
    ",": "044",
    "!": "033",
    "?": "063",
    "/": "47",

    "1": "049",
    "2": "050",
    "3": "051",
    "4": "052",
    "5": "053",
    "6": "054",
    "7": "055",
    "8": "056",
    "9": "057",
    "0": "048",
}

hexa_decimal = {
    "a": "61",
    "b": "62",
    "c": "63",
    "d": "64",
    "e": "65",
    "f": "66",
    "g": "67",
    "h": "68",
    "i": "69",
    "j": "6a",
    "k": "6b",
    "l": "6c",
    "m": "6d",
    "n": "6e",
    "o": "6f",
    "p": "70",
    "q": "71",
    "r": "72",
    "s": "73",
    "t": "74",
    "u": "75",
    "v": "76",
    "w": "77",
    "x": "78",
    "y": "79",
    "z": "7a",

    " ": "20",
    '"': "22",
    "'": "27",    
    ".": "2e",
    ",": "2c",
    "!": "21",
    "?": "3f",
    "/": "2f",

    "1": "31",
    "2": "32",
    "3": "33",
    "4": "34",
    "5": "35",
    "6": "36",
    "7": "37",
    "8": "38",
    "9": "39",
    "0": "30",
}

icositrimal = {
    "a": "23",
    "b": "24",
    "c": "25",
    "d": "26",
    "e": "27",
    "f": "28",
    "g": "29",
    "h": "30",
    "i": "31",
    "j": "32",
    "k": "33",
    "l": "34",
    "m": "35",
    "n": "36",
    "o": "37",
    "p": "38",
    "q": "39",
    "r": "40",
    "s": "41",
    "t": "42",
    "u": "43",
    "v": "44",
    "w": "45",
    "x": "46",
    "y": "47",
    "z": "48",

    " ": "51",
    '"': "53",
    "'": "58",    
    ".": "65",
    ",": "63",
    "!": "52",
    "?": "82",
    "/": "66",

    "1": "68",
    "2": "69",
    "3": "70",
    "4": "71",
    "5": "72",
    "6": "73",
    "7": "74",
    "8": "75",
    "9": "76",
    "0": "67",
}

os.system('cls')

print ("Bienvenue sur ce programme vous permettant de crypter / décrypter un texte.")

sleep(1)

while Trad == True:
    print ("Voici nos options de cryptage / décryptage :")

    sleep(0.75)

    print ("""
Cryptage :
    1) Cryptage en binaire
    2) Cryptage en octal
    3) Cryptage en décimal
    4) Cryptage en hexadécimal
    5) Cryptage en octo-décimal (alterne entre octal et décimal)
    23) Cryptage en icositrimal

Décryptage :
    6) Décrypteur en binaire
    7) Décrypteur en octal
    8) Décrypteur en décimal
    9) Décrypteur en hexadécimal
    10) Décrypeur en octo-décimal (alterne entre octal et décimal)
    32) Décrypteur en icositrimal
    """)

    un = "binaire"
    deux = "octal"
    trois = "décimal"
    quatre = "hexadécimal"
    cinq = "octo-décimal"
    vingt_trois = "icositrimal"

    sleep(0.5)

    print ("Veuillez choisir le mode de cryptage que vous souhaitez utiliser.")
    choix_crypt = input("")


    while choix_crypt not in options_cryptage:
        print ("Veuillez choisir le mode de cryptage que vous souhaitez utiliser.")
        choix_crypt = input("")

# Crypteur en ...

#binaire :
    if choix_crypt == "1":
        traduction = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Cryptage en " + un)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")

        for letter in phrase.lower():
            for keys in binaire.keys():
                if letter == keys:
                    traduction = str(traduction) + binaire.get(keys) + " "
        
        print ('\nVoici la traduction de "' + phrase + '" en ' + un + ":\n" + traduction)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#octal :
    if choix_crypt == "2":
        traduction = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Cryptage en " + deux )

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")

        for letter in phrase.lower():
            for keys in octal.keys():
                if letter == keys:
                    traduction = str(traduction) + octal.get(keys) + " "
                
        print ('\nVoici la traduction de "' + phrase + '" en ' + deux + ":\n" + traduction)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#décimal :
    if choix_crypt == "3":
        traduction = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Cryptage en " + trois)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")

        for letter in phrase.lower():
            for keys in decimal.keys():
                if letter == keys:
                    traduction = str(traduction) + decimal.get(keys) + " "
        
        print ('\nVoici la traduction de "' + phrase + '" en ' + trois + ":\n" + traduction)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#hexadécimal :
    if choix_crypt == "4":
        traduction = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Cryptage en " + quatre )

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")

        for letter in phrase.lower():
            for keys in hexa_decimal.keys():
                if letter == keys:
                    traduction = str(traduction) + hexa_decimal.get(keys) + " "
                
        print ('\nVoici la traduction de "' + phrase + '" en ' + quatre + ":\n" + traduction)

        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#octo-décimal :
    if choix_crypt == "5":
        traduction = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Cryptage en " + cinq)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")

        length = len(phrase)
        i = 0
        while i < length:
            for letter in phrase.lower():
                if int(i/2) == float(i/2):
                    for keys in octal.keys():
                        if letter == keys:
                            traduction = str(traduction) + octal.get(keys) + " "
                            i += 1
                                
                else:
                    for keys in decimal.keys():
                        if letter == keys:
                            traduction = str(traduction) + decimal.get(keys) + " "
                            i += 1

        print ('\nVoici la traduction de "' + phrase + '" en ' + cinq + ":\n" + traduction)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#icositrimal
    if choix_crypt == "23":
        traduction = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Cryptage en " + vingt_trois)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")

        for letter in phrase.lower():
            for keys in icositrimal.keys():
                if letter == keys:
                    traduction = str(traduction) + icositrimal.get(keys) + " "
        
        print ('\nVoici la traduction de "' + phrase + '" en ' + vingt_trois + ":\n" + traduction)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

# Décrypteur en ...

#binaire :
    if choix_crypt == "6":
        decrypter = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Décryptage en " + un)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")
    
        phrase_decoupe = phrase.split()

        def get_key(val):
   
            for key, value in binaire.items():
                if val == value:
                    return key
    
            return " [...] "
 

        for element in phrase_decoupe:
            decrypter = decrypter + get_key(element)

        print ('\nVoici la traduction de "' + phrase + '" en ' + un + ":\n" + decrypter)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#octal :
    if choix_crypt == "7":
        decrypter = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Décryptage en " + deux)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")
    
        phrase_decoupe = phrase.split()

        def get_key(val):
   
            for key, value in octal.items():
                if val == value:
                    return key
    
            return " [...] "
 

        for element in phrase_decoupe:
            decrypter = decrypter + get_key(element)

        print ('\nVoici la traduction de "' + phrase + '" en ' + deux + ":\n" + decrypter)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#décimal :
    if choix_crypt == "8":
        decrypter = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Décryptage en " + trois)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")
    
        phrase_decoupe = phrase.split()


        def get_key(val):
   
            for key, value in decimal.items():
                if val == value:
                    return key
    
            return " [...] "
 

        for element in phrase_decoupe:
            decrypter = decrypter + get_key(element)

        print ('\nVoici la traduction de "' + phrase + '" en ' + trois + ":\n" + decrypter)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#hexadécimal :
    if choix_crypt == "9":
        decrypter = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Décryptage en " + quatre)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")
    
        phrase_decoupe = phrase.split()


        def get_key(val):
   
            for key, value in hexa_decimal.items():
                if val == value:
                    return key
    
            return " [...] "
 

        for element in phrase_decoupe:
            decrypter = decrypter + get_key(element)


        print ('\nVoici la traduction de "' + phrase + '" en ' + quatre + ":\n" + decrypter)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#octo-décimal
    if choix_crypt == "10":
        decrypter = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Décryptage en " + cinq)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")
    
        phrase_decoupe = phrase.split()
        print(phrase_decoupe)

        def get_key_octal(val):
   
            for key, value in octal.items():
                if val == value:
                    return key
    
            return " [...] "
 
        def get_key_decimal(val):
   
            for key, value in decimal.items():
                if val == value:
                    return key
    
            return " [...] "


        length = len(phrase_decoupe)
        i = 0
        while i < length:
            for element in phrase_decoupe:

                if int(i/2) == float(i/2):
                    decrypter = decrypter + get_key_octal(element)
                    i += 1
                    

                else:
                    decrypter = decrypter + get_key_decimal(element)
                    i += 1

            

        print ('\nVoici la traduction de "' + phrase + '" en ' + cinq + ":\n" + decrypter )
                
        # Boucle du programme pour d'autre crytage / décryptage
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False

#icositrimal
    if choix_crypt == "32":
        decrypter = ""
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
        
        print ("Vous avez bien choisi :", choix_crypt +". Décryptage en " + vingt_trois)

        print ("Veuillez rentrer la phrase que vous voulez traduire :")
        phrase = input("")
    
        phrase_decoupe = phrase.split()

        def get_key(val):
   
            for key, value in icositrimal.items():
                if val == value:
                    return key
    
            return " [...] "
 

        for element in phrase_decoupe:
            decrypter = decrypter + get_key(element)

        print ('\nVoici la traduction de "' + phrase + '" en ' + vingt_trois + ":\n" + decrypter)
        restart = input("Voulez vous traduire autre chose ? [Y/n]")

        if restart == "Y" or  "y" :
            Trad = True
            sleep(0.5)
            os.system('cls')
        else:
            Trad = False    





# modele de cryptage

# if choix_crypt == "x":
#     for letter in phrase:
#         for keys in dictio.keys():
#             if letter == keys:
#                 traduction = str(traduction) + dictio.get(keys) + " "
    
#      print ('\nVoici la traduction de "' + phrase + '" en ' + nom de cryptage + "\n" + traduction)
#         restart = input("Voulez vous traduire autre chose ? [Y/n]")

#         if restart == "Y" or  "y" :
#             Trad = True
#             sleep(0.5)
#             os.system('cls')
#         else:
#             Trad = False
