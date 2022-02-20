from requests import get
import re


url = "https://gist.githubusercontent.com/Sathishzus/fe108a94f6bca6d8309ac132a059837b/raw/9bb0be78d77e1133b8c51edfb387bf3c8f244ed6/profanity.txt"


def get_words():
    return (get(url).text).split("\n")


def check_word(sentence):
    words = get_words()
    for i in sentence:
        for j in words:
            if i.lower() == j.lower():
                return j, True  # return the word 
    return None, False
