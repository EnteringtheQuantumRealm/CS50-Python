from twttr import shorten


def test_assert():
    assert shorten("Whenever you don't know someone") == "Whnvr y dn't knw smn"
    assert shorten("and you overhear their problems") == "nd y vrhr thr prblms"
    assert shorten("they always sound so trivial.") == "thy lwys snd s trvl."
    assert shorten("HELLO 001!") == "HLL 001!"