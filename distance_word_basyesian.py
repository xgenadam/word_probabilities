# ------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be ---
'''


words_to_guess = ["ahead", "could"]


# TODO: check this
def PriorWords(sample, word, distance):
    from max_likelihood import next_word_probabilities_for_given_words
    '''
    @param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''

    word_succession_probabilities = next_word_probabilities_for_given_words(sample)

    cumulative_succession_probabilites = [word_succession_probabilities]
    for x in xrange(1, distance + 1):
        next_prob = {preceeding_word: {succeeding_word: 0.0 for succeeding_word in word_succession_probabilities.keys()}
                     for preceeding_word in word_succession_probabilities.keys()}
        for first_word in word_succession_probabilities.keys():
            for preceeding_word, preceeding_word_probability in cumulative_succession_probabilites[-1][first_word].items():
                for successive_word, successive_word_probability_dict in word_succession_probabilities.items():
                    next_prob[first_word][successive_word] += preceeding_word_probability * successive_word_probability_dict[preceeding_word]

        cumulative_succession_probabilites.append(next_prob)

    most_likely_word = sorted(cumulative_succession_probabilites[-1][word].items(), key=lambda t: -t[1])[0][0]
    return most_likely_word


def generate_successive_word_probabilities(sample, distance):
    from max_likelihood import next_word_probabilities_for_given_words
    '''
    @param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''

    word_succession_probabilities = next_word_probabilities_for_given_words(sample)

    cumulative_succession_probabilites = [word_succession_probabilities]
    for x in xrange(1, distance):
        next_prob = {preceeding_word: {succeeding_word: 0.0 for succeeding_word in word_succession_probabilities.keys()}
                     for preceeding_word in word_succession_probabilities.keys()}
        for first_word in word_succession_probabilities.keys():
            for preceeding_word in cumulative_succession_probabilites[-1][first_word].keys():
                for successive_word in word_succession_probabilities.keys():
                    next_prob[first_word][successive_word] += cumulative_succession_probabilites[-1][first_word][preceeding_word] * word_succession_probabilities[preceeding_word][successive_word]

        cumulative_succession_probabilites.append(next_prob)
    # import pdb; pdb.set_trace()
    return cumulative_succession_probabilites


def LaterWords(sample_text, word, distance):
    return sorted(generate_successive_word_probabilities(sample_text, distance)[-1][word].items(), key= lambda t: -t[1])[0][0]

if __name__ == '__main__':
    print LaterWords(sample_memo, "terrific", 1)