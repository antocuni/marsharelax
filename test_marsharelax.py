import marsharelax
import marshal

def check(T, initval):
    class A(T):
        pass
    x = A(initval)
    s = marsharelax.dumps(x)
    y = marshal.loads(s)
    z = marsharelax.loads(s)
    assert y == z == initval
    assert type(y) is type(z) is T
    

def test_dump_subclasses():
    check(int, 42)
    check(long, 42)
    check(float, 42.0)
    check(complex, (42 + 42j))
    check(str, 'hello')
    check(unicode, u'hello')
    check(tuple, (1, 2, 3))
    check(list, [1, 2, 3])
    check(dict, dict(a=1, b=2, c=3))
    check(set, set([1, 2, 3]))
