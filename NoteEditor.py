import os
clear = lambda: os.system('cls')



captial = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']




idk = int(input("New File (1), Existing File (2): "))
clear()

if idk == 1:
    test = input("Enter a New File Name: ")
    clear()
if idk == 2:
   
    test = input("Enter The File Name: ")
    clear()


choice = int(input("Read(1), Write(2), Delete Line(3), Delete All(4): "))
clear()

if choice == 1:
    with open(test + ".txt",'r') as reader:
        print(reader.read())


elif choice == 2:
    with open(test + ".txt",'a') as a_writer:
        print('To Stop Writing Type "endwriting" ')
        print("Write Here: ")
        string = input()

        while string != "endwriting":
            
            if string[0] not in captial:
                print("No Capital Letter At Start Of Sentence")

            else:
                a_writer.write('\n' + string)

            string = input()
            

    with open(test + ".txt",'r') as reader:
        print(reader.read())


elif choice == 3:
    with open(test + ".txt", "r") as f:
        lines = f.readlines()
        
    with open(test + ".txt",'r') as reader:
        print(reader.read())

    cont = 'y'
    while cont == 'y':
        
        keyword = input("Enter Line (Copy & Paste The Line): ")
        cont = input("Another Line (y/n): ")
    
    with open(test + ".txt", "w") as f:
        for line in lines:
            if line.strip("\n") != keyword:
                f.write(line)
                
    with open(test + ".txt",'r') as reader:
        print(reader.read())

elif choice == 4:
    
    sure = input("Are you sure (y/n): ")
    if sure == 'y':
                 
        with open(test + ".txt",'w') as writer:
            writer.write("")
    elif sure == 'n':
        print("Okay, exiting....")
    else:
        print("ERROR: Use y or n")

print("")
button = input("Click Any Button To Exit...")
