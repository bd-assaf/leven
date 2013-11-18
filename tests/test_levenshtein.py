from nose.tools import assert_equal, assert_raises

from leven import levenshtein
from six import b

S1 = b("kitten")
S2 = b("sitting")

U1 = S1.decode("utf-8")
U2 = S2.decode("utf-8")


def test_distance():
    assert_equal(levenshtein(S1, S2), 3)
    assert_equal(levenshtein(U1, U2), 3)


def test_types():
    assert_raises(TypeError, levenshtein, S1, U2)
    assert_raises(TypeError, levenshtein, U1, S2)