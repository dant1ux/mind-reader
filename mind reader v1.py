import time
print("Welcome to Mind Reader! What do you want to do?")
print("Mind read (1) About (2)")

while True:
    choice=input("Choose [1,2]: ")

    if choice in('1','2'):

        if choice== '1':
            print("Type anything, this program will read your mind and try to see what you typed.")
            textThing=str(input("Type here...: "))
            print("Beginning brain analyzing process...")
            time.sleep(1)
            print("Looking at brain patterns...")
            time.sleep(1)
            print("Hacking brain :o...")
            time.sleep(1)
            print("Done! Brain successfully hacked.")
            time.sleep(1)
            print('You were thinking: "' + textThing + '"')

        elif choice== '2':
            print("I made this program after seeing a funny gif and decided I wanted to try that out myself, this is the first version eventually I'm going to want to remake this as a gui app I think it would be dumb and funny. You can see the code here on my github it's the only thing I have there lol: https://github.com/dant1ux/mindreader")

        again=input("Go again? [Y/n]: ")
        if again=='n':
            break

    else:
        print("invalid")
