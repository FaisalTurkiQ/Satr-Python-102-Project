from datetime import datetime
class Bank_Account:
    def __init__(self):
        self.__balace = 0.0

    def deposit (self,amount) :
        self.__balace+=amount
        day = datetime.now().strftime('%A')
        date = datetime.now().strftime('%-d %B %Y')
        time = datetime.now().strftime('%-I:%M%p')
        print('{} SAR has been deposited to your bank balance on {}, {} , at {}.'.format(amount,day,date,time))


    def withdraw(self,amount):
        if self.__balace-amount >= 0 :
            day = datetime.now().strftime('%A')
            date = datetime.now().strftime('%-d %B %Y')
            time = datetime.now().strftime('%-I:%M%p')
            print('{} SAR has been deducted from your bank balance on {}, {} , at {}.'.format(amount, day, date,time))
            self.__balace-=amount
        else:
            print('The balance is not allowed to withdraw')

    def get_balace(self):
        return self.__balace

