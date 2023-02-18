# 前処理&後処理の関数の作成

# 前処理
def setup_function(function):
    print('setup_function')

# 後処理
def teardown_function(function):
    print('teardown')

def test_hello_world():
    print('hello world')

def test_pytest():
    print('pytest')