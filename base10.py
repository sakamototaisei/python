# メタクラス：クラスの再定義をするクラスというふうに考えれば良い
# 主にその定義で良いのかクラスの検証する際に使用する

class MetaException(Exception):
  pass


class Meta1(type): # type(デフォルトのメタクラス)

  def __new__(metacls, name, bases, class_dict):
    print('metacls = {}'.format(metacls))
    print('name = {}'.format(name))
    print('bases = {}'.format(bases))
    print('class_dict = {}'.format(class_dict))

    # if 'my_var' not in class_dict.keys():
    #   raise MetaException('my_varを定義して下さい')

    for base in bases: # 継承しているクラス
      if isinstance(base, Meta1):
        raise MetaException('継承できません') # finalクラス


    return super().__new__(metacls, name, bases, class_dict)


class ClassA(metaclass=Meta1):
  a = '123'
  my_var = 'AAA'
  pass

class SubClassA(ClassA):
  pass
