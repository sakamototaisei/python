# テストのスキップ
import pytest

def test_hello():
    print('hello')

# 引数のreason='ここにスキップする理由を記載する')
@pytest.mark.skip(reason='write reason')
def test_goodmorning():
    print('good morning')

def test_goodafternoon():
    print('good afternoon')
