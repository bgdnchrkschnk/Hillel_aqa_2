def normalize(text):
    return text.strip().lower()

def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())