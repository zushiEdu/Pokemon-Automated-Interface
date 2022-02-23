print("Hello, Welcome to the PAI")

run = True

usernames = ["ethan", "john"]
passwords = ["password", "password"]

pokemons = [["Pikachu", "Squirtle"], ["Tortoise", "SVN"]]

signedIn = False
while run:

    # user interface
    if signedIn == False:
        print("Sign in or Register")
        print("1. Sign in")
        print("2. Register")
        print("3. Shutdown")
    else:
        print("4. Deposit A Pokemon")
        print("5. Logout")
        print("6. Display Pokemons Stored")
    signIn = input()

    # user register
    if signIn == "2":
        print("Enter the desired username")
        username = input()
        print("Enter the desired password")
        password = input()
        print("Is " + password + " the desired password")
        print("Y | N")
        confirm = input()
        while confirm == "N" or confirm == "n":
            print("Enter correct password")
            password = input()
            print("Is " + password + " the desired password")
            confirm = input()
        print("Username: " + username)
        print("Password: " + password)
        usernames.append(username)
        passwords.append(password)

    # user sign in
    if signIn == "1":
        print("Enter your username")
        username = input()
        print("Enter your password")
        password = input()
        for x in range(len(usernames)):
            if signedIn == False:
                if username == usernames[x]:
                    if password == passwords[x]:
                        signedIn = True
                        print("Sign in successful")
                        userSigned = username
                        userID = x
        print("If you didn't get signed in, the information you entered was invalid")

    # when the user signed in
    if signedIn:
        print("User " + userSigned + " signed in")

    # system shutdown
    if signIn == "3":
        print("Goodbye " + username)
        run = False

    # pokemon deposit
    if signIn == "4":
        print("Enter the name of the pokemon you desire to deposit")
        nameOfPokemon = input()
        pokemons[userID].append(nameOfPokemon)

    # logout
    if signIn == "5":
        signedIn = False

    # display pokemon
    if signIn == "6":
        if not len(pokemons) - 1 < userID:
            print("Pokemons stored: ", end="")
            for x in range(len(pokemons[userID])):
                if (x < len(pokemons[userID]) - 1):
                    ending = ", "
                else:
                    ending = ""
                print(pokemons[userID][x], end=ending)
            print("")
        else:
            print("No pokemon found in this account")
