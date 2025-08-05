def num_words():
    text = get_book_text()
    return len(text.split())

print(f"{num_words()} words found in the document.")


