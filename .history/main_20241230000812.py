from  transliterate import to_cyrillic, to_latin


def convert(text, from_variant, to_variant):
    if from_variant == 'cyrillic':
        text = to_latin(text)
    elif from_variant == 'latin':
        text = to_cyrillic(text)

    return text

