import random
import requests
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"


class Random_Words():
    response = requests.get(word_site)
    words = response.content.splitlines()
    random_word = random.choice(words)
