# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
kilopascle = float(input('Kilopascle pressure '))

converted = kilopascle/6.895
mmhg = kilopascle*760/101.325
atm = kilopascle/101.325
print('The pressure in pound pwe square inch is ',converted)
print('The pressure in mmhg is ',mmhg)
print('The pressure in atmospheric pressure is ',atm)