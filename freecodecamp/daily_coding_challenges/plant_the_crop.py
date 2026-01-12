"""
Given an integer representing the size of your farm field,
and "acres" or "hectares" representing the unit for the size
of your farm field, and a type of crop, determine how many
plants of that type you can fit in your field.
"""
CONVERSION_FACTORS = {
    "acres": 4046.86,
    "hectares": 10000
}

def get_number_of_plants(field_size, unit, crop):
    crop_unit = unit.lower()
    crop_name = crop.lower()

    if field_size <= 0:
        raise ValueError("Field size must be a positive value")

    if crop_unit not in CONVERSION_FACTORS:
        raise ValueError("Invalid crop unit: must be either 'acres' or 'hectares'")
    else:
        total_square_meters = field_size * CONVERSION_FACTORS[crop_unit]

    crop_spacing = {
        "corn": 1,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }

    if crop_name not in crop_spacing:
        raise ValueError(f"Invalid crop: {crop}")
    else:
        plant_count = total_square_meters // crop_spacing[crop_name]

    return plant_count