import requests
from bs4 import BeautifulSoup
import sys


class OnlineTranslator:

    def __init__(self):
        self.lgs = {
                '1': 'Arabic', '2': 'German', '3': 'English', '4': 'Spanish', '5': 'French',
                '6': 'Hebrew', '7': 'Japanese', '8': 'Dutch', '9': 'Polish', '10': 'Portuguese',
                '11': 'Romanian', '12': 'Russian', '13': 'Turkish'
                }

    def take_inp(self, data):
        frm_lg = data[1].capitalize()
        to_lg = data[2].capitalize()
        word = data[3]
        return [frm_lg, to_lg, word]

    def get_from_web(self, link):
        headers = {'User-Agent': 'Mozilla/5.0'}
        s = requests.Session()
        r = s.get(link, headers=headers)
        words = []
        sentences = []
        soup = BeautifulSoup(r.content, 'html.parser')

        for i in soup.find(id='translations-content').find_all('a'):
            words.append(i.text.strip())

        for i in soup.find(id='examples-content').find_all('span', {'class': 'text'}):
            sentences.append(i.text.strip())

        return [words, sentences]

    def write_to_file(self, name, content, sep, end):
        with open(f'{name}.txt', 'a', encoding='utf-8') as f:
            print(content, file=f, sep=sep, end=end)

    def trans_to_many(self, lst):
        word = lst[2]
        for n in self.lgs:
            if lst[0] != self.lgs[n]:
                url = f'https://context.reverso.net/translation/{lst[0].lower()}-{self.lgs[n].lower()}/{word}'
                try:
                    data = self.get_from_web(url)
                    words = data[0]
                    sentences = data[1]
                    print('\n'f'{self.lgs[n].lower()} translations:')
                    self.write_to_file(word, f'{self.lgs[n].lower()} translations:', sep=' ', end='\n')

                    print(*words[:1], sep='\n', end='\n\n')
                    for i in words[:1]:
                        self.write_to_file(word, i, sep='\n', end='\n\n')

                    print(f'{self.lgs[n].lower()} examples:')
                    self.write_to_file(word, f'{self.lgs[n].lower()} examples:', sep=' ', end='\n')

                    print(*sentences[:2], sep=':\n', end='\n\n')
                    for i in sentences[:2]:
                        self.write_to_file(word, i, sep=':\n', end='\n')
                except AttributeError:
                    print(f'Sorry, unable to find {word}')
                    break
                except requests.exceptions.ConnectionError:
                    print('Something wrong with your internet connection')
                    break
            else:
                continue

    def trans_word(self, lst):
        word = lst[2]
        url = f'https://context.reverso.net/translation/{lst[0].lower()}-{lst[1].lower()}/{word}'
        try:
            data = self.get_from_web(url)
            words = data[0]
            sentences = data[1]

            print('\n'f'{lst[0].lower()} translations:')
            print(*words[:5], sep='\n', end='\n\n')
            print(f'{lst[1].lower()} examples:')
            for i in [0, 2, 4, 6, 8, 10]:
                print(*sentences[i:i + 2], sep=':\n', end='\n\n')
        except AttributeError:
            print(f'Sorry, unable to find {word}')
        except requests.exceptions.ConnectionError:
            print('Something wrong with your internet connection')

    def main(self):
        args = sys.argv
        if len(args) == 4:
            quest = self.take_inp(args)
            if quest[1] == "All":
                self.trans_to_many(quest)
            elif quest[1] not in self.lgs.values():
                print(f"Sorry, the program does not support {quest[1].lower()}")
            elif quest[0] not in self.lgs.values():
                print(f"Sorry, the program does not support {quest[0].lower()}")
            else:
                self.trans_word(quest)
        else:
            print('Please, enter 4 arguments')


translate = OnlineTranslator()
translate.main()
