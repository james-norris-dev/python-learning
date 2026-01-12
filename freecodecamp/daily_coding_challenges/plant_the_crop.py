"""
Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size
of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.
"""

def get_number_of_plants(field_size, unit, crop):
    total_square_meters = 0
    plant_count = 0
    ACRE_SQUARE_METER = 4046.86
    HECTARE_SQUARE_METER = 10000

    if unit == "acres":
        total_square_meters = field_size * ACRE_SQUARE_METER
    elif unit == "hectares":
        total_square_meters = field_size * HECTARE_SQUARE_METER

    crop_spacing = {
        "corn": 1,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }

    if crop in crop_spacing:
        plant_count = int(total_square_meters / crop_spacing[crop])

    return plant_count

if __name__ == "__main__":
    print(get_number_of_plants(2, "hectares", "lettuce"))