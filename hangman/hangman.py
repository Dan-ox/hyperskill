import random
print('H A N G M A N')


while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    print('')

    if choice == "play":
        var = ['python', 'java', 'kotlin', 'javascript']
        c_var = random.choice(var)
        p_phrased = len(c_var) * "-"
        atts = 0
        u_let_list = []


        while atts < 8 or p_phrased == c_var:
            print('')
            print(p_phrased)
            let = input("Input a letter: ")

            if len(let) == 1:

                if let.islower() and let.isascii() and let.isalpha():
                    u_let_list.append(let)

                    if let in c_var:
                        ind = c_var.find(let)
                        p_phrased = p_phrased[:ind] + let + p_phrased[ind + 1:]

                        if c_var.count(let) == 2:
                            ind = c_var.rfind(let)
                            p_phrased = p_phrased[:ind] + let + p_phrased[ind + 1:]

                        if u_let_list.count(let) > 1:
                            print("You already typed this letter")

                        if p_phrased == c_var:
                            break

                    else:
                        if u_let_list.count(let) > 1:
                            print("You already typed this letter")
                        else:
                            atts += 1
                            print('No such letter in the word')

                else:
                    print("It is not an ASCII lowercase letter")

            else:
                print("You should input a single letter")


        if atts == 8:
            print("You are hanged!")
            print("")
        else:
            print('')
            print(p_phrased)
            print("You guessed the word!")
            print("You survived!")
            print("")
            choice

    elif choice == "exit":
        break

    else:
        choice


