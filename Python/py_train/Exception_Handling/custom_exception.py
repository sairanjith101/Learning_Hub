# Step 1: Create custom exception
class UnderAgeException(Exception):
    pass

# Step 2: Use the custom exception
def check_voting_eligibility(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative")
        elif age < 18:
            raise UnderAgeException("Not eligible to vote")
        else:
            return "Eligible to vote"
    except ValueError as ve:
        return f"ValueError: {ve}"
    except UnderAgeException as ue:
        return f"UnderAgeException: {ue}"

# Step 3: Test the function
print(check_voting_eligibility(25))     # Eligible to vote
print(check_voting_eligibility(15))     # UnderAgeException
print(check_voting_eligibility(-5))     # ValueError
print(check_voting_eligibility("abc"))  # ValueError
