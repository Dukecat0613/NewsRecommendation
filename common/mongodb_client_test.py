# @Author: Dukecat
# @Date:   2017-05-02T23:27:09-04:00
# @Last modified by:   Dukecat
# @Last modified time: 2017-05-11T19:42:27-04:00





import mongodb_client as client

def test_basic():
    db = client.get_db('test')
    db.demo.drop()
    assert db.demo.count() == 0
    db.demo.insert({"test": 123})
    assert db.demo.count() == 1
    db.demo.drop()
    assert db.demo.count() == 0
    print 'test_basic passed!'

if __name__ == "__main__":
    test_basic()
