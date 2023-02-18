# 前処理&後処理のメソッドの作成

class TestExample():
    # 前処理メソッド
    def setup_method(self, method):
        print('setup_method')
    # 後処理メソッド
    def teardown_method(self, method):
        print('teardown_method')

    def test_example(self):
        print('hello world')

    def test_example2(self):
        print('pytest')