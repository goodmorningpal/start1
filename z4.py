def count_words(text):
    words = text.split()
    return len(words)


def main():
    text = input("Введите текст: ")
    if text.strip():
        word_count = count_words(text)
        print(f"Количество слов: {word_count}")
    else:
        print("Текст пустой!")


if __name__ == "__main__":
    main()
