# 抽象クラス
# 多様はしない方が良い会社や開発者の意向に合わせる
import abc


class Person(metaclass=abc.ABCMeta):
	def __init__(self, age=1):
		self.age = age

	# 必ず継承してくださいとなる。必ず実装してほしいファンクションを定義できる
	@abc.abstractmethod
	def drive(self):
		pass


class Baby(Person):
	def __init__(self, age=1):
		if age < 18:
			super().__init__(age)
		else:
			raise ValueError

	def drive(self):
		raise Exception('No drive')


class Adult(Person):
	def __init__(self, age=18):
		if age >= 18:
			super().__init__(age)
		else:
			raise ValueError

	def drive(self):
		print('Ok')

baby = Baby()
# baby.drive()

# driveを定義していないとエラーになる
adult = Adult()
# adult.drive()

print('--------------------')


# ---------------------------------------------------------------
