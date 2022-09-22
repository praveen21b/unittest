from join import joins

def test_joins_single_items():
    assert joins([1],'')=='1'

def test_with_delimiter():
    assert joins([1,2,3],',') == '1,2,3'

def test_join_empty_string():
    assert joins([],',')==''
