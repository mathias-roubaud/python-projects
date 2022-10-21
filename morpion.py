import random


class morpion:

    def __init__(self):
        self.tableau = []

    def creer_tableau(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.tableau.append(row)

    def get_random_premier_joueur(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, joueur):
        self.tableau[row][col] = joueur

    def is_joueur_win(self, joueur):
        win = None

        n = len(self.tableau)

        for i in range(n):
            win = True
            for j in range(n):
                if self.tableau[i][j] != joueur:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if self.tableau[j][i] != joueur:
                    win = False
                    break
            if win:
                return win

        win = True
        for i in range(n):
            if self.tableau[i][i] != joueur:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.tableau[i][n - 1 - i] != joueur:
                win = False
                break
        if win:
            return win
        return False

        for row in self.tableau:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_tableau_filled(self):
        for row in self.tableau:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_joueur_turn(self, joueur):
        return 'X' if joueur == 'O' else 'O'

    def show_tableau(self):
        for row in self.tableau:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.creer_tableau()

        joueur = 'X' if self.get_random_premier_joueur() == 1 else 'O'
        while True:
            print(f"au tour de {joueur}")

            self.show_tableau()

            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            self.fix_spot(row - 1, col - 1, joueur)

            if self.is_joueur_win(joueur):
                print(f"joueur {joueur} a gagné la partie !")
                break

            if self.is_tableau_filled():
                print("Match nul !")
                break

            player = self.swap_joueur_turn(joueur)

        print()
        self.show_tableau()


morpion = morpion()
morpion.start()
