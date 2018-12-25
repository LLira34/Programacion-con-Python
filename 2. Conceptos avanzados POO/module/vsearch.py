# vsearch.py

def search4vowels(text:str) -> set:
    vowels = set("aeiou")
    return set(text).intersection(vowels)

def search4letters(msg:str, letters:str) -> set:
    return set(msg).intersection(set(letters))
