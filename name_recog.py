import text_extract
import spacy
import transcript

def name_recog_func():

    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text_extract.text_extract_func())

    sentence_tokens = [sent for sent in doc.sents]
    #print(sentence_tokens)

    count = 1

    temp_list = []

    '''for i in sentence_tokens :
        if word in i.text :
            print(str(count) + ". " + i.text)
            count += 1
    '''

    word, _ = transcript.perform_magic()

    for i in sentence_tokens :
        if word in i.text :
            temp_list.append(i.text)

    return temp_list




