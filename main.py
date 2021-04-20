# Implementation of Two Player Tic-Tac-Toe game in Python.

# Credits https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874

theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}


board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Твой ход " + turn + ".Куда шлепнем?")

        move = str(input())

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1

        else:
            print("Тут уже занято\nКуда шлепнем?")
            continue

        # Проверяем, кто выиграл после 5-ти ходов
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # Нижний ряд
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # Средний ряд
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # Верхний ряд
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # 1 столбец
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # Средний столбец
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # Правый столбец
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # Диагоняль
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # Диагоняль
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " выиграл. ****")
                break

                # Объявляем ничью, если не выиграл ни X, ни 0
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Мне игрока после хода
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

            # Задаем вопрос, перезапустить или нет?
    restart = input("Сыграем еще?(y/n)").lower()
    if restart == "y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()