import io
from pprint import pprint


print()


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):

        # Создайте пустой словарь all_words.
        all_words = {}

        # Переберите названия файлов и открывайте каждый из них, используя оператор with.
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:

                    # Для каждого файла считывайте единые строки,
                    # переводя их в нижний регистр (метод lower()).
                    line = line.lower()

                    # Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - ']
                    # в строке.
                    punctuation = [',', '.', '=', '!', '?', ';', ':']
                    for punct in punctuation:
                        line = line.replace(punct, '')
                    line = line.replace(' - ', ' ')


                all_words[file_name] = words
        return all_words


    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1

        return places


    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count

        return counters




finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))