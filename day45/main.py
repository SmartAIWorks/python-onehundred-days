from bs4 import BeautifulSoup

import requests

def main():
    # with open('website.html') as file:
    #     content = file.read()

    # soup = BeautifulSoup(content, "html.parser")
    # print(soup.title.get_text() if soup.title else '')

    # print(soup.p.get_text() if soup.p else '')

    # print(soup.find_all(name = 'a'))


   # url = soup.select_one('p a')

    # print(soup.a)

    url = 'https://news.ycombinator.com/news'

    response = requests.get(url=url)

    #print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')

    story_links = soup.select('.titleline > a')

    for link in story_links:
        print(f'* {link.string} -  {link.get('href')}')


if __name__ == '__main__':
    main()