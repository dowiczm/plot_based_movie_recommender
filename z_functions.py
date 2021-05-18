import spacy

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

nlp = spacy.load("en_core_web_lg")

#adding words to stopwords
add_to_stop_words = ['asks', 'says', 'know', 'ask', 'say', 'knows', 'tell', 'tells', 'way', 'portray', 'portrays', 'ways']
stopwords = list(STOP_WORDS)
for word in add_to_stop_words:
    stopwords.append(word)

#function extracts the 10 most common verbs and nouns from each collection of user_plots 
def extract(doc):
    key_words = []
    pos_tag = ['NOUN', 'VERB']

    for token in doc:
        if token.text in stopwords or token.text in punctuation:
            continue
        if token.pos_ in pos_tag:
            key_words.append(token.text)
            
    freq_word = Counter(key_words)
    freq_tups = freq_word.most_common(n=10)
    
    new_keywords = [word[0] for word in freq_tups]
    
    freq_string = ''
    for word in new_keywords:
        freq_string += word + ' ' 
    
    return freq_string




def full_extract(doc):
    keywords = []
    pos_tag = ['NOUN', 'VERB']

    #filter tokens
    for token in doc:
        if(token.text in stopwords or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keywords.append(token.text)
    
    freq_word = Counter(keywords)
    
    max_freq = Counter(keywords).most_common()[0][1]

    #normalizing 
    for word in freq_word.keys():
        freq_word[word] = (freq_word[word] / max_freq)
    
    
    
    sent_strength = {}

    #loop through sentences
    for sent in doc.sents:
    
        #loop through words in sentence
        for word in sent:
        
            #checking if word is in our frequent_words dict.
            if word.text in freq_word.keys():
            
            #adding freq_word value to sent value
                if sent in sent_strength.keys():
                    sent_strength[sent] += freq_word[word.text]
            
                else:
                    sent_strength[sent] = freq_word[word.text]
    
    
    summarized_sentences = nlargest(5, sent_strength, key=sent_strength.get)
    
    final_sentences = [w.text for w in summarized_sentences]
    
    final_summary = ' '.join(final_sentences)
    
    final_keys = extract(nlp(final_summary))
    
    return final_keys


    