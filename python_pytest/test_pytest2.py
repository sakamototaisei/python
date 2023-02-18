def test_calculate():
    result = 5 * 2
    assert result == 10

def test_len():
    text = 'My name is sakatai!.'
    assert len(text) == 20

def test_contain():
    text = 'My name is sakatai!.'
    assert 'tai' in text