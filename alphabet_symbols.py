# Program to print all Alphabet symbols using '*'.

while True:

    Alphabet = input('Enter any Alphabet:')

    # To Print Alphabet A symbol using '*':
    def A():
        for row in range(7):
            for col in range(5):
                if (row==0) and (col in {1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 2, 4, 5, 6}) and (col in {0, 4}):
                    print('* ', end='')
                elif row==3:
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'a':
        A()


    # To Print Alphabet B symbol using '*':
    def B():
        for row in range(7):
            for col in range(5):
                if (row in {0, 3, 6}) and (col in {0, 1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 2, 4, 5}) and (col in {0, 4}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'b':
        B()


    # To Print Alphabet C symbol using '*':
    def C():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 5}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row in {2, 3, 4}) and (col==0):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'c':
        C()


    # To Print Alphabet D symbol using '*':
    def D():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {0, 1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 2, 3, 4, 5}) and (col in {0, 4}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'd':
        D()


    # To Print Alphabet E symbol using '*':
    def E():
        for row in range(7):
            for col in range(5):
                if (row in {0, 3, 6}) and (col in range(5)):
                    print('* ', end='')
                elif (row in {1, 2, 4, 5}) and (col==0):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'e':
        E()


    # To Print Alphabet F symbol using '*':
    def F():
        for row in range(7):
            for col in range(5):
                if (row in {0, 3}) and (col in range(5)):
                    print('* ', end='')
                elif (row in {1, 2, 4, 5, 6}) and (col==0):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'f':
        F()


    # To Print Alphabet G symbol using '*':
    def G():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 5}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==4) and (col in {0, 2, 3, 4}):
                    print('* ', end='')
                elif (row in {2, 3}) and (col==0):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'g':
        G()

    # To Print Alphabet H symbol using '*':
    def H():
        for row in range(7):
            for col in range(5):
                if (row in {0, 1, 2, 4, 5, 6}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==3) and (col in range(5)):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'h':
        H()

    # To Print Alphabet I symbol using '*':
    def I():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in range(5)):
                    print('* ', end='')
                elif (row in range(1, 6)) and (col==2):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'i':
        I()

    # To Print Alphabet J symbol using '*':
    def J():
        for row in range(7):
            for col in range(5):
                if (row==0) and (col in range(5)):
                    print('* ', end='')
                elif (row in range(1, 5)) and (col==2):
                    print('* ', end='')
                elif (row==5) and (col in {0, 2}):
                    print('* ', end='')
                elif (row==6) and (col==1):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'j':
        J()


    # To Print Alphabet K symbol using '*':
    def K():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row in {1, 5}) and (col in {0, 3}):
                    print('* ', end='')
                elif (row in {2, 4}) and (col in {0, 2}):
                    print('* ', end='')
                elif (row==3) and (col in {0, 1}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'k':
        K()

    # To Print Alphabet L symbol using '*':
    def L():
        for row in range(7):
            for col in range(5):
                if (row in range(6)) and (col==0):
                    print('* ', end='')
                elif (row==6) and (col in range(5)):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'l':
        L()

    # To Print Alphabet M symbol using '*':
    def M():
        for row in range(7):
            for col in range(5):
                if (row in {0, 3, 4, 5, 6}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==1) and (col in {0, 1, 3, 4}):
                    print('* ', end='')
                elif (row==2) and (col in {0, 2, 4}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'm':
        M()

    # To Print Alphabet N symbol using '*':
    def N():
        for row in range(7):
            for col in range(5):
                if (row in {0, 1, 5, 6}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==2) and (col in {0, 1, 4}):
                    print('* ', end='')
                elif (row==3) and (col in {0, 2, 4}):
                    print('* ', end='')
                elif (row==4) and (col in {0, 3, 4}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'n':
        N()

    # To Print Alphabet O symbol using '*':
    def O():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in {1, 2, 3}):
                    print('* ', end='')
                elif (row in range(1, 6)) and (col in {0, 4}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'o':
        O()

    # To Print Alphabet P symbol using '*':
    def P():
        for row in range(7):
            for col in range(5):
                if (row in {0, 3}) and (col in {0, 1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 2}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row in {4, 5, 6}) and (col==0):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'p':
        P()

    # To Print Alphabet Q symbol using '*':
    def Q():
        for row in range(7):
            for col in range(5):
                if (row==0) and (col in {1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 2, 3}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==4) and (col in {0, 2, 4}):
                    print('* ', end='')
                elif (row==5) and (col in {0, 3, 4}):
                    print('* ', end='')
                elif (row==6) and (col in {1, 2, 3, 4}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'q':
        Q()

    # To Print Alphabet R symbol using '*':
    def R():
        for row in range(7):
            for col in range(5):
                if (row in {0, 3}) and (col in {0, 1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 2}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==4) and (col in {0, 2}):
                    print('* ', end='')
                elif (row==5) and (col in {0, 3}):
                    print('* ', end='')
                elif (row==6) and (col in {0, 4}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'r':
        R()

    # To Print Alphabet S symbol using '*':
    def S():
        for row in range(7):
            for col in range(5):
                if (row in {0, 3, 6}) and (col in {1, 2, 3}):
                    print('* ', end='')
                elif (row in {1, 5}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==2) and (col==0):
                    print('* ', end='')
                elif (row==4) and (col==4):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 's':
        S()

    # To Print Alphabet T symbol using '*':
    def T():
        for row in range(7):
            for col in range(5):
                if (row==0) and (col in range(5)):
                    print('* ', end='')
                elif (row in range(1, 7)) and (col==2):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 't':
        T()

    # To Print Alphabet U symbol using '*':
    def U():
        for row in range(7):
            for col in range(5):
                if (row in range(6)) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==6) and (col in {1, 2, 3}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'u':
        U()

    # To Print Alphabet V symbol using '*':
    def V():
        for row in range(7):
            for col in range(5):
                if (row in {0, 1, 2, 3, 4}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==5) and (col in {1, 3}):
                    print('* ', end='')
                elif (row==6) and (col==2):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'v':
        V()

    # To Print Alphabet W symbol using '*':
    def W():
        for row in range(7):
            for col in range(5):
                if (row in {0, 1, 2, 3, 6}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==4) and (col in {0, 2, 4}):
                    print('* ', end='')
                elif (row==5) and (col in {0, 1, 3, 4}):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'w':
        W()

    # To Print Alphabet X symbol using '*':
    def X():
        for row in range(7):
            for col in range(5):
                if (row in {0, 1, 5, 6}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row in {2, 4}) and (col in {1, 3}):
                    print('* ', end='')
                elif (row==3) and (col==2):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'x':
        X()

    # To Print Alphabet Y symbol using '*':
    def Y():
        for row in range(7):
            for col in range(5):
                if (row in {0, 1}) and (col in {0, 4}):
                    print('* ', end='')
                elif (row==2) and (col in {1, 3}):
                    print('* ', end='')
                elif (row in range(3, 7)) and (col==2):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'y':
        Y()

    # To Print Alphabet Z symbol using '*':
    def Z():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6}) and (col in range(5)):
                    print('* ', end='')
                elif (row==1) and (col==4):
                    print('* ', end='')
                elif (row==2) and (col==3):
                    print('* ', end='')
                elif (row==3) and (col==2):
                    print('* ', end='')
                elif (row==4) and (col==1):
                    print('* ', end='')
                elif (row==5) and (col==0):
                    print('* ', end='')
                else:
                    print('  ', end='')
            print()
    if Alphabet.lower() == 'z':
        Z()

    option = input('Yow wanna print another [Y|N]:')
    if option.lower() != 'y':
        break
