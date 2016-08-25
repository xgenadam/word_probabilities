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


def LaterWords(sample, word, distance):
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
        for preceeding_word, successive_word_dict in cumulative_succession_probabilites[x-1].items():
            for successive_word, probability_of_successive_word in successive_word_dict.items():
                absolute_prob = word_succession_probabilities[preceeding_word][successive_word]
                if absolute_prob > 0:
                    try:
                        # if x == 1:
                        #     print successive_word, probability_of_successive_word, preceeding_word, probability_of_successive_word * word_succession_probabilities[preceeding_word][successive_word]
                        probability_of_preceeding_word_given_successive_word = word_succession_probabilities[]
                        print preceeding_word, probability_of_preceeding_word_given_successive_word
                        next_prob[successive_word][preceeding_word] += (probability_of_successive_word * word_succession_probabilities[preceeding_word][successive_word])
                    except Exception as e:
                        import pdb; pdb.set_trace()

        cumulative_succession_probabilites.append(next_prob)
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    # for w, p in cumulative_succession_probabilites[-1][word].items():
    #     print w, p
    # import pdb; pdb.set_trace()

    most_likely_word = sorted(cumulative_succession_probabilites[-1][word].items(), key=lambda t: -t[1])[0][0]
    return most_likely_word


print LaterWords(sample_memo, "ahead", 2)