# 列挙型クラス

from enum import Enum, auto

class Week(Enum):
  MONDAY = auto()
  TUESDAY = auto()
  WEDNESDAY = auto()
  THURSDAY = auto()
  FRIDAY = auto()
  SATURDAY = auto()
  SUNDAY = auto()

# week_today = Week.SATURDAY
# print(week_today)
print(Week.SUNDAY.name, Week.SUNDAY.value)
