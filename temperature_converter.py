#project-20
#Project Idea: Temperature Converter 
#• Description: Create a temperature converter that converts temperatures between 
#Celsius, Fahrenheit, and Kelvin. 
#• Features: 
#o Input temperature value. 
#o Choose conversion type (Celsius to Fahrenheit, etc.). 
#o Display the converted temperature.



def temperature_converter():
    print("Select conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter choice (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        temp = float(input("Enter temperature value: "))

        if choice == '1':
            calculate=(temp * 9/5) + 32
            print(f"The converted temperature is: {calculate} Fahrenheit")
        elif choice == '2':
            calculate =(temp - 32) * 5/9
            print(f"The converted temperature is: {calculate } Celsius")
        elif choice == '3':
            calculate =temp+ 273.15
            print(f"The converted temperature is: {calculate } Kelvin")
        elif choice == '4':
            calculate = temp- 273.15
            print(f"The converted temperature is: {calculate} Celsius")
    else:
        print("Invalid Input")

temperature_converter()
