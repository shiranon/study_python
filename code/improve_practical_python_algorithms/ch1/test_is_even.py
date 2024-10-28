# pytestを使うにはtest_xxx.py形式でファイルを作成し、
# consoleでpytest ファイル名で実行する

# 2から5までをテスト
def test_is_even():
    assert is_even(2)
    assert not is_even(3)
    assert is_even(4)
    assert not is_even(5)


# 偶数判定用
def is_even(num):
    return num % 2 == 0
