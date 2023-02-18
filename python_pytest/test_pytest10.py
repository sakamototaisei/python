import pytest

@pytest.fixture()
# 前処理
def setup_processing(request):
    print('前処理:setup_processing')
    # 後処理
    def teardown_processing():
        print('後処理:teardown_processing')
    request.addfinalizer(teardown_processing)

# 前処理後処理メソッドの作成
class TestExample():

    def test_hello(self, setup_processing):
        print('hello')

    def test_goodmorning(self):
        print('goodmorning')

    def test_goodafternoon(self, setup_processing):
        print('goodafternoon')
