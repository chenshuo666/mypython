import random

import time


class Account(object):
    num_accounts=0
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        Account.num_accounts+=1
    def __del__(self):
        Account.num_accounts-=1
    def despoist(self,amt):
        self.balance=self.balance+amt
        return self.balance
    def withdraw(self,amt):
        self.balance=self.balance-amt
        return self.balance
    def inquiry(self):
        return self.balance


class EvilAccount(Account):
    def __init__(self,name,balance,evilfactor):
        Account.__init__(self,name,balance)
        self.evilfactor=evilfactor
    def inquiry(self):
        if random.randint(0,4)==1:
            return self.balance*self.evilfactor
        else:
            return self.balance

class MoreEvilAccount(EvilAccount):
    def despoist(self,amount):
        self.withdraw(6)
        super().despoist(amount)#返回一个特殊对象，该对象支持在基类上执行属性查找
        return self.balance

class DepositCharge(Account):
    fee=5
    def deposit_fee(self):
        self.withdraw(self.fee)
        return self.balance

class WithdrawChagde(Account):
    fee=2.5
    def Withdraw_fee(self):
        self.withdraw(self.fee)
        return self.balance


class MostEvilAccount(EvilAccount,DepositCharge,WithdrawChagde):
    def despoist(self,amt):
        self.deposit_fee()
        super().despoist(amt)
        return self.balance

    def withdraw(self,amt):
        self.Withdraw_fee()
        super().withdraw(amt)
        return self.balance

a=MoreEvilAccount("lala",1000,0.4)
print(a.despoist(1000))

b=DepositCharge("as",10000)
print(b.deposit_fee())
# print(b.Withdraw_fee())

class data(object):
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
        print(self.year,self.month,self.day)
    @staticmethod
    def now():
        t=time.localtime()
        return data(t.tm_year,t.tm_mon,t.tm_day)

i=data(1923,4,2)
print(i.day)
# print(data.now())