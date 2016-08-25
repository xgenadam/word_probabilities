sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

#
#   Maximum Likelihood Hypothesis
#
#
#   In this quiz we will find the maximum likelihood word based on the preceding word
#
#   Fill in the NextWordProbability procedure so that it takes in sample text and a word,
#   and returns a dictionary with keys the set of words that come after, whose values are
#   the number of times the key comes after that word.
#
#   Just use .split() to split the sample_memo text into words separated by spaces.


def format_text(text, remove_chars=('.', ',', '\"', '!', '?', '\n'), replacement_char=''):
    new_text = text.lower()
    for remove_char in remove_chars:
        new_text = new_text.replace(remove_char, replacement_char)
    return new_text


def offset_zip(l1, l2, offset=0):
    from itertools import chain
    return zip(l1, chain(l2[offset:], l2[:offset]))


def most_likely_next_word(sampletext, preceding_word):
    word_list = format_text(sampletext).split()
    word_dict = {succeding_word: {other_word:0 for other_word in word_list} for succeding_word in set(word_list)}
    for preceding_word_, successive_word in list(offset_zip(word_list, word_list, 1))[:-1]:
        word_dict[preceding_word_][successive_word] +=1

    return word_dict[preceding_word]


def num_next_words(sample_text):
    formated_text = format_text(sample_text).split()
    word_dict = {preceeding_word: {successive_word: 0 for successive_word in set(formated_text)} for preceeding_word in set(formated_text)}

    for preceeding_word, succeeding_word in offset_zip(formated_text, formated_text, 1):
        word_dict[preceeding_word][succeeding_word] += 1

    return word_dict


def next_word_probabilities_for_given_words(sampletext):
    num_next_word_dict = num_next_words(sampletext)
    probability_dict = {preceeding_word: {} for preceeding_word in set(format_text(sampletext).split())}
    for preceeding_word, successive_word_dict in num_next_word_dict.items():
        total_num_succeeding_words = sum(successive_word_dict.values())
        for successive_word, successive_word_count in successive_word_dict.items():
            try:
                probability_dict[preceeding_word][successive_word] = float(successive_word_count)/float(total_num_succeeding_words)
            except Exception as e:
                import pdb; pdb.set_trace()

    # for preceeding_word, successive_word_dict in probability_dict.items():
    #     if sum(successive_word_dict.values()) != 1.0:
    #         print preceeding_word, sum(successive_word_dict.values())

    return probability_dict
