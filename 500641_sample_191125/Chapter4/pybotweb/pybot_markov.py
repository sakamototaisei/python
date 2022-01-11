import random
import pickle

BEGIN = '__BEGIN__'  # 文の開始マーク
END = '__END__'  # 文の終了マーク

def generate_text(first_words, first_weights, markov_dict):
    """入力された辞書データを元に文章を生成する"""
    first_word = random.choices(first_words, weights=first_weights)[0]
    generate_words = [BEGIN, first_word]
    while True:
        pair = tuple(generate_words[-2:])
        words = markov_dict[pair]['words']
        weights = markov_dict[pair]['weights']
        next_word = random.choices(words, weights=weights)[0]
        if next_word == END:
            break
        generate_words.append(next_word)

    return ''.join(generate_words[1:])

def markov_command():
    """マルコフ連鎖用の各種データを読み込み、文章を生成する"""
    with open('markov-dict.pickle', 'rb') as f:
        first_words, first_weights, markov_dict = pickle.load(f)

    return generate_text(first_words, first_weights, markov_dict)
