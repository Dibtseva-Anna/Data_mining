# for files
import pandas as pd
# for work with regular expressions
import re
# wordlist of stopwords
from nltk.corpus import stopwords
# for stemming
from nltk.stem import PorterStemmer
# for diagrams
from matplotlib import pyplot as plt


def print_arr(data_arr):
    for row in data_arr:
        print(row)


# if wordlist have the word in its keys it add 1 to counter (to it value)
# if doesn't it add this word to keys with value 1
def add_word_to_wordlist(item, wordlist):
    if item in wordlist:
        wordlist[word] += 1
        return
    wordlist[word] = 1


# write to csv file
def write_to_csv(information, filename):
    data_frame = pd.DataFrame(data={'words': information.keys(), 'count': information.values()})
    data_frame.to_csv(filename, index=False)


sample = pd.read_csv("sms-spam-corpus.csv", encoding='1251')
data = sample.v2
# number, special signs and stop words deleting
stop_words = stopwords.words('English')
stemmer = PorterStemmer()
for i in range(len(data)):
    data[i] = re.sub(r'[^\w\s]|_|\d+', ' ', data[i])
    data[i] = data[i].lower()
    for word in data[i].split():
        if word in stop_words:
            data[i] = data[i].replace(f' {word} ', ' ')
            continue
        data[i] = data[i].replace(word, stemmer.stem(word))
    data[i] = re.sub(r'\s+', ' ', data[i])
# print_arr(data)

# dictionaries with counts for ham and spam words
group = sample.v1
# structure of ..._wordlist: key - word, value - number of such words
ham_wordlist = {}
spam_wordlist = {}
for i in range(len(data)):
    for word in data[i].split():
        if group[i] == 'ham':
            add_word_to_wordlist(word, ham_wordlist)
            continue
        if group[i] == 'spam':
            add_word_to_wordlist(word, spam_wordlist)

# writing to file
write_to_csv(ham_wordlist, 'output\\ham_wordlist.csv')
write_to_csv(spam_wordlist, 'output\\spam_wordlist.csv')

# print(ham_wordlist)
# print(spam_wordlist)


#######################################################################################################################
# build barchart with words' length and its frequency
def display_barchart_text_lengths_and_it_frequency(text_length_frequency, barchart_color):
    frequencies = text_length_frequency.values()
    max_frequency = max(frequencies)
    normalized_frequency = []
    for frequency in frequencies:
        normalized_frequency = normalized_frequency + [frequency / max_frequency]
    plt.bar(text_length_frequency.keys(), normalized_frequency, color=barchart_color, alpha=0.5)


# count the amount of words with each length in the wordlist
def count_word_length_in_wordlist(wordlist, lengths_list):
    for word in wordlist:
        word_length = len(word)
        if word_length in lengths_list:
            lengths_list[word_length] += 1
            continue
        lengths_list[word_length] = 1


# count average word length
def count_average_word_length(list_of_words_lengths_and_frequencies_dictionaries: list) -> float:
    wordcount = 1
    letter_count = 0
    for words_lengths_dict in list_of_words_lengths_and_frequencies_dictionaries:
        for number_of_letters in words_lengths_dict:
            number_of_words = words_lengths_dict[number_of_letters]
            letter_count = letter_count + number_of_letters*number_of_words
            wordcount = wordcount + number_of_words
    # for preventing division on 0 wordcount was initialized with 1, so now we need to decrease it by 1
    wordcount = wordcount - 1
    return letter_count / wordcount


# structure of ...__wordlist_length_frequency: key - length of word, value - number of words with such length
ham_wordlist_length_frequency = {}
spam_wordlist_length_frequency = {}
# counting words lengths in wordlist
count_word_length_in_wordlist(ham_wordlist, ham_wordlist_length_frequency)
count_word_length_in_wordlist(spam_wordlist, spam_wordlist_length_frequency)

# Display on the graphs of the distribution by word length for each category and the average word length.
display_barchart_text_lengths_and_it_frequency(ham_wordlist_length_frequency, 'blue')
display_barchart_text_lengths_and_it_frequency(spam_wordlist_length_frequency, 'lime')
plt.xlabel('word length')
plt.ylabel('count of words')
average_word_length = count_average_word_length([ham_wordlist_length_frequency, spam_wordlist_length_frequency])
plt.bar(average_word_length, 1, color='red', alpha=1, width=0.1)
plt.legend(['ham', 'spam', 'average length'])
plt.get_current_fig_manager().window.state('zoomed')
plt.show()


#######################################################################################################################
def add_mess_length_and_frequency_to_dict(mess, mess_dict):
    mess_length = len(mess)
    if mess_length in mess_dict:
        mess_dict[mess_length] += 1
        return
    mess_dict[mess_length] = 1


# structure of ..._messages_lengths_dict: key - lengths, value - count of such messages
ham_mess_lengths_and_frequency_dict = {}
spam_mess_lengths_and_frequency_dict = {}
for i in range(len(data)):
    if group[i] == 'ham':
        add_mess_length_and_frequency_to_dict(data[i], ham_mess_lengths_and_frequency_dict)
        continue
    if group[i] == 'spam':
        add_mess_length_and_frequency_to_dict(data[i], spam_mess_lengths_and_frequency_dict)

# print(ham_mess_lengths_and_frequency_dict)
# print(spam_mess_lengths_and_frequency_dict)


# count average message length
def count_average_message_length(list_of_messages_lengths_and_frequencies_dictionaries: list) -> float:
    number_of_letters = 0
    number_of_messages = 1
    for messages_lengths_and_frequencies_dict in list_of_messages_lengths_and_frequencies_dictionaries:
        for message_length in messages_lengths_and_frequencies_dict:
            message_frequency = messages_lengths_and_frequencies_dict[message_length]
            number_of_letters += message_length * message_frequency
            number_of_messages += message_frequency
    # for preventing division on 0 number_of_messages was initialized with 1, so now we need to decrease it by 1
    number_of_messages = number_of_messages - 1
    return number_of_letters / number_of_messages


# Display on the graphs of the distribution by messages length for each category and the average length of message.
display_barchart_text_lengths_and_it_frequency(ham_mess_lengths_and_frequency_dict, 'blue')
display_barchart_text_lengths_and_it_frequency(spam_mess_lengths_and_frequency_dict, 'lime')
plt.xlabel('message length')
plt.ylabel('count of messages')
average_mess_length = count_average_message_length([ham_mess_lengths_and_frequency_dict,
                                                    spam_mess_lengths_and_frequency_dict])
plt.bar(average_mess_length, 1, color='red', alpha=0.5)
plt.legend(['ham', 'spam', 'average length'])
plt.get_current_fig_manager().window.state('zoomed')
plt.show()


#######################################################################################################################
# Провести частотний аналіз появи слів для двох категорій.
# Вивести на графіках 20 слів, які зустрічаються найчастіше для кожної категорії окремо.


def get_most_common_words(words_frequencies_dict: dict, number_of_words: int) -> dict:
    frequencies_words_list = list(words_frequencies_dict.items())
    frequencies = sorted(frequencies_words_list, key=lambda cortege: cortege[1], reverse=True)
    res = {}
    i = 0
    for item in frequencies:
        res[item[0]] = item[1]
        i += 1
        if i >= number_of_words:
            break
    # print(res)
    return res


number_of_words = 20
# word : frequency
most_common_words_in_ham = get_most_common_words(ham_wordlist, number_of_words)
most_common_words_in_spam = get_most_common_words(spam_wordlist, number_of_words)


# build barchart with 20 the most common words and its frequency
def display_barchart_most_common_words_it_frequency(words_frequencies, barchart_color):
    frequencies = words_frequencies.values()
    max_frequency = max(frequencies)
    normalized_frequency = []
    for frequency in frequencies:
        normalized_frequency = normalized_frequency + [frequency / max_frequency]
    plt.bar(words_frequencies.keys(), normalized_frequency, color=barchart_color, alpha=0.5)


display_barchart_most_common_words_it_frequency(most_common_words_in_ham, 'blue')
plt.xlabel('words')
plt.ylabel('count of words')
plt.legend(['ham'])
plt.get_current_fig_manager().window.state('zoomed')
plt.show()

display_barchart_most_common_words_it_frequency(most_common_words_in_spam, 'lime')
plt.xlabel('words')
plt.ylabel('count of words')
plt.legend(['spam'])
plt.get_current_fig_manager().window.state('zoomed')
plt.show()

