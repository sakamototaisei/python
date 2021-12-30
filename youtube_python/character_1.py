class CharacterAlreadyExistException(Exception):
    pass


class AllCharacters(object):

    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('そのキャラの名前は存在しています')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls, name):
        cls.alive_characters.remove(name)
        cls.dead_characters.append(name)


class Character(object):

    def __init__(self, name, hp, offence, defense):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defense = defense

    def attack(self, enemy, critical_point=1):
        if enemy.hp <= 0:
            print('攻撃相手のキャラはすでにダウンしています')
            return
        elif self.hp <= 0:
            print('自信はダウンしているので攻撃できません')
            return
        attack_point = self.offence - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)

    def critical_hit(self, enemy):
        self.attack(enemy, 2)


character_sakatai = Character('sakatai', 10, 7, 3)
character_masatika = Character('masatika', 10, 5, 5)

print(AllCharacters.all_characters)

character_sakatai.attack(character_masatika)
print(character_masatika.hp)
character_sakatai.critical_hit(character_masatika)
character_sakatai.critical_hit(character_masatika)
print(character_masatika.hp)

print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)

character_a = Character('sakatai', 10, 3, 4)