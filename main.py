path_to_book = "books/frankenstein.txt"

def sort_on(dict):
    return dict["times"]

def getWordCount(path):
    with open(path) as f:
        words_list = f.read().split()
        return len(words_list)

def getLetterCount(path):
    letters_counted = {}
    with open(path) as f:
        for i in f.read().lower():
            if i in letters_counted.keys():
               letters_counted[i] += 1
            else:
               letters_counted[i] = 1
    return letters_counted

def printReport(word_count, letters_count):
    list_of_dicts = []
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for i in letters_count:
        if i.isalpha():
            list_of_dicts.append({"letter": i, "times": letters_count[i]})
            # print(f"The '{i} character was found {letters_count[i]} times")
    list_of_dicts.sort(key=sort_on, reverse=True)
    for i in list_of_dicts:
        print(f"The '{i["letter"]}' character was found {i["times"]} times.")
    print("--- End report ---")

def main():
    printReport(getWordCount(path_to_book), getLetterCount(path_to_book))

main()