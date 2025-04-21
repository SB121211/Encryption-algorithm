
import random
import re

def encrypt(text,seed1,seed2,seed3):
    encryption = ""
    for i in text:
        if i.lower() == "a":
            encryption = encryption + str((random.randint(400,414)*seed1*seed2)+seed3) + " "
        elif i.lower() == "b":
            encryption = encryption + str((random.randint(415,429)*seed1*seed2)+seed3) + " "
        elif i.lower() == "c":
            encryption = encryption + str((random.randint(430,444)*seed1*seed2)+seed3) + " "
        elif i.lower() == "d":
            encryption = encryption + str((random.randint(445,459)*seed1*seed2)+seed3) + " "
        elif i.lower() == "e":
            encryption = encryption + str((random.randint(460,474)*seed1*seed2)+seed3) + " "
        elif i.lower() == "f":
            encryption = encryption + str((random.randint(475,489)*seed1*seed2)+seed3) + " "
        elif i.lower() == "g":
            encryption = encryption + str((random.randint(490,504)*seed1*seed2)+seed3) + " "
        elif i.lower() == "h":
            encryption = encryption + str((random.randint(111,125)*seed1*seed2)+seed3) + " "
        elif i.lower() == "i":
            encryption = encryption + str((random.randint(126,140)*seed1*seed2)+seed3) + " "
        elif i.lower() == "j":
            encryption = encryption + str((random.randint(141,155)*seed1*seed2)+seed3) + " "
        elif i.lower() == "k":
            encryption = encryption + str((random.randint(156,170)*seed1*seed2)+seed3) + " "
        elif i.lower() == "l":
            encryption = encryption + str((random.randint(171,185)*seed1*seed2)+seed3) + " "
        elif i.lower() == "m":
            encryption = encryption + str((random.randint(186,200)*seed1*seed2)+seed3) + " "
        elif i.lower() == "n":
            encryption = encryption + str((random.randint(201,215)*seed1*seed2)+seed3) + " "
        elif i.lower() == "o":
            encryption = encryption + str((random.randint(216,230)*seed1*seed2)+seed3) + " "
        elif i.lower() == "p":
            encryption = encryption + str((random.randint(231,245)*seed1*seed2)+seed3) + " "
        elif i.lower() == "q":
            encryption = encryption + str((random.randint(246,260)*seed1*seed2)+seed3) + " "
        elif i.lower() == "r":
            encryption = encryption + str((random.randint(261,275)*seed1*seed2)+seed3) + " "
        elif i.lower() == "s":
            encryption = encryption + str((random.randint(276,290)*seed1*seed2)+seed3) + " "
        elif i.lower() == "t":
            encryption = encryption + str((random.randint(291,305)*seed1*seed2)+seed3) + " "
        elif i.lower() == "u":
            encryption = encryption + str((random.randint(306,320)*seed1*seed2)+seed3) + " "
        elif i.lower() == "v":
            encryption = encryption + str((random.randint(321,335)*seed1*seed2)+seed3) + " "
        elif i.lower() == "w":
            encryption = encryption + str((random.randint(336,350)*seed1*seed2)+seed3) + " "
        elif i.lower() == "x":
            encryption = encryption + str((random.randint(351,365)*seed1*seed2)+seed3) + " "
        elif i.lower() == "y":
            encryption = encryption + str((random.randint(366,380)*seed1*seed2)+seed3) + " "
        elif i.lower() == "z":
            encryption = encryption + str((random.randint(381,395)*seed1*seed2)+seed3) + " "
        elif i == " ":
            encryption = encryption + str((random.randint(550,564)*seed1*seed2)+seed3) + " "
    x = encryption.split()
    n_enc = ""
    for i in x:
        n_enc = n_enc + i[::-1] + " "
    return n_enc

def decrypt(text,key):
    parts = text.split()
    m_text = ""
    for i in parts:
        m_text = m_text + i[::-1] + " "
    m_parts = m_text.split()
    m_key = key.split()
    seed1 = ""
    seed2 = ""
    seed3 = ""
    for i in m_key:
        if len(i) == 1:
            seed2 = seed2 + i
        if len(i) == 4:
            seed1 = seed1 + i
        if len(i) == 5:
            seed3 = seed3 + i
    decryption = ""
    for i in m_parts:
        if int(i) >= (400*int(seed1)*int(seed2))+int(seed3) and int(i) <= (414*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "a"
        elif int(i) >= (415*int(seed1)*int(seed2))+int(seed3) and int(i) <= (429*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "b"
        elif int(i) >= (430*int(seed1)*int(seed2))+int(seed3) and int(i) <= (444*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "c"
        elif int(i) >= (445*int(seed1)*int(seed2))+int(seed3) and int(i) <= (459*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "d"
        elif int(i) >= (460*int(seed1)*int(seed2))+int(seed3) and int(i) <= (474*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "e"
        elif int(i) >= (475*int(seed1)*int(seed2))+int(seed3) and int(i) <= (489*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "f"
        elif int(i) >= (490*int(seed1)*int(seed2))+int(seed3) and int(i) <= (504*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "g"
        elif int(i) >= (111*int(seed1)*int(seed2))+int(seed3) and int(i) <= (125*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "h"
        elif int(i) >= (126*int(seed1)*int(seed2))+int(seed3) and int(i) <= (140*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "i"
        elif int(i) >= (141*int(seed1)*int(seed2))+int(seed3) and int(i) <= (155*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "j"
        elif int(i) >= (156*int(seed1)*int(seed2))+int(seed3) and int(i) <= (170*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "k"
        elif int(i) >= (171*int(seed1)*int(seed2))+int(seed3) and int(i) <= (185*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "l"
        elif int(i) >= (186*int(seed1)*int(seed2))+int(seed3) and int(i) <= (200*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "m"
        elif int(i) >= (201*int(seed1)*int(seed2))+int(seed3) and int(i) <= (215*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "n"
        elif int(i) >= (216*int(seed1)*int(seed2))+int(seed3) and int(i) <= (230*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "o"
        elif int(i) >= (231*int(seed1)*int(seed2))+int(seed3) and int(i) <= (245*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "p"
        elif int(i) >= (246*int(seed1)*int(seed2))+int(seed3) and int(i) <= (260*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "q"
        elif int(i) >= (261*int(seed1)*int(seed2))+int(seed3) and int(i) <= (275*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "r"
        elif int(i) >= (276*int(seed1)*int(seed2))+int(seed3) and int(i) <= (290*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "s"
        elif int(i) >= (291*int(seed1)*int(seed2))+int(seed3) and int(i) <= (305*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "t"
        elif int(i) >= (306*int(seed1)*int(seed2))+int(seed3) and int(i) <= (320*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "u"
        elif int(i) >= (321*int(seed1)*int(seed2))+int(seed3) and int(i) <= (335*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "v"
        elif int(i) >= (336*int(seed1)*int(seed2))+int(seed3) and int(i) <= (350*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "w"
        elif int(i) >= (351*int(seed1)*int(seed2))+int(seed3) and int(i) <= (365*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "x"
        elif int(i) >= (366*int(seed1)*int(seed2))+int(seed3) and int(i) <= (380*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "y"
        elif int(i) >= (381*int(seed1)*int(seed2))+int(seed3) and int(i) <= (395*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + "z"
        elif int(i) >= (550*int(seed1)*int(seed2))+int(seed3) and int(i) <= (564*int(seed1)*int(seed2))+int(seed3):
            decryption = decryption + " "


    return decryption

def key_encryption(seed1,seed2,seed3):
    indicator = "!@#$%^&*"
    seed1_e = ""
    seed2_e = ""
    seed3_e = ""
    for i in seed1:
        if i == "1":
            seed1_e = seed1_e + "s"
        if i == "2":
            seed1_e = seed1_e + "v"
        if i == "3":
            seed1_e = seed1_e + "r"
        if i == "4":
            seed1_e = seed1_e + ";"
        if i == "5":
            seed1_e = seed1_e + "q"
        if i == "6":
            seed1_e = seed1_e + "o"
        if i == "7":
            seed1_e = seed1_e + "p"
        if i == "8":
            seed1_e = seed1_e + "n"
        if i == "9":
            seed1_e = seed1_e + "d"
        if i == "0":
            seed1_e = seed1_e + "f"
    for i in seed2:
        if i == "1":
            seed2_e = seed2_e + "s"
        if i == "2":
            seed2_e = seed2_e + "v"
        if i == "3":
            seed2_e = seed2_e + "r"
        if i == "4":
            seed2_e = seed2_e + ";"
        if i == "5":
            seed2_e = seed2_e + "q"
        if i == "6":
            seed2_e = seed2_e + "o"
        if i == "7":
            seed2_e = seed2_e + "p"
        if i == "8":
            seed2_e = seed2_e + "n"
        if i == "9":
            seed2_e = seed2_e + "d"
        if i == "0":
            seed2_e = seed2_e + "f"
    for i in seed3:
        if i == "1":
            seed3_e = seed3_e + "s"
        if i == "2":
            seed3_e = seed3_e + "v"
        if i == "3":
            seed3_e = seed3_e + "r"
        if i == "4":
            seed3_e = seed3_e + ";"
        if i == "5":
            seed3_e = seed3_e + "q"
        if i == "6":
            seed3_e = seed3_e + "o"
        if i == "7":
            seed3_e = seed3_e + "p"
        if i == "8":
            seed3_e = seed3_e + "n"
        if i == "9":
            seed3_e = seed3_e + "d"
        if i == "0":
            seed3_e = seed3_e + "f"
    final_key = seed2_e + random.choice(indicator) + seed1_e + random.choice(indicator) + seed3_e
    return final_key

def key_translation(key):
    a_key = re.split(r"[!@#$%^&*]",key)
    t_key = ""
    for i in a_key:
        if len(i) == 1:
            if i == "s":
                t_key = t_key + "1" + " "
            if i == "v":
                t_key = t_key + "2" + " "
            if i == "r":
                t_key = t_key + "3" + " "
            if i == ";":
                t_key = t_key + "4" + " "
            if i == "q":
                t_key = t_key + "5" + " "
            if i == "o":
                t_key = t_key + "6" + " "
            if i == "p":
                t_key = t_key + "7" + " "
            if i == "n":
                t_key = t_key + "8" + " "
            if i == "d":
                t_key = t_key + "9" + " "
            if i == "f":
                t_key = t_key + "0" + " "
        if len(i) == 4:
            for n in i:
                if n == "s":
                    t_key = t_key + "1"
                if n == "v":
                    t_key = t_key + "2"
                if n == "r":
                    t_key = t_key + "3"
                if n == ";":
                    t_key = t_key + "4"
                if n == "q":
                    t_key = t_key + "5"
                if n == "o":
                    t_key = t_key + "6"
                if n == "p":
                    t_key = t_key + "7"
                if n == "n":
                    t_key = t_key + "8"
                if n == "d":
                    t_key = t_key + "9"
                if n == "f":
                    t_key = t_key + "0"
            t_key = t_key + " "
        if len(i) == 5:
            for n in i:
                if n == "s":
                    t_key = t_key + "1"
                if n == "v":
                    t_key = t_key + "2"
                if n == "r":
                    t_key = t_key + "3"
                if n == ";":
                    t_key = t_key + "4"
                if n == "q":
                    t_key = t_key + "5"
                if n == "o":
                    t_key = t_key + "6"
                if n == "p":
                    t_key = t_key + "7"
                if n == "n":
                    t_key = t_key + "8"
                if n == "d":
                    t_key = t_key + "9"
                if n == "f":
                    t_key = t_key + "0"
            t_key = t_key + " "
    return t_key

n = True
try:
    while n == True:
        print("1. Encryption")
        print("2. Decryption")
        a = input("Enter the desired action: ")
        if a == "1":
            t = input("\n" + "Enter your text to encrypt: ")
            text = t[::-1]
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            seed1 = random.randint(1235,2341)
            seed2 = random.randint(2,9)
            seed3 = random.randint(12345,34567)
            print("Encrypted text: " + encrypt(text,seed1,seed2,seed3))
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            key = key_encryption(str(seed1),str(seed2),str(seed3))
            print("Decryption key: " + key)
            h = True
            while h == True:
                c = input("Do you want to continue?(y or n): ")
                if c == "n":
                    n = False
                    h = False
                elif c == "y":
                    h = False
                else:
                    print("Invalid input!")

        elif a == "2":
            text = input("\n" + "Enter the text to decrypt: ")
            key = input("Enter the key: ")
            a_key = key_translation(key)
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            t = decrypt(text,a_key)[::-1]
            print("Here's the decrypted text: " + t)
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            c = input("Do you want to continue?(y or n): ")
            if c == "n":
                n = False
except ValueError:
    print("Invalid value!")

finally:
    print("Have fun!")