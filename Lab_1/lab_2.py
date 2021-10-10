import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import argparse


# number, special signs and stop words deleting
def filter_data(data: dict):
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
    return data


# number, special signs and stop words deleting
def filter_message(_message: str):
    stop_words = stopwords.words('English')
    stemmer = PorterStemmer()
    _message = re.sub(r'[^\w\s]|_|\d+', ' ', _message)
    _message = _message.lower()
    for _word in _message.split():
        if _word in stop_words:
            _message = _message.replace(f' {_word} ', ' ')
            continue
        _message = _message.replace(_word, stemmer.stem(_word))
    _message = re.sub(r'\s+', ' ', _message)
    return _message


def parse_args() -> (str, str):
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--message")
    args = parser.parse_args()
    _filename = args.file
    if _filename is None:
        _filename = 'sms-spam-corpus.csv'
    _message = args.message
    if _message is None:
        _message = 'URGENT! You have won a 1 week FREE membership in our еЈ100,000 Prize Jackpot! ' \
                   'Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18'
    return _filename, _message


# if wordlist have the word in its keys it add 1 to counter (to it value)
# if doesn't it add this word to keys with value 1
def add_word_to_wordlist(item, wordlist):
    if item in wordlist:
        wordlist[word] += 1
        return
    wordlist[word] = 1


filename, message = parse_args()
sample = pd.read_csv(filename, encoding='1251')
group = sample.v1
data = sample.v2
data = filter_data(data)
message = filter_message(message)

# dictionaries with counts for ham and spam words
# structure of ..._wordlist_word_number_list: key - word, value - number of such words
ham_word_number_list = {}
spam_word_number_list = {}
# numbers of messages in each group
number_of_ham_messages = 0
number_of_spam_messages = 0
# common numbers of words in groups
ham_common_number_of_words = 0
spam_common_number_of_words = 0
for i in range(len(data)):
    if group[i] == 'ham':
        number_of_ham_messages += 1
    else:
        if group[i] == 'spam':
            number_of_spam_messages += 1
    for word in data[i].split():
        if group[i] == 'ham':
            ham_common_number_of_words += 1
            add_word_to_wordlist(word, ham_word_number_list)
            continue
        if group[i] == 'spam':
            spam_common_number_of_words += 1
            add_word_to_wordlist(word, spam_word_number_list)
common_number_of_messages = number_of_ham_messages + number_of_spam_messages


def count_messages_coefficient(number_of_this_group_messages: int, _common_number_of_messages: int):
    return number_of_this_group_messages / _common_number_of_messages


def count_smoothing_laplace(_message, word_number_list: dict, group_words_number: int):
    number_of_unic_words = 0
    for _word in _message.split():
        if _word in word_number_list:
            continue
        number_of_unic_words += 1
    group_words_number += number_of_unic_words

    probability = 1
    for _word in _message.split():
        if _word in word_number_list:
            probability *= (word_number_list[_word] + 1) / group_words_number
        else:
            probability *= 1 / group_words_number
    return probability


def count_words_coefficient(_message, word_number_list: dict, group_words_number: int):
    probability = 1
    for _word in _message.split():
        if _word in word_number_list:
            probability *= word_number_list[_word] / group_words_number
        else:
            probability = count_smoothing_laplace(_message, word_number_list, group_words_number)
            break
    return probability


def count_n_b_a(_message, number_of_this_group_messages: int, _common_number_of_messages: int,
                word_number_list: dict, number_of_words_in_group: int):
    probability = count_messages_coefficient(number_of_this_group_messages, _common_number_of_messages) \
                  * count_words_coefficient(_message, word_number_list, number_of_words_in_group)
    return probability


ham_n_b_a = count_n_b_a(message, number_of_ham_messages, common_number_of_messages, ham_word_number_list,
            ham_common_number_of_words)
spam_n_b_a = count_n_b_a(message, number_of_spam_messages, common_number_of_messages, spam_word_number_list,
            spam_common_number_of_words)
normalized_ham_n_b_a = ham_n_b_a / (ham_n_b_a + spam_n_b_a)
normalized_spam_n_b_a = spam_n_b_a / (ham_n_b_a + spam_n_b_a)
print(round(normalized_ham_n_b_a, 4))
print(round(normalized_spam_n_b_a, 4))


