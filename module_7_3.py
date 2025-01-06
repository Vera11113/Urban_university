class WordsFinder:

    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):

        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding = 'utf-8') as file:
                str_del = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n', '']
                all_words[name] = []
                for line in file:
                    line = "".join([char for char in line if char not in str_del])
                    all_words[name].extend(line.lower().split(' '))
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        for key, values in all_words.items():
            if word.lower() in values:
                return {key: values.index(word.lower()) + 1}

    def count(self, word):
        all_words = self.get_all_words()
        for key, values in all_words.items():
            if word.lower() in values:
                return {key: values.count(word.lower())}




finder2 = WordsFinder('file1.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


