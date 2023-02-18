# fixtureによるクラスの前処理後処理の代替
import pytest

# scopeはフィクスチャ関数が実行される粒度を指定
@pytest.fixture(scope='class')
# 前処理
def setup_processing(request):
    print('前処理:setup_processing')
    # 後処理
    def teardown_processing():
        print('後処理:teardown_processing')
    request.addfinalizer(teardown_processing)


# クラスに対する前処理後処理
class TestExample():
    def test_example1(self, setup_processing):
        print('hello world')

    def test_example2(self, setup_processing):
        print('pytest')