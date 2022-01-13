import random
import pickle


BEGIN = '__BEGIN__'
END = '__END__'


def generate_text(first_words, first_weights, markov_dict):
    """入力された辞書型データをもとに文章を生成する"""
    # 最初の単語を取得
    first_word = random.choices(first_words, weights=first_weights)[0]
    # 文章生成用の単語を格納するリスト
    generate_words = [BEGIN, first_word]
    while True:
        # 最後の二つを取得
        pair = tuple(generate_words[-2:])
        # 次の単語と重みのリストを取得
        words = markov_dict[pair]['words']
        weights = markov_dict[pair]['weights']
        # 次の単語を取得
        next_word = random.choices(words, weights=weights)[0]
        # 文章が終了した場合はループを抜ける
        if next_word == END:
            break
        generate_words.append(next_word)

    return ''.join(generate_words[1:])


def markov_command():
    """マルコフ連鎖用の各種データを読み込み、文章を生成する"""
    # ファイルをバイナリ読み込みモードで開く
    with open('markov-dict.pickle', 'rb') as f:
        # ファイルからデータを再構成
        first_words, first_weights, markov_dict = print(pickle.load(f))

        return generate_text(first_words, first_weights, markov_dict)
