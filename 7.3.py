class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}

        for i in self.file_names:
            keys = [i]

            with open(i, encoding='utf-8') as file:
                values = file.read()
                values = values.lower()
                a = ',', '.', '=', '!', '?', ';', ':', ' - '

                for j in values:
                    if j in a:
                        values = values.replace(j, "")
                values = values.split()

            for key, value in zip(keys, values):
                all_words[key] = values
        return all_words

    def find(self, word):
        for key, value in self.get_all_words().items():
            for i in value:
                if word.lower() == i.lower():
                    return {key: (value.index(word.lower()) + 1)}

    def count(self, word):
        for key, value in self.get_all_words().items():
            for i in value:
                if word.lower() == i.lower():
                    return {key: (value.count(word.lower()))}


finder1 = WordsFinder('test_file.txt', 'test_file_2.txt')
finder2 = WordsFinder('Mother Goose - Monday’s Child.txt')

print(finder1.get_all_words())  # Все слова
print(finder1.find('TEXT'))  # 3 слово по счёту
print(finder1.count('teXT'))  # 4 слова teXT в тексте всего
print(finder2.get_all_words())
print(finder2.find('Child'))
print(finder2.count('ChIlD'))
