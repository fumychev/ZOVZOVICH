import math
import random
from VD_games.engine import run_game

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f'{num1} {num2}'
    answer = math.gcd(num1, num2)

    return question, str(answer)


def main():
    run_game(DESCRIPTION, generate_question)


if __name__ == '__main__':
    main()
