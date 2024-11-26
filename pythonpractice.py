#1
'''
class Bank:
    bank_name='rbi'
    bank_roi=7
    bank_address='kizikistan'
bharath=Bank()
##Access using generic properties by using object
print(bharath.bank_roi)
print(bharath.bank_address)
##Access using generic properties by using class
print(Bank.bank_address)
print(Bank.bank_name)
##modifying genericproperties by using class   --> classname.classvariable=newvalue
Bank.bank_name='hdfc'
print(bharath.bank_name)
##modifying genericproperties by using object  --> objectname.classvariable=newvalue
bharath.bank_address='india'
print(bharath.bank_address)
##creating generic properties by using class
Bank.bank_ifsc=1234                                 ## creating and deleting generic properties using object not posiible 
print(bharath.bank_ifsc)
##deleting generic properties by using class
del Bank.bank_address
print(Bank.bank_address)
'''
#------------------------------------------------------------------------------------------------------
#2
class Bank:
    bank_name='rbi'
    bank_roi=7
    bank_address='kizikistan'
    def __init__(self,cn,a,cbal):
        self.customer_name=cn
        self.age=a
        self.cbalance=cbal
    def customer_Details(self):
        print('Customer name is :',self.customer_name)
        print('customer age:',self.age)
        print('customer_balance:',self.cbalance)
    def withdraw(self):
        amount=int(input('Enter amount to withdraw'))
        if self.cbalance>=amount:
            self.cbalance-=amount
            print('withdraw process completed successfully')
            print('Remaining balance')
        else:
            print('Insufficient Balance')
    def deposite(self):
        amount=int(input('Enter amount: '))
        if amount>=0:
            self.cbalance+=amount
            print('Amount deposited successfully')
        else:
            print('Please enter amount greater than 1')
bharath=Bank('Bharath',21,6000000)
bharath.customer_Details()
Bank.customer_Details(bharath)
bharath.withdraw()