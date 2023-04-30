

def count_words(text):
    """
    take text with a lot of words , and return the word with the length of the word.

            :param str text: the text we work on
            :return: dictionary of all words : the length of the word
            :rtype: dictionary
    """
    words = ''.join([char for char in text.lower() if char.isalpha() or char == " "])  # take only the lower letters
    final_result = {word: len(word) for word in words.split()}  # create a new dictionary
    return final_result


def main():
    """ test the function count_words"""

    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    expected_result = {'you': 3, 'see': 3, 'wire': 4, 'telegraph': 9, 'is': 2, 'a': 1, 'kind': 4, 'of': 2, 'very': 4,
                       'long': 4, 'cat': 3, 'pull': 4, 'his': 3, 'tail': 4, 'in': 2, 'new': 3, 'york': 4, 'and': 3,
                       'head': 4, 'meowing': 7, 'los': 3, 'angeles': 7, 'do': 2, 'understand': 10, 'this': 4,
                       'radio': 5, 'operates': 8, 'exactly': 7, 'the': 3, 'same': 4, 'way': 3, 'send': 4, 'signals': 7,
                       'here': 4, 'they': 4, 'receive': 7, 'them': 4, 'there': 5, 'only': 4, 'difference': 10,
                       'that': 4, 'no': 2}

    assert count_words(text) == expected_result


if __name__ == '__main__':
    main()
