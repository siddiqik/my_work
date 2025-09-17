
def cm2_to_m2(area_cm2: float) -> float:
    return area_cm2 / 10_000.0

def compare_two_areas(shape1, shape2) -> int:
    area1 = shape1.area()
    area2 = shape2.area()

    eps = 1e-9
    if area1 < area2 - eps:
        return -1
    elif area1 > area2 + eps:
        return 1
    else:
        return 0
def pretty_area(area: float, unit: str = "cm^2") -> str:
        return f"{area:.2f} {unit}"