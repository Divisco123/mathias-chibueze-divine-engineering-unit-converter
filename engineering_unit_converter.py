"""
Engineering Unit Converter
CTE123 Python Mini Project - ND1 Mechatronics Engineering

This program converts between common engineering measurement units.
It also keeps a history of successful conversions during the current run.
"""

# Store successful conversions so the user can review them later.
conversion_history = []


def get_number(prompt, allow_negative=True):
    """Ask for a number and keep asking until valid input is entered."""
    while True:
        try:
            number = float(input(prompt))

            # Negative values are not accepted for length, mass, or speed.
            if not allow_negative and number < 0:
                print("Please enter zero or a positive number.")
                continue

            return number

        except ValueError:
            print("Invalid input. Please enter a number, for example 12 or 12.5.")


def get_direction():
    """Ask which direction the user wants to convert."""
    while True:
        print("1. First unit to second unit")
        print("2. Second unit to first unit")

        try:
            direction = int(input("Choose conversion direction (1 or 2): "))
            if direction in (1, 2):
                return direction
            print("Please choose 1 or 2.")
        except ValueError:
            print("Invalid choice. Please enter 1 or 2.")


def convert_length(value, direction):
    """Convert millimetres and inches."""
    if direction == 1:
        return value / 25.4, "inches"
    else:
        return value * 25.4, "mm"


def convert_temperature(value, direction):
    """Convert Celsius and Fahrenheit."""
    if direction == 1:
        return (value * 9 / 5) + 32, "°F"
    else:
        return (value - 32) * 5 / 9, "°C"


def convert_mass(value, direction):
    """Convert kilograms and pounds."""
    if direction == 1:
        return value * 2.20462, "lb"
    else:
        return value / 2.20462, "kg"


def convert_speed(value, direction):
    """Convert kilometres per hour and metres per second."""
    if direction == 1:
        return value / 3.6, "m/s"
    else:
        return value * 3.6, "km/h"


def show_history():
    """Display all successful conversions made during this run."""
    print("\n--- CONVERSION HISTORY ---")

    if len(conversion_history) == 0:
        print("No conversions have been made yet.")
    else:
        for item_number, record in enumerate(conversion_history, start=1):
            print(f"{item_number}. {record}")

    print("--------------------------\n")


def main():
    """Display the menu and control the unit converter."""
    while True:
        print("\n================================")
        print("      ENGINEERING UNIT CONVERTER")
        print("================================")
        print("1. Length (mm and inches)")
        print("2. Temperature (°C and °F)")
        print("3. Mass (kg and lb)")
        print("4. Speed (km/h and m/s)")
        print("5. View conversion history")
        print("6. Exit")
        print("================================")

        try:
            choice = int(input("Select an option (1-6): "))
        except ValueError:
            print("Invalid menu choice. Please enter a whole number from 1 to 6.")
            continue

        if choice == 1:
            print("\nLENGTH CONVERSION")
            direction = get_direction()
            value = get_number("Enter the measurement: ", allow_negative=False)
            result, result_unit = convert_length(value, direction)
            input_unit = "mm" if direction == 1 else "inches"

        elif choice == 2:
            print("\nTEMPERATURE CONVERSION")
            direction = get_direction()
            value = get_number("Enter the temperature: ")
            result, result_unit = convert_temperature(value, direction)
            input_unit = "°C" if direction == 1 else "°F"

        elif choice == 3:
            print("\nMASS CONVERSION")
            direction = get_direction()
            value = get_number("Enter the mass: ", allow_negative=False)
            result, result_unit = convert_mass(value, direction)
            input_unit = "kg" if direction == 1 else "lb"

        elif choice == 4:
            print("\nSPEED CONVERSION")
            direction = get_direction()
            value = get_number("Enter the speed: ", allow_negative=False)
            result, result_unit = convert_speed(value, direction)
            input_unit = "km/h" if direction == 1 else "m/s"

        elif choice == 5:
            show_history()
            continue

        elif choice == 6:
            print("Thank you for using the Engineering Unit Converter. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 6.")
            continue

        # Display the answer to three decimal places.
        result_message = f"{value:g} {input_unit} = {result:.3f} {result_unit}"
        print("\nConversion result:")
        print(result_message)

        # Save the successful conversion in the history list.
        conversion_history.append(result_message)


# Start the program when this file is run.
if __name__ == "__main__":
    main()
