
symbols = input("Enter cells: ")

if len(symbols) == 9:
    if 'X' or 'O' or '_' in symbols:
        print('-' * 9)
        fst_line = symbols[0] + ' ' + symbols[1] + ' ' + symbols[2]
        scnd_line = symbols[3] + ' ' + symbols[4] + ' ' + symbols[5]
        thrd_line = symbols[6] + ' ' + symbols[7] + ' ' + symbols[8]
        print('|', fst_line, '|')
        print('|', scnd_line, '|')
        print('|', thrd_line, '|')
        print('-' * 9)
