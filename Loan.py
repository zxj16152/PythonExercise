class Loan:
    def __init__(self,annualInterestRate=2.5,numberOfYears=1,loanAmount=1000,borrower=""):
        self.__annualInterestRate=annualInterestRate
        self.__numberOfYears=numberOfYears
        self.__loanAmout=loanAmount
        self.__borrower=borrower
    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAmout

    def getBorrower(self):
        return self.__borrower

    def setAnnualInterestRate(self,annualInterestRate):
        self.__annualInterestRate=annualInterestRate

    def setNumberOfYears(self,numberOfYears):
        self.__numberOfYears=numberOfYears

    def setLoanAmount(self,loanAmount):
        self.__loanAmout=loanAmount

    def setBorrower(self,borrowwer):
        self.__borrower=borrowwer

    def getMonthlyPayMent(self):
        monthlyInterestRate=self.__annualInterestRate/1200
        monthlyPayment=self.__loanAmout*monthlyInterestRate/(1-(1/(1+monthlyInterestRate)**(self.__numberOfYears*12)))
        return monthlyPayment
    def getTotalPayment(self):
        totalPayment=self.getMonthlyPayMent()*self.__numberOfYears*12
        return totalPayment