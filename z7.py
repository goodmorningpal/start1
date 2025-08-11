def count_vowels(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def main():
    text = input("Введите текст: ")
    vowel_count = count_vowels(text)
    print(f"Количество гласных: {vowel_count}")
    if vowel_count == 0:
        print("Гласных букв не найдено!")
    else:
        print("Гласные присутствуют!")


if __name__ == "__main__":
    main()
