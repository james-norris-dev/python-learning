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

CROP_SPACING = {
    "corn": 1,
    "wheat": 0.1,
    "soybeans": 0.5,
    "tomatoes": 0.25,
    "lettuce": 0.2
}

def get_number_of_plants(field_size: float, unit: str, crop: str) -> int:
    crop_unit = unit.lower()
    crop_name = crop.lower()

    if field_size <= 0:
        raise ValueError("Field size must be a positive value")

    if crop_unit not in CONVERSION_FACTORS:
        raise ValueError("Invalid crop unit: must be either 'acres' or 'hectares'")

    total_square_meters = field_size * CONVERSION_FACTORS[crop_unit]


    if crop_name not in CROP_SPACING:
        raise ValueError(f"Invalid crop: {crop}")

    # noinspection PyTypeChecker
    return total_square_meters // CROP_SPACING[crop_name]
