from classes.account import Account
import pytest

class TestClass(object):
    def test_one(self):
        acc = Account('bob', 10)
        assert 'Account of bob with starting amount: 10' in str(acc)
        acc2 = Account('tom', 40)
        assert 'Account of tom with starting amount: 40' in str(acc2)
        acc.add_transaction(20)
        acc.add_transaction(-10)
        acc.add_transaction(50)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        assert acc.balance == 80
        assert len(acc) == 5
        assert acc[1] == -10
        assert list(reversed(acc)) == [30, -20, 50, -10, 20]
        acc2 = Account('tim', 100)
        acc2.add_transaction(20)
        acc2.add_transaction(40)
        acc2.balance
        assert acc2 > acc
        assert not acc2 < acc
        assert not acc == acc2
