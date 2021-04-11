import numpy as np
import sys

# these are reading the txt files and appropriately creating
# lists for each type of word

adverbs = []
fileAdverbs = open('6K adverbs.txt', 'r')
dAdverbs = fileAdverbs.read()
lines = dAdverbs.split('\n')
for i in lines:
    adverbs.append(i)

verbs = []
fileVerbs = open('31K verbs.txt', 'r')
dVerbs = fileVerbs.read()
lines = dVerbs.split('\n')
for i in lines:
    verbs.append(i)

nouns = []
fileNouns = open('91K nouns.txt', 'r')
dNouns = fileNouns.read()
lines = dNouns.split('\n')
for i in lines:
    nouns.append(i)

adjectives = []
fileAdjectives = open('28K adjectives.txt', 'r')
dAdjectives = fileAdjectives.read()
lines = dAdjectives.split('\n')
for i in lines:
    adjectives.append(i)

# these are some lists used in the generation process

# each standard sentence begins with an article. If the second word
# starts with a vowel, then articles_2 is selected

# the sentence_selector_list stores the acceptable answers for
# selecting a sentence type

vowels = ['a', 'e', 'i', 'o', 'u']

articles_1 = ['The', 'A']

articles_2 = ['The', 'An']

sentence_selector_list = ['standard']

affirmative = ['Y', 'y', 'Yes', 'yes', 'Yes.', 'yes.', 'yup', 'Yeah', 'yeah']
negative = ['n', 'N', 'no', 'No', 'No.', 'no.', 'Nope', 'nope']

# this function randomly selects a word from a given word list

def word_selector(words):
    n = int(np.random.randint(len(words), size=1))
    word = words[n]
    return (word)

# the function below generates a standard sentence

# the whole thing repeats as many times as h is set to.
# the 'standard' structure is simple: Pick and print a random article,
# then a random adjective, then noun, then adverb, then verb, then noun again.
# This series is stored in a list and then each element is individually printed
# with hard coded linebreaks, spacings, and punctuation.

# there are two variables that complicate things. Depending on the first word (always an adjective)
# beginning with a vowel or not determines which articles can be used. The other issue is that
# the list of verbs I use are not correctly conjugated. I've implemented quick and easy fixes for these
# issues, which can probably be optimised in the future.

# at each iteration of the overall loop, the adjective and verb is generated first. Then there
# are there is an if/else statement, with another if/else statement nested in each answer.
# the code asks if the adjective begins with a vowel (by converting it to lowercase and
# checking against the vowels list). If yes, then it uses the second set of articles. It also
# asks if the verb ends with the letter 'e'. If yes, then it adds the letter 's' to the
# end of it. Simples. Otherwise it isn't altered. The same if/else statement is executed if
# the adjective does not start with a vowel, in which case the first set of articles is used.

# in all cases, after these checks the word_positions list is created,
# which generates the rest of the words and puts them in the correct order.
# each word is then printed out with the added details and punctuation mentioned above.

def standard_sentence(amount):
    for h in range(amount):
        word = []
        adjective = word_selector(adjectives)
        verb = word_selector(verbs)
        if adjective[0].lower() in vowels:
            if verb.endswith('e') == True:
                word_positions = [word_selector(articles_1), adjective, word_selector(nouns), word_selector(adverbs), verb, word_selector(nouns)]
                for i in word_positions:
                    word.append(i)
                print('\n' + word[0] + ' ' + word[1] + ' ' + word[2] + ' ' + word[3] + ' ' + word[4] + 's' + ' ' + word[5]
                      + '.' + ' ' + '\n')
            else:
                word_positions = [word_selector(articles_2), adjective, word_selector(nouns), word_selector(adverbs), verb, word_selector(nouns)]
                for i in word_positions:
                    word.append(i)
                print('\n' + word[0] + ' ' + word[1] + ' ' + word[2] + ' ' + word[3] + ' ' + word[
                    4] + ' ' + word[5] + '.' + ' ' + '\n')
        else:
            if verb.endswith('e') == True:
                word_positions = [word_selector(articles_2), adjective, word_selector(nouns), word_selector(adverbs), verb, word_selector(nouns)]
                for i in word_positions:
                    word.append(i)
                print('\n' + word[0] + ' ' + word[1] + ' ' + word[2] + ' ' + word[3] + ' ' + word[
                    4] + 's' + ' ' + word[5] + '.' + ' ' + '\n')
            else:

                word_positions = [word_selector(articles_1), adjective, word_selector(nouns), word_selector(adverbs), verb, word_selector(nouns)]
                for i in word_positions:
                    word.append(i)
                print('\n' + word[0] + ' ' + word[1] + ' ' + word[2] + ' ' + word[3] + ' ' + word[
                    4] + ' ' + word[5] + '.' + '\n')

# this function asks the user which sentence type they want to generate.
# the only type right now is the 'standard' type outlined above,
# and so that's the only valid answer. The valid answers are stored
# in the sentence_selector_list defined higher up.

# any further information needed to generate a sentence type is also coded in this function.
# Right now it just asks how many sentences you want of the standard type, which must be answered
# as an integer.

def sentence_type(item):
    while item not in sentence_selector_list:
        item = input('Whoops, no can do. Come again? ')
    if item == sentence_selector_list[0]:
        amount = input('How many sentences? ')
        if amount.isdigit() == True:
            amount = int(amount)
        integer_test = isinstance(amount, int)
        while integer_test == False:
            amount = input('Please type an integer. ')
            if amount.isdigit() == True:
                amount = int(amount)
            integer_test = isinstance(amount, int)
        standard_sentence(int(amount))

# little easter egg

def easter_egg():
    quote_odds = np.random.randint(6, size=1)

    if quote_odds == 5:

        return print(
            '#####################################\nLanguage is a virus from outer space.\n - William Burroughs\n'
            '#####################################')


# Finally, the answer to the following question kicks off the code.

type = input('Howdy! Please select a thing to generate from the following list:\n'
      ' - A standard sentence (type "standard").\n - [XXXX]\n - [XXXX]\n')

sentence_type(type)
easter_egg()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# this loop governs whether the code repeats or not

while True:
    repeat_code = input('\nWould you like like to generate more?\n ')
    if repeat_code in affirmative:
        type = input('\nPlease select a thing to generate from the following list:\n'
      ' - A standard sentence (type "standard").\n - [XXXX]\n - [XXXX]\n')
        sentence_type(type)
        easter_egg()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        continue
    elif repeat_code in negative:
        print('\nFair, goodbye.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        sys.exit()
    else:
        print('Sorry, didn\'t catch that.')
        continue
