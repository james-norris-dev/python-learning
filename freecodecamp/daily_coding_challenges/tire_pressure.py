"""
Tire Pressure
Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, and another array of two numbers representing the minimum and maximum pressure for your tires in bar, return an array of four strings describing each tire's status.

    1 bar equal 14.5038 psi.

Return an array with the following values for each tire:
*** "Low" if the tire pressure is below the minimum allowed.
*** "Good" if it's between the minimum and maximum allowed.
*** "High" if it's above the maximum allowed.

"""
# # First attempt
# def tire_status(pressures_psi, range_bar):
#     # Converted the range_bar values to min and max psi
#     min_psi = range_bar[0] * 14.5038
#     max_psi = range_bar[1] * 14.5038
#
#     # Created a new list to hold the tire status for all four tires
#     pressures_status = []
#
#     # Iterate through the list of tire pressures
#     # Compare them to the min and max
#     # Attach the tire status for each tire to the new list
#     for i in range(len(pressures_psi)):
#         if pressures_psi[i] < min_psi:
#             pressures_status.append("Low")
#         elif pressures_psi[i] >= min_psi and pressures_psi[i] <= max_psi:
#             pressures_status.append("Good")
#         else:
#             pressures_status.append("High")
#
#     # Return the tire status list
#     return pressures_status

# # More Pythonic
# def tire_status(pressures_psi, range_bar):
#     # Converted the range_bar values to min and max psi
#     min_psi = range_bar[0] * 14.5038
#     max_psi = range_bar[1] * 14.5038
#
#     # Created a new list to hold the tire status for all four tires
#     pressures_status = []
#
#     # Iterate through the list of tire pressures
#     # Compare them to the min and max
#     # Attach the tire status for each tire to the new list
#     for pressure in pressures_psi:
#         if pressure < min_psi:
#             pressures_status.append("Low")
#         elif min_psi <= pressure <= max_psi:
#             pressures_status.append("Good")
#         else:
#             pressures_status.append("High")
#
#     # Return the tire status list
#     return pressures_status

# Most Pythonic
def tire_status(pressures_psi, range_bar):
    # Converted the range_bar values to min and max psi
    min_psi = range_bar[0] * 14.5038
    max_psi = range_bar[1] * 14.5038

    # Converted empty list declaration and for loop to a list comprehension
    return [
        "Low" if pressure < min_psi
        else "High" if pressure > max_psi
        else "Good"
        for pressure in pressures_psi
    ]
