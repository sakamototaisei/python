# fixtureのautouse設定
import pytest

# scopeはフィクスチャ関数が実行される粒度を指定
@pytest.fixture(autouse=True)
# 前処理
def setup_processing(request):
    print('前処理:setup_processing')
    # 後処理
    def teardown_processing():
        print('後処理:teardown_processing')
    request.addfinalizer(teardown_processing)

class TestExample():
    def test_hello_world(self):
        print('hello world')

    def test_pytest(self):
        print('pytest')
