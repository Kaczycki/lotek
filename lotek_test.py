from lotek import WYNIKI_LOSOWANIA, losuj, zakres
assert len(set(losuj())) == 6
for _ in WYNIKI_LOSOWANIA:
    assert _ < zakres
