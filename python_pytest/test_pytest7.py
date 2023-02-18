# モジュールに対する前処理後処理

# 前処理
def setup_module(module):
    print('setup_module')
# 後処理
def teardown_module(module):
    print('teardown_module')

def test_hello_world():
    print('hello world')

def test_pytest():
    print('pytest')

class TestExample():
    def test_hello_world(self):
        print('hello world')

    def test_pytest(self):
        print('pytest')