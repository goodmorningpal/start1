import random


def guess_number():
    target = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Угадайте число от 1 до 100: "))
            attempts += 1
            if guess < target:
                print("Слишком мало!")
            elif guess > target:
                print("Слишком много!")
            else:
                print(f"Поздравляем! Угадано за {attempts} попыток!")
                break
        except ValueError:
            print("Введите целое число!")


guess_number()
