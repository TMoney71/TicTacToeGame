def main():

    tic  = '''1|2|3
-+-+-
4|5|6
-+-+-
7|8|9'''
    print(tic)  
    turn = input("Who wants to go first x/o: ")
    # changex = input("X's turn chose a square (1-9): ")
    # changey = input("y's turn chose a square (1-9): ")
    def x_turn():
        changex = input("X's turn chose a square (1-9): ")
        tic2 = tic.replace( changex, 'X', 1)
        print(tic2)
        return tic2

    def o_turn():
        changeo = input("O's turn chose a square (1-9): ")
        tic2 = tic.replace( changeo, 'O', 1)
        print(tic2)
        return tic2

    if turn is 'x':
        tic = x_turn()
        # tic = print(x_turn())
        # print(tic)
        tic = o_turn()
        # tic = x_turn()
        # tic = o_turn()
        # tic = x_turn()
        # tic = o_turn()
        # tic = x_turn()
        # tic = o_turn()
        # tic = x_turn()

    else:
        tic = o_turn()
        tic = x_turn()
        tic = o_turn()
        tic = x_turn()
        tic = o_turn()
        tic = x_turn()
        tic = o_turn()    
        tic = x_turn()
        tic = o_turn()


if __name__ == '__main__':
    main()