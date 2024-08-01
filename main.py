def main ():
    book_source = "Frankenstein"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        word_count = count_words(file_contents)
        #word_dict(file_contents)
        processed_dict = report_gen(file_contents)
        processed_dict.sort(reverse=True, key=sort_gen)
        print(f"Beginning report of {book_source}")
        print("-----------------------------------------")
        print(f"Total amount of words: {word_count}")
        print("------------------------------------------")
        for letter in processed_dict:
            print(f"found letter {letter['letter']}, an amount of {letter['amount']} of times")
        print("------End of Report-----------------------")


def count_words(book_file):  #counts the words of the book file
    words = book_file.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def word_dict(book_file): #generates the dictionary of letters in lowercase
    alphabet_dict = {}
    words_lowered = book_file.lower()
    words = words_lowered.split()
    for word in words:
        for char in word:
            if char not in alphabet_dict and char.isalpha():
                alphabet_dict[char] = 1
            elif char.isalpha():
                alphabet_dict[char] += 1
    return alphabet_dict

    
def report_gen(book_file): #generates a list of a dictionary from the original dictionary
    generator_letters = word_dict(book_file)
    list_gen = [{'letter': letter, 'amount': amount} for letter, amount in generator_letters.items()]
    return list_gen

def sort_gen(dict): #sorts the generator with occurrences
    return dict["amount"]

main()
