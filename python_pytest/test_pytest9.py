# fixtureの利用
import pytest

# # 前処理
# def setup_function(fnc):
#     print('setup_function')

# # 後処理
# def teardown_function(fnc):
#     print('teardown_function')

@pytest.fixture()
# 前処理
def setup_processing(request):
    print('前処理:setup_processing')
    # 後処理
    def teardown_processing():
        print('後処理:teardown_processing')
    request.addfinalizer(teardown_processing)

def test_hello(setup_processing):
    print('hello')

def test_goodmorning():
    print('goodmorning')

def test_goodafternoon(setup_processing):
    print('goodafternoon')
