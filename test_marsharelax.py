import marsharelax
import marshal

def test_dump_subclasses():
    class A(int):
        pass
    x = A(42)
    s = marsharelax.dumps(x)
    y = marshal.loads(s)
    assert y == 42
    assert type(y) is int
