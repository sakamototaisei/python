"""
キャラクターを作成して戦わせる

Characterクラスを作成し、インスタンス変数として
name, hp, offence, defenseを持たせます。

attackメソッドを実行すると、敵インスタンスHPが自分のoffence-敵のdefense分減ります。
(自分のoffense-敵のdefenceがマイナスの場合は1)

critical_hitメソッドを実行すると、attackメソッドの倍のダメージを与えます。

HPが０になると死んでしまい、攻撃ができなくなります。

AllCharactersクラスを作成します。クラス変数が3個存在します
all_characters :  現在作成されている全てのキャラクターの配列
alive_characters : 現在生きている全てのキャラクターの配列
dead_characters : 現在死んでいる全てのキャラクターの配列を表します

もし同じ名前のキャラクターを登録したときは、CharacterAlreadyExistExceptionを作成して返してください
"""
# 例外
class CharacterAlreadyExistException(Exception):
    pass


class AllCharacters(object):
    """
    現在生きているキャラ、死んでいるキャラ、全キャラの表示
    hpに応じてリスト間の移動を行う。
    同じ名前のキャラの作成を許さない。エラーを返す
    """
    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('その名前のキャラクターは既に存在しています')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)


class Character(object):
    """
    キャラの作成ステータスの決定
    攻撃を行いhpを削る
    """

    def __init__(self, name, hp, offence, defense):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defense = defense

    def attack(self, enemy, critical_point=1):
        if enemy.hp <= 0:
            print('攻撃相手のキャラクターはすでに死んでいます')
            return
        elif self.hp <= 0:
            print('自身はすでに死んでいるんので攻撃はできません')
            return
        attack_point = self.offence - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)

    def critical_hit(self, enemy):
        self.attack(enemy, 2)


print('全キャラ = {}'.format(AllCharacters.all_characters))
character_x = Character('sakatai', 10, 8, 2)
print('全キャラ = {}'.format(AllCharacters.all_characters))
# # 同じ名前のキャラを作成しようとするとエラーを返す
# character_z = Character('sakatai', 10, 10, 10)