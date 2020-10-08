import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style


def process_filename(url):
    if "www" in url:
        url = url.split('www')[1]
    if '.com' in url:
        url = url.split('.com')[0]
    if '.org' in url:
        url = url.split('.org')[0]
    url = url.strip('https://')
    return url


def write_file(file_name, variable):
    with open(directory_name + '/' + file_name, 'w', encoding='UTF-8') as out_file:
        out_file.write(variable)


def create_dir():
    args = sys.argv

    if len(args) > 1:
        directory_name = args[1].split('-')[0]

        if directory_name:
            if not os.path.exists(directory_name):
                os.mkdir(directory_name)


def special_printing(soup):
    tags = ['p', 'h1', 'a', 'ul', 'ol', 'li']
    for tag in tags:
        content = soup.find_all(tag)
        for i in content:
            print(Fore.BLUE + i.text if tag == 'a' else Style.RESET_ALL + i.text)


def rqt_to_internet(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'html.parser')


create_dir()
stack = deque()

while True:
    url = input()
    if url == "exit":
        break
    elif url == "back":
        if stack:
            stack.pop()
        if stack:
            print(stack.pop())
    elif "." in url:
        if not url.startswith("https://"):
            url = "https://" + url

        soup = rqt_to_internet(url)
        special_printing(soup)
        file_name = process_filename(url)
        write_file(file_name, soup.text)
        stack.append(soup.text)
    else:
        print('Error: Incorrect URL')


