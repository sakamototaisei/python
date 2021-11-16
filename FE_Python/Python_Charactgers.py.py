"""
キャラクターを作成してバトルさせるapp

Characterクラスを作成し、インスタンス変数としてname, hp, offence, defenseを持たせる

attackメソッドを実行すると、敵インスタンスのHPが自分のoffence - 敵のdefence分減る
(自分のoffence - 敵のdefenceがマイナスの場合は1)

critical_hitメソッドを実行すると、attackメソッドの倍ダメージを与える

HPが0になると死んでしまい、攻撃ができなくなる

AllCharactersクラスを作成する、クラス変数が3個存在している
all_characters : 現在作成されているすべてのキャラクターの配列
alive_characters : 現在生きているすべてのキャラクターの配列
dead_characters : 現在死んでいるすべてのキャラクターの配列
文字同じキャラクターを登録した場合は、CharacterAlreadyExistExceptionを作成いて返す

"""

class CharacterAlreadyExistException(Exception):
    pass

class AllCharacters(object):

    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターは既に存在しています')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)


class Character(object):

    def __init__(self, name, hp, offense, defense):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense =defense

    def attack(self, enemy, critical_point=1):
        if self.hp <= 0:
            print('キャラクターは既に死んでいます')
            return
        attack_point = self.offense - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)

    def critical_hit(self, enemy):
        self.attack(enemy, 2)


character_a = Character('A', 10, 5, 3)
character_b = Character('B', 8, 6, 2)


print('-----------------------------')
print('生きているキャラクター = {}'.format(AllCharacters.alive_characters))
print('死んでいるキャラクター = {}'.format(AllCharacters.dead_characters))
print('-----------------------------')

print('現在のBのhp = {}'.format(character_b.hp))
character_a.critical_hit(character_b)

print('攻撃を受けた後のBのhp = {}'.format(character_b.hp))

character_a.attack(character_b)

print('攻撃を受けた後のBのhp = {}'.format(character_b.hp))

print('-----------------------------')
print('生きているキャラクター = {}'.format(AllCharacters.alive_characters))
print('死んでいるキャラクター = {}'.format(AllCharacters.dead_characters))
print('-----------------------------')

character_b.attack(character_a)

character_c = Character('A', 10, 4, 3)