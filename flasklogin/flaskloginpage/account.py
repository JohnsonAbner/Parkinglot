#!/usr/bin/python
# -*- coding: UTF-8 -*-


def displayCstNum():
    print("Total CustomerAccount :", CustomerAccount.costCount)


class CustomerAccount:
    costCount = 0

    def __init__(self):
        self.FirstName = None
        self.SecondName = None
        self.Username = None
        self.Password = None
        self.PhoneNumber = None
        self.CreditCard = None
        self.CarPlate = None
        self.Membership = False
        CustomerAccount.costCount += 1

    def setCustomerAttribute(self, FirstName, SecondName, Username, Password, PhoneNumber, CreditCard, CarPlate,
                             Membership):
        self.FirstName = FirstName
        self.SecondName = SecondName
        self.Username = Username
        self.Password = Password
        self.PhoneNumber = PhoneNumber
        self.CreditCard = CreditCard
        self.CarPlate = CarPlate
        self.Membership = Membership

    def displayCustomerAccount(self):
        print("FirstName :", self.FirstName)
        print("SecondName :", self.SecondName)
        print("UserName :", self.Username)
        print("Password :", self.Password)
        print("PhoneNumber :", self.PhoneNumber)
        print("CreditCard :", self.CreditCard)
        print("CarPlate :", self.CarPlate)
        print("Membership :", self.Membership)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


emp1 = CustomerAccount()
emp1.setCustomerAttribute("Bo", "Hu", "Niccolo", "123456789", "18801308814", "450103199811252519", "US-123", True)
emp2 = CustomerAccount()

emp1.displayCustomerAccount()
emp2.displayCustomerAccount()


displayCstNum()