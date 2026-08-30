import random
from VD_games.engine import run_game

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    progression = []
    for i in range(length):
        current_element = start + i * step
        progression.append(str(current_element))

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    return ' '.join(progression), correct_answer


def main():
    run_game(DESCRIPTION, generate_progression)


if __name__ == '__main__':
    main()
