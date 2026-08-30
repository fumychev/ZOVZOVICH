import random

def main():
    print('Welcome to the Brain Game!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        question = random.randint(1, 100)
        print(f'Question: {question}')
        answer = input('Your answer: ').lower().strip()

        correct = 'yes' if question % 2 == 0 else 'no'

        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is a wrong answer ;(. Correct answer was '{correct}'.")
            print("Let's try again!")
            return
    print('Congratulations!')

if __name__ == '__main__':
    main()
