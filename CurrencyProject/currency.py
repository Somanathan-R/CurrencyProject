from forex_python.converter import CurrencyCodes,CurrencyRates

'''test=CurrencyCodes()

symbol=test.get_symbol('INR')
name=test.get_currency_name('USD')
print("the name is ",name)
print("the symbol is",symbol)'''

c=CurrencyRates()
#c.convert('USD', 'INR', 10)
print( c.convert('USD', 'INR', 454))