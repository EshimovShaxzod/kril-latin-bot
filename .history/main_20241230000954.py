from  transliterate import to_cyrillic, to_latin


text = input("matn kiriting:")
if text.isascii():
    print(to_cyrillic(text))
else:
    print(to_latin(text))
