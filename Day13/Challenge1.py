import ChallengeIf
from copy import deepcopy


class Cart:
    def __init__(self, x, y, arrow):
        self.x = x
        self.y = y
        self.arrow = arrow
        self.turns = 0

#... forgot to copy code to challenge 2... challenge 1 gone forever, RIP.
class Day13Challange1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.TestInputs = [open("Input2T", 'r').read()]
        self.TestOutputs = [(6,4)]
        self.Input = open("Input1", 'r').read()

    def Run(self, arg):
        p_arg = arg.split("\n")
        matrix = []

        for line in p_arg:
            matrix.append(list(line))


        max_len = max([len(x) for x in matrix])
        for line in matrix:
            while len(line) < max_len:
                line.append(' ')

        list_of_carts = []

        for i in range(len(matrix)):
            for j in range(max_len):
                char = matrix[i][j]
                if char == '>' or char == '<' or char == '^' or char == 'v':
                    list_of_carts.append(Cart(i,j, char))
                    if char == '>' or char == '<':
                        matrix[i][j] = '-'
                    else:
                        matrix[i][j] = '|'

        loop = True
        to_remove = []
        while loop:
            list_of_carts.sort(key=lambda c: (c.x, c.y))
            for cart in list_of_carts:
                if cart.arrow == '>':
                    cart.y += 1
                    if matrix[cart.x][cart.y] == '-':
                        pass
                    elif matrix[cart.x][cart.y] == '\\':
                        cart.arrow = "v"
                    elif matrix[cart.x][cart.y] == '/':
                        cart.arrow = "^"
                    elif matrix[cart.x][cart.y] == '+':
                        if cart.turns % 3 == 0:
                            cart.arrow = "^"
                        if cart.turns % 3 == 2:
                            cart.arrow = "v"
                        cart.turns += 1
                elif cart.arrow == 'v':
                    cart.x += 1
                    if matrix[cart.x][cart.y] == '|':
                        pass
                    elif matrix[cart.x][cart.y] == '\\':
                        cart.arrow = ">"
                    elif matrix[cart.x][cart.y] == '/':
                        cart.arrow = "<"
                    elif matrix[cart.x][cart.y] == '+':
                        if cart.turns % 3 == 0:
                            cart.arrow = ">"
                        if cart.turns % 3 == 2:
                            cart.arrow = "<"
                        cart.turns += 1
                elif cart.arrow == '^':
                    cart.x -= 1
                    if matrix[cart.x][cart.y] == '|':
                        pass
                    elif matrix[cart.x][cart.y] == '\\':
                        cart.arrow = "<"
                    elif matrix[cart.x][cart.y] == '/':
                        cart.arrow = ">"
                    elif matrix[cart.x][cart.y] == '+':
                        if cart.turns % 3 == 0:
                            cart.arrow = "<"
                        if cart.turns % 3 == 2:
                            cart.arrow = ">"
                        cart.turns += 1
                elif cart.arrow == '<':
                    cart.y -= 1
                    if matrix[cart.x][cart.y] == '-':
                        pass
                    elif matrix[cart.x][cart.y] == '\\':
                        cart.arrow = "^"
                    elif matrix[cart.x][cart.y] == '/':
                        cart.arrow = "v"
                    elif matrix[cart.x][cart.y] == '+':
                        if cart.turns % 3 == 0:
                            cart.arrow = "v"
                        if cart.turns % 3 == 2:
                            cart.arrow = "^"
                        cart.turns += 1
                # check for collision
                for cart1 in list_of_carts:
                    if cart1 is not cart and cart.y == cart1.y and cart.x == cart1.x:
                        to_remove.append(cart)
                        to_remove.append(cart1)
                        break
            for cart in to_remove:
                list_of_carts.remove(cart)
            to_remove = []
            if len(list_of_carts) == 1:
                loop = False
        print(list_of_carts[0].arrow)
        return list_of_carts[0].y, list_of_carts[0].x


obj = Day13Challange1()
obj.Test()
obj.Solve()