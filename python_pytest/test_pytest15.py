# テストのスキップ
import pytest

def test_hello():
    print('hello')

# @pytest.mark.グループ名　でグルーピングできる
@pytest.mark.morning
def test_goodmorning():
    print('good morning')

@pytest.mark.afternoon
def test_goodafternoon():
    print('good afternoon')