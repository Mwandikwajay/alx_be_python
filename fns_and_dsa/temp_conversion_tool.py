# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_FREEZING_POINT = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT

# Main function to handle user interaction
def main():
    try:
        # Prompt user to enter temperature
        temperature = float(input("Enter the temperature: "))
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on user input
        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result:.2f}°F")
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result:.2f}°C")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
