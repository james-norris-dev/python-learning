"""
Energy Consumption

Given the number of Calories burned during a workout,
and the number of watt-hours used by your electronic devices during that workout,
determine which one used more energy.
"""
CALORIE_IN_JOULES = 4184
WATT_HOUR_IN_JOULES = 3600
# def compare_energy(calories_burned: int, watt_hours_used: int) -> str:
#     calories_burned_in_joules = calories_burned * CALORIE_IN_JOULES
#     watt_hours_in_joules = watt_hours_used * WATT_HOUR_IN_JOULES
#
#     if calories_burned_in_joules == watt_hours_in_joules:
#         result = "Equal"
#     elif calories_burned_in_joules > watt_hours_in_joules:
#         result = "Workout"
#     else:
#         result = "Devices"
#
#     return result

# More Pythonic
def compare_energy(calories_burned: int, watt_hours_used: int) -> str:
    calories_joules = calories_burned * CALORIE_IN_JOULES
    watt_joules = watt_hours_used * WATT_HOUR_IN_JOULES

    # Condensed down to a conditional expression, similar to Java's ternary operator
    return ("Equal" if calories_joules == watt_joules
            else "Workout" if calories_joules > watt_joules
            else "Devices")