counter = 0
cells = list("         ")
location = [13, 23, 33, 12, 22, 32, 11, 21, 31]

print('-' * 9)
print('|', cells[0], cells[1], cells[2], '|')
print('|', cells[3], cells[4], cells[5], '|')
print('|', cells[6], cells[7], cells[8], '|')
print('-' * 9)

while True:
    move = "".join(input("Enter the coordinates: ").split())
    if move.isnumeric():
        if int(move) in location:
            _ind = location.index(int(move))
            if cells[_ind] == " ":
                if counter % 2 == 0:
                    cells[_ind] = "X"
                    counter += 1
                    print('-' * 9)
                    print('|', cells[0], cells[1], cells[2], '|')
                    print('|', cells[3], cells[4], cells[5], '|')
                    print('|', cells[6], cells[7], cells[8], '|')
                    print('-' * 9)

                    if cells[0] == cells[1] == cells[2] == "X" \
                            or cells[3] == cells[4] == cells[5] == "X" \
                            or cells[6] == cells[7] == cells[8] == "X" \
                            or cells[0] == cells[3] == cells[6] == "X" \
                            or cells[1] == cells[4] == cells[7] == "X" \
                            or cells[2] == cells[5] == cells[8] == "X" \
                            or cells[0] == cells[4] == cells[8] == "X" \
                            or cells[6] == cells[4] == cells[2] == "X":
                        print("X wins")
                        break
                else:
                    cells[_ind] = "O"
                    counter += 1
                    print('-' * 9)
                    print('|', cells[0], cells[1], cells[2], '|')
                    print('|', cells[3], cells[4], cells[5], '|')
                    print('|', cells[6], cells[7], cells[8], '|')
                    print('-' * 9)
                    if cells[0] == cells[1] == cells[2] == "O" \
                            or cells[3] == cells[4] == cells[5] == "O" \
                            or cells[6] == cells[7] == cells[8] == "O" \
                            or cells[0] == cells[3] == cells[6] == "O" \
                            or cells[1] == cells[4] == cells[7] == "O" \
                            or cells[2] == cells[5] == cells[8] == "O" \
                            or cells[0] == cells[4] == cells[8] == "O" \
                            or cells[6] == cells[4] == cells[2] == "O":
                        print("O wins")
                        break
                if cells.count("X") == 4 and cells.count("O") == 5 or cells.count("X") == 5 and cells.count("O") == 4:
                    print("Draw")
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")






