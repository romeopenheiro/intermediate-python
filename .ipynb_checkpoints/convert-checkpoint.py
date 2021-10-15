def ounces_to_grams(weight):
    new_weight = weight * 28.3495
    return new_weight

def to_metric(value, unit):
    if unit == "oz":
        new_val = value * 28.3495
        return new_val, "g"
    
    if unit == "F":
        new_val = (value - 32) * .5556
        return new_val, "C"
    
    raise ValueError(f"The unit '{unit}' is not recogised")