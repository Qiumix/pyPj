import string
import random


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    count = -1
    for i in paragraphs:
        if select(i):
            count += 1
            if count == k:
                return i
    return ""
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])€¼
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([x.lower == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def inner(Strings):
        Lists = (remove_punctuation(Strings.lower())).split()
        for i in topic:
            if i in Lists:
                return True
        return False

    return inner
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = typed.split()
    reference_words = reference.split()
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    total = len(typed_words)
    total2 = len(reference_words)
    iter = min(total, total2)
    count = 0
    if iter == 0:
        if typed == reference:
            return 100.0
        return 0.0
    for i in range(iter):
        if typed_words[i] == reference_words[i]:
            count += 1
    return count * 100 / total

    # END PROBLEM 3


punctuation_remover = str.maketrans('', '', string.punctuation)
KEY_LAYOUT = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
              ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]"],
              ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'"],
              ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"], [" "]]


def remove_punctuation(s):
    """Return a string with the same contents as s, but with punctuation removed.

    >>> remove_punctuation("It's a lovely day, don't you think?")
    'Its a lovely day dont you think'
    """
    return s.strip().translate(punctuation_remover)


def lines_from_file(path):
    """Return a list of strings, one for each line in a file."""
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


PARAGRAPH_PATH = "./data/sample_paragraphs.txt"
WORDS_LIST = lines_from_file('data/words.txt')
WORDS_SET = set(WORDS_LIST)
LETTER_SETS = [(w, set(w)) for w in WORDS_LIST]
SIMILARITY_LIMIT = 2


def analyze(prompted_text, typed_text, start_time, cur_time):
    """Return [wpm, accuracy]."""
    return {
        "wpm": len(typed_text) / 5 / ((cur_time - start_time) / 60),
        "accuracy": accuracy(typed_text, prompted_text)
    }


def request_paragraph(topics=None):
    """Return a random paragraph."""
    paragraphs = lines_from_file(PARAGRAPH_PATH)
    random.shuffle(paragraphs)
    select = about(topics) if topics else lambda x: True
    return choose(paragraphs, select, 0)


def similar(w, v, n):
    """Whether W intersect V contains at least |W|-N and |V|-N elements."""
    intersect = len(w.intersection(v))
    return intersect >= len(w) - n and intersect >= len(v) - n


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if goal == '' or start == '':  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return max(len(goal), len(start))
        # END
    elif start[0] == goal[0]:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return pawssible_patches(start[1:], goal[1:], limit)
        # END
    elif limit < 0:
        return 0
    else:
        add_diff = pawssible_patches(start[1:], goal,
                                     limit - 1)  # Fill in these lines
        remove_diff = pawssible_patches(start, goal[1:], limit - 1)
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit - 1)
        # BEGIN
        return 1 + min(add_diff, remove_diff, substitute_diff)
        "*** YOUR CODE HERE ***"
        # END


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if start == goal:
        return 0
    elif limit == 0:
        return max(len(start), len(goal))
    elif start == '' or goal == '':
        return max(len(goal), len(start))
    diff_t = 0 if start[0] == goal[0] else 1
    return diff_t + shifty_shifts(start[1:], goal[1:], limit - diff_t)


    # END PROBLEM 6
def reformat(word, raw_word):
    """Reformat WORD to match the capitalization and punctuation of RAW_WORD."""
    # handle capitalization
    if raw_word != "" and raw_word[0].isupper():
        word = word.capitalize()

    # find the boundaries of the raw word
    first = 0
    while first < len(raw_word) and raw_word[first] in string.punctuation:
        first += 1
    last = len(raw_word) - 1
    while last > first and raw_word[last] in string.punctuation:
        last -= 1

    # add wrapping punctuation to the word
    if raw_word != word:
        word = raw_word[:first] + word
        word = word + raw_word[last + 1:]

    return word


def autocorrect(word=""):
    """Call autocorrect using the best score function available."""
    raw_word = word
    word = remove_punctuation(raw_word).lower()
    if word in WORDS_SET or word == '':
        return raw_word

    # Heuristically choose candidate words to score.
    letters = set(word)
    candidates = [
        w for w, s in LETTER_SETS if similar(s, letters, SIMILARITY_LIMIT)
    ]

    # Try various diff functions until one doesn't raise an exception.
    for fn in [pawssible_patches, shifty_shifts]:
        try:
            guess = autocorrect(word, candidates, fn, SIMILARITY_LIMIT)
            return reformat(guess, raw_word)
        except BaseException:
            pass

    return raw_word
