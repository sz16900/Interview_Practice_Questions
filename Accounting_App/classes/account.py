from functools import total_ordering

@total_ordering
class Account:

    def __init__(self, owner, amount=0):

        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __str__(self):
        return "Account of %s with starting amount: %s" % (
            self.owner, self.amount)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        else:
            self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)


    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance
