def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words = sentence.split()
    rev_words = []
    for word in words:
        rev_word = ""
        for w in word:
            if w.isupper():
                w = w.lower()
            else:
                w = w.upper()
            rev_word += w
        rev_words.append(rev_word)
    rev_sentence = " ".join(rev_words[::-1])
    print(rev_sentence)
    return rev_sentence


reverse_words_order_and_swap_cases("aWESOME is cODING")
