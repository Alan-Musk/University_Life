"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # filter(function,iterable) 用法:iterable 中函数 function 返回真的那些元素，构建一个新的迭代器
    selectd = list(filter(select, paragraphs))
    if k < len(selectd):
        return selectd[k]
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def about_helper(s):
        s = split(remove_punctuation(lower(s)))  # 处理字符串
        for i in topic:
            if i in s:
                return True
        return False
    return about_helper
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
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # base_case
    if len(typed_words) == 0:
        return 0.0
    correct = 0
    for i in range(min(len(reference_words), len(typed_words))):
        if typed_words[i] == reference_words[i]:
            correct += 1

    return correct/len(typed_words)*100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / (elapsed/60)/5
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    diff_char = []  # 词容器
    for i in valid_words:
        diff_num = diff_function(user_word, i, limit)  # 两个单词的差异值
        if diff_num < limit:  # 若valid_words词组中比前一个单词 则缩小limit 并存入
            limit = diff_num
            diff_char = [i]
        elif diff_num == limit:
            diff_char += [i]
    # Q:为什么要判断 user_word in diff_char
    # A:参考
    """
    >>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
        'idea'
    """
    if len(diff_char) == 0 or user_word in diff_char:
        return user_word
    return diff_char[0]
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # assert False , 'Remove this line'
    # BEGIN PROBLEM 6
    if limit < 0:
        return 0
    elif start == '' or goal == '':
        return max(len(goal), len(start))
    else:
        if goal[0] != start[0]:
            return 1+shifty_shifts(start[1:], goal[1:], limit-1)
        else:
            return shifty_shifts(start[1:], goal[1:], limit)


    # END PROBLEM 6

def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'
    # 有三个base case:
    # 1. 一方为空,则只需要返回另一方的剩余字符数
    # 2. 两方首字符相同,不修改,不增数递进
    # 3. limit
    if start == '' or goal == '':  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return max(len(start), len(goal))
        # END
    # 如果字符相等,不计数递进
    elif start[0] == goal[0]:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        start = start[1:]
        goal = goal[1:]
        return pawssible_patches(start, goal, limit)
        # END
    elif limit < 0:
        return 0
    else:
        add_diff = pawssible_patches(start, goal[1:], limit-1)
        remove_diff = pawssible_patches(start[1:], goal, limit-1)
        substitute_diff = pawssible_patches(start[1:], goal[1:], limit-1)
        # BEGIN
        "*** YOUR CODE HERE ***"

        return 1+min(add_diff, remove_diff, substitute_diff)
        # END

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    total = 0
    for i, j in zip(typed, prompt):
        if i == j:
            total += 1
        else:
            break
    send({'id': user_id, 'progress': total/len(prompt)})
    return total/len(prompt)
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time = []
    for i in range(len(times_per_player)):
        temp = []
        for j in range(len(words)):  # 2
            temp.append(times_per_player[i][j+1]-times_per_player[i][j])
        time.append(temp)
    return game(words, time)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game))
                           )  # contains an *index* for each player
    # contains an *index* for each word
    word_indices = range(len(all_words(game)))
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"

    lst = [[] for _ in player_indices]
    for word_index in word_indices:
        word = word_at(game, word_index)
        time_lst = []
        for id in player_indices:
            time_lst += [time(game, id, word_index)]
        id_index = time_lst.index(min(time_lst))
        lst[id_index].append(word)
    return lst
    # END PROBLEM 10

# print(fastest_words((['What', 'great', 'luck'], [p0, p1])))


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]
               ), 'words should be a list of strings'
    assert all([type(t) == list for t in times]
               ), 'times should be a list of lists'
    assert all([isinstance(i, (int, float))
               for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]
               ), 'There should be one word per time.'
    return [words, times]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    def select(p): return True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
