def temperature_converter():
    print("Temperature Converter")
    try:
        value = float(input("Enter the temperature value: "))
        source_unit = input("Enter the source unit (Celsius or Fahrenheit): ").lower()
        target_unit = input("Enter the target unit (Celsius or Fahrenheit): ").lower()

        if source_unit == "celsius" and target_unit == "fahrenheit":
            result = (value * 9/5) + 32
        elif source_unit == "fahrenheit" and target_unit == "celsius":
            result = (value - 32) * 5/9
        else:
            print("Invalid unit conversion. Supported units: Celsius, Fahrenheit.")
            return

        print(f"Result: {result} {target_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def length_converter():
    print("Length Converter")
    try:
        value = float(input("Enter the length value: "))
        source_unit = input("Enter the source unit (Meters or Feet): ").lower()
        target_unit = input("Enter the target unit (Meters or Feet): ").lower()

        if source_unit == "meters" and target_unit == "feet":
            result = value * 3.281
        elif source_unit == "feet" and target_unit == "meters":
            result = value / 3.281
        else:
            print("Invalid unit conversion. Supported units: Meters, Feet.")
            return

        print(f"Result: {result} {target_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def weight_converter():
    print("Weight Converter")
    try:
        value = float(input("Enter the weight value: "))
        source_unit = input("Enter the source unit (Kilograms or Pounds): ").lower()
        target_unit = input("Enter the target unit (Kilograms or Pounds): ").lower()

        if source_unit == "kilograms" and target_unit == "pounds":
            result = value * 2.205
        elif source_unit == "pounds" and target_unit == "kilograms":
            result = value / 2.205
        else:
            print("Invalid unit conversion. Supported units: Kilograms, Pounds.")
            return

        print(f"Result: {result} {target_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def main():
    print("Choose the type of conversion:")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        temperature_converter()
    elif choice == "2":
        length_converter()
    elif choice == "3":
        weight_converter()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
