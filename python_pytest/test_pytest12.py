# fixtureによるモジュールの前処理後処理の代替
import pytest

# scopeはフィクスチャ関数が実行される粒度を指定
@pytest.fixture(scope='module')
# 前処理
def setup_module(request):
    print('前処理:setup_module')
    # 後処理
    def teardown_module():
        print('後処理:teardown_module')
    request.addfinalizer(teardown_module)

@pytest.fixture(scope='function')
# 前処理
def setup_function(request):
    print('前処理:setup_function')
    # 後処理
    def teardown_function():
        print('後処理:teardown_function')
    request.addfinalizer(teardown_function)

def test_hello_world(setup_module, setup_function):
    print('hello world')

def test_pytest(setup_module):
    print('pytest')

class TestExample():
    def test_hello_world(self, setup_module):
        print('hello world')

    def test_pytest(self, setup_module):
        print('pytest')
