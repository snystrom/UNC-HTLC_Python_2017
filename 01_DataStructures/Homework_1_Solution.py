#!/user/bin/python3

userTemp = int(input("Temperature: "))
userUnit = input("Unit: ")


if userUnit == "Farenheit":
    degC = (userTemp - 32) * (5/9)
    degK = degC + 273.15
    print("{0} Celcius".format(degC))
    print("{0} Kelvin".format(degK))

elif userUnit == "Celcius":
    degF = (userTemp * (9/5)) + 32 
    degK = userTemp + 273.15
    print("{0} Farenheit".format(degF))
    print("{0} Kelvin".format(degK))

elif userUnit == "Kelvin":
    degC = userTemp - 273.15
    degF = (degC - 32) * (5/9) 
    print("{0} Celcius".format(degC))
    print("{0} Farenheit".format(degF))

else:
    print("Error, {inputUnit} is not a valid unit of temperature! Try \"Farenheit\", \"Celcius\", or \"Kelvin\".".format(inputUnit = userUnit))


