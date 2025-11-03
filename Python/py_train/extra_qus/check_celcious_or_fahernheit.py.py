def temp(c, f, choice):
    if choice.lower() == "celsius":
        formula = ((f - 32) * 5) / 9
        return round(formula)
    elif choice.lower() == "fahrenheit":
        formula = (c * 9 / 5) + 32
        return round(formula)
    else:
        return "Invalid choice. Please choose 'Celsius' or 'Fahrenheit'."

# Example usage
c = 60
f = 45 
choice = input("Choose One (Celsius or Fahrenheit): ")
print(temp(c, f, choice))
