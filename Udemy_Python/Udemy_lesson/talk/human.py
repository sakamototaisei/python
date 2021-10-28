# このように絶対パスの方が良い
from Udemy_lesson import utils

# 相対パスでもかけるがあまり進められていない
# from .. import utils

def sing():
  return utils.say_twice('sing')

def cry():
  return utils.say_twice('cry')

