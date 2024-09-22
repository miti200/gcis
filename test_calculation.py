"""this python consists of test cases 
for calculation.py"""

from calculation import add, subtract, multiple, division

def test_add():
    additionResult=add(4,3)
    assert additionResult==7

def test_subtract():
    subtractionResult= subtract(4,3)
    assert subtractionResult==1

def test_multiple():
    multipleResult= multiple(4,3)
    assert multipleResult==12


def test_division():
    divisionResult= division(4,3)
    assert divisionResult==2





