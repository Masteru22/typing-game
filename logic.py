def verify_if_correct(player_word, sentence):
    first_word = sentence.split(' ', 1)[0]
    return player_word.strip() == first_word.strip()

def remove_first_word(sentence, add_sentence_func):
    parts = sentence.split(' ', 1)
    if len(parts) > 1:
        new_sentence = parts[1].lstrip()
    else:
        new_sentence = add_sentence_func()
    if not new_sentence.strip():
        new_sentence = add_sentence_func()
    return new_sentence
