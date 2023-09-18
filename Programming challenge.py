def Menu():
    MenuInt = int(input("""Press 1 for Area of triangle,
Press 2 for Power Calculator,
Press 3 for Sum of two numbers,
Press 4 for Convert age to days,
Press 5 for Encode Morse,
Press 6 for Calculate profit.
Press 7 to Exit """))
    if MenuInt == 1:
        TriArea()
    elif MenuInt == 2:
        PowerCalc()
    elif MenuInt == 3:
        TwoSum()
    elif MenuInt == 4:
        AgeConvert()
    elif MenuInt == 5:
        EncodeMorse()
    elif MenuInt == 6:
        CalcProfit()

               
#Area of a Triangle
def TriArea():
    base = int(input("Base of triangle? "))
    height = int(input("Height of triangle? "))
    area = int(base * height / 2)
    print (area)
    Menu()

def PowerCalc():
    volt = int(input("Voltage? "))
    current = int(input("Current? "))
    power = int(volt * current)
    print(power)
    Menu()

def TwoSum():
    num1 = int(input("Enter first num "))
    num2 = int(input("Enter second num "))
    add = int(num1 + num2)
    if num1 % 7 == 0 or num2 %7 == 0:
        div = int(num1 / num2)
        print(div)
    elif num1 % 11 == 0 or num2 % 11 == 0:
        mult = int(num1 * num2)
        print(mult)
    else:
        print(add)
    Menu()

def AgeConvert():
    age = -1
    while age < 0:
        age = int(input("Enter age"))
    days = age * 365.25
    print(days)
    Menu()

def EncodeMorse():
    char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
    msg = input("Enter message ")
    char = [*msg.upper()]
    morse = []

    for x in (char):
        ms = char_to_dots.get(x)
        morse.append(ms)
    print(morse)
    Menu()
    
def CalcProfit():
    profit = ({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
})
    cost = profit.get("cost_price")
    invent = profit.get("inventory")
    Total_cost = cost*invent
    sold = profit.get("sell_price")
    Total_sales = sold*invent
    Total = Total_sales-Total_cost
    print(Total)
    Menu()

Menu()
