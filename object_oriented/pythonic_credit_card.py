"""
This codes originally comes from the
Data Structures and Algorithms in Python book by Goodrich et al.
Book's program does not utilize the property decorator and just
defines any attributes as protected which is quite unpythonic.
It also doesn't include any exception class.

I use this program to teach:
- How to define and throw an undefined error
- Using Property decorator, when we want to protect an attribute
- Overriding a method
"""


class LimitOverFlow(Exception):
    pass


class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, str) and len(customer.split()) > 1:
            self.__customer = customer
        else:
            raise ValueError("Enter both fisrt and last name correctly.")

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        if limit > 1000:
            raise LimitOverFlow("Limit cannot be more than $1000")
        else:
            self.__limit = limit

    def charge(self, price):
        if price + self.balance > self.__limit:
            return False
        else:
            self.balance += price
            print(f"carte moshtari {price} tooman sharj shod.")
            return True

    def make_payment(self, amount):
        self.balance -= amount
        print(f"moshtary {amount} tooman az bedehi khod ra pardaakht kard")

    def __str__(self):
        return "Name: {0:>14}\n" \
               "Account: {1:>11}\n" \
               "Limit: {2:>8}\n" \
               "Balance: {3:>4}\n"\
               .format(self.__customer, self.account, self.__limit, self.balance)


class CreditRate(CreditCard):
    def __init__(self, customer, bank, account, limit, rate):
        super().__init__(customer, bank, account, limit)
        self.rate = rate

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self.balance += 5
        return success

    def month_rate(self):
        if self.balance > 0:
            monthly_factor = pow(1 + self.rate, 1/12)
            self.balance *= monthly_factor


if __name__ == "__main__":
    account_1 = CreditRate("John Doe", "A Bank", 12345678, 900, 0.0825)
    print(account_1)

    # charging more than the defined limit will have penalty
    account_1.charge(1000)

    # 5$ with its monthly rate
    account_1.month_rate()
    print(account_1.balance)