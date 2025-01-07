def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = sort_list(chars_dict)

    print("--- Begin report of ", path, " ---")
    print(num_words, "words found in the document.")  
    for dict in chars_list:
        print("The '" + dict["key"] + "' character was found " + str(dict["value"]) + " times.")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    text_lowered = text.lower()
    chars = {}
    for c in text_lowered:
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars

def sort_list(text):
    chars_list = []
    for char in text:
        new_dict = {}
        new_dict["key"] = char
        new_dict["value"] = text[char]
        chars_list.append(new_dict)

    def sort_on(dict):
        return dict["value"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

main()