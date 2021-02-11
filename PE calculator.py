'''

basic P/E calculator

by MrSugo

'''

# Inputs
ShPr = input("Share price: ")
Ea = input("Earnings (in billions): ")
NSh = input("Number of shares (in billions): ")
result = float(ShPr) / float(Ea) * float(NSh)

# How it works
print()
def explanation():
    print("With a Share price of " + ShPr + "$")
    print(Ea + " billions of earnings")
    print("and a number of shares equal to " + NSh + " billions")

print("the P/E ration is the ratio of a company's share price to the company's earnings per share")
print()
explanation()
print()
print("P/E ratio is " + str(round(result, 2)))

# Considerations
very_high_pe = 50
high_pe = 30
cheap = 15
if result >= very_high_pe:
    print("This stock is very overvalued")
elif high_pe <= result <= very_high_pe:
    print("This stock is a bit overvalued")
elif cheap <= result <= high_pe:
    print("The stock's price reflects the company's value")
else:
    print("You discovered a bargain issue!")

