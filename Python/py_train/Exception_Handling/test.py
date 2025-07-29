class UnderAgeException(Exception):
    pass

def check_voting_eligibility(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be nagative")
        elif age < 18:
            raise UnderAgeException("Not eligible to vote")
        else:
            return "Eligible to vote"
    except ValueError as ve:
        return f'Value Error: {ve}'
    except UnderAgeException as uge:
        return f'Under Age Exception: {uge}'
    
age = input("Enter Age: ")
print(check_voting_eligibility(age))