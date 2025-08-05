from stats import get_num_words

# Write get_book_text function.
def get_book_text():
    # It uses the relative path to frankenstein.tx
    relative_path = "/books/frankenstein.txt"
    # Opens the file and reads the contents
    with open(relative_path) as f:
        file_contents = f.read()
    #return the content
    return(file_contents)
#call and print the method
print(get_book_text())


