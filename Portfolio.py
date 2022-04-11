'''Construct a simple Portfolio class that has a collection of Stocks and 
a "Profit" method that receives 2 dates and returns the profit of the 
Portfolio between those dates. 
Assume each Stock has a "Price" method that receives a date and returns its Price.
Bonus Track: make the Profit method return the "annualized return" of the 
portfolio between the given dates.'''


from datetime import datetime, timedelta
import random
import calendar


class Portfolio:

    def __init__(self, stocks):

        self._stocks = stocks

    def Price(self, date):

        sotckPrices = [stock.Price(date) for stock in self._stocks]

        return sum(sotckPrices)

    def Profit(self, entryDate, withdrawalDate):

        entryPrice = self.Price(entryDate)
        withdrawalPrice = self.Price(withdrawalDate)

        instantReturn = withdrawalPrice - entryPrice
        annualizedReturn = self.AnnualizedTotalReturn(
            entryDate, withdrawalDate, entryPrice, withdrawalPrice)

        return instantReturn, annualizedReturn

    def AnnualizedTotalReturn(self, entryDate, withdrawalDate, entryPrice, withdrawalPrice):

        differenceOfYears = withdrawalDate.year - entryDate.year
        difference = withdrawalDate - entryDate.replace(withdrawalDate.year)
        daysInYear = 366 if calendar.isleap(withdrawalDate.year) else 365
        numberYears = differenceOfYears + difference.days/daysInYear
        annualReturn = (((withdrawalPrice/entryPrice)**(1/numberYears))-1)*100

        return annualReturn


class Stock:

    def __init__(self, symbol, quantity):

        self._symbol = symbol
        self._quantity = quantity

    def Price(self, date):

        return random.randrange(10, 100)*self._quantity


if __name__ == '__main__':

    # Create stocks for portfolio
    appleStocks = Stock("AAPL", 4.3)
    microsoftStocks = Stock("MSFT", 5.4)
    samsungStocks = Stock("SMSNN", 3.2)

    # Create Portfolio
    portfolio = Portfolio(stocks=[appleStocks, microsoftStocks, samsungStocks])
    print(portfolio.Profit(entryDate=datetime(2021, 1, 1),
          withdrawalDate=datetime(2022, 6, 1)))
