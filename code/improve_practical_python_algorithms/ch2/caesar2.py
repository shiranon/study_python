# シーザー暗号をテストする関数
def test_encrypt_caesar():
    assert encrypt("CAT", 3) == "FDW"
    assert encrypt("LOVE", 3) == "ORYH"
    assert decrypt("FDW", 3) == "CAT"
    assert encrypt("cat", 3) == "fdw"
    assert encrypt("love", 3) == "oryh"
    assert decrypt("fdw", 3) == "cat"


def encrypt(str, key_no):
    result = ""
    for c in str:
        if "A" <= c <= "Z":
            base = ord("A")
            c = chr((ord(c) + key_no - base) % 26 + base)
        elif "a" <= c <= "z":
            base = ord("a")
            c = chr((ord(c) - base + key_no) % 26 + base)
        result += c
    return result


def decrypt(str, key_no):
    return encrypt(str, key_no * -1)
