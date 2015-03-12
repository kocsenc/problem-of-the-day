# Kocsen Chung
# Sentence Finder

# PROBLEM
# Given the lipsum text create an array of all the sentences. Then with that data create a function that takes in
# a string and each sentence that contains that string. Partial word matches such as "sum" in the word "lipsum"
# still counts. Matching should also be case insensitive.

def main():
    """
    Gather sentences split up by . and stripped.
    Use pythons in to check for this
    """
    filename = "lorem.txt"

    sentences = []
    query = "lorem"

    with open(filename) as f:
       sentences = f.read().split(".")

    found_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if query.lower() in sentence.lower():
            found_sentences.append(sentence)


    print("Found Sentences with query " + query)
    print(found_sentences)

if __name__ == "__main__":
    main()
