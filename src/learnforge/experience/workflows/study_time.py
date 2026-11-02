
def minute_conversion(minutes):
    print(minutes)
    print(type(minutes))

    hours = minutes // 60  ## // is the floor division operator 
    remaining_minutes = minutes % 60  # % is the modulus operator

    print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")
    print(type(hours))
    print(type(remaining_minutes))

minute_conversion(90)