import random
from VD_games.engine import run_game

DESCRIPTION = 'What is the result of the calculation?'


def generate_question():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operation = random.choice(['+', '-', '*'])

    question = f'{num1} {operation} {num2}'

    match operation:
        case '+':
            answer = num1 + num2
        case '-':
            answer = num1 - num2
        case '*':
            answer = num1 * num2

    return question, str(answer)


def main():
    run_game(DESCRIPTION, generate_question)


if __name__ == '__main__':
    main()
