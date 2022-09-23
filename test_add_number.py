from add_number import add_number_max

def test_add_num_make_max():
    assert add_number_max(128) == 5128
    assert add_number_max(-128) == -1258