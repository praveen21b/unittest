
def test_1():
    # x,y = 10, 20
    x,y = 10, 10
    assert x == y

def test_2():
    name = 'selenium'
    title = ' selenium is for web automation'
    assert name in title

def test_3():
    name = 'selenium'
    title = ' Selenium is for web automation'
    assert name in title, 'Title does not match' # dispays only when it fails