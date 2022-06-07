import pytest
import pyhello as dh

def test_greet():
    assert dh.greet() == 'hello, world!'

