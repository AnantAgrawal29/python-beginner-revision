print(r'''          
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88        
''')

def ceasar(message,shift,choice):
    new_message = ""
    for char in message:
        nch = char
        shifted = ord(nch)
        if 97 <= shifted <= 122:
            if choice[0] == 'e':
                if shifted+shift>122 :
                    nch = chr(shift-(122-shifted)+97-1)
                else:
                    nch = chr(shifted+shift)
            else:
                if shifted-shift<97:
                    nch = chr(122-shift+((shifted-97)+1))
                else:
                    nch = chr(shifted-shift)
        new_message += nch
    return new_message

while True:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if not (choice=='encode' or choice=='decode'):
        print("Wrong Input")
        break
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    result = ceasar(message,shift,choice)
    print(f"Here's your {choice}d result: {result}")
    cont = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if cont=='no':
        print("Goodbye")
        break