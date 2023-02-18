# クラスに対する前処理後処理の実行

class TestExample():
    # 前処理最初に実行される
    @classmethod
    def setup_class(cls):
        print('setup_method')
    # 後処理最後に実行される
    @classmethod
    def teardown_class(cls):
        print('teardown_method')

    def test_example(self):
        print('hello world')

    def test_example2(self):
        print('pytest')