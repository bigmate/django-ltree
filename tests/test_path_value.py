import pytest

from django_ltree.fields import PathValue


def test_create():
    assert str(PathValue([1, 2, 3, 4, 5])) == '1.2.3.4.5'
    assert str(PathValue((1, 3, 5, 7))) == '1.3.5.7'
    assert str(PathValue('hello.world')) == 'hello.world'

    def generator():
        yield from '100 bottles of beer'.split(' ')

    assert str(PathValue(generator())) == '100.bottles.of.beer'

    with pytest.raises(ValueError):
        PathValue(4)


