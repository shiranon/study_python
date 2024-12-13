# リングバッファを初期化
def ringBuffer_new(size):
    return {
        "head": 0,  # 先頭
        "tail": 0,  # 末尾
        "size": 0,  # サイズ
        "buffer": [0 for _ in range(size)],  # バッファ
    }


# リングバッファに値を追加
def ringBuffer_write(rb, v):
    # 書き込み
    rb["buffer"][rb["tail"]] = v
    # 次回書き込み先を後ろに移動
    rb["tail"] = (rb["tail"] + 1) % len(rb["buffer"])
    # バッファがいっぱいになったか
    if rb["size"] >= len(rb["buffer"]):
        rb["head"] = (rb["head"] + 1) % len(rb["buffer"])
    else:
        rb["size"] += 1


# リングバッファから値を取得
def ringBuffer_read(rb):
    if rb["size"] <= 0:
        return None
    v = rb["buffer"][rb["head"]]
    rb["size"] -= 1
    # 読み取り位置を後ろに移動
    rb["head"] = (rb["head"] + 1) % len(rb["buffer"])
    return v


# リングバッファのテスト
def test_ringBuffer1():
    # リングバッファを作成
    rb = ringBuffer_new(3)
    # リングバッファに追加
    ringBuffer_write(rb, 0)
    ringBuffer_write(rb, 1)
    ringBuffer_write(rb, 2)
    assert ringBuffer_read(rb) == 0
    assert ringBuffer_read(rb) == 1
    assert ringBuffer_read(rb) == 2


def test_ringBuffer2():
    rb = ringBuffer_new(3)
    # 1から100まで書き込む
    for i in range(1, 100 + 1):
        ringBuffer_write(rb, i)
    assert ringBuffer_read(rb) == 98
    assert ringBuffer_read(rb) == 99
    assert ringBuffer_read(rb) == 100
    assert ringBuffer_read(rb) is None
