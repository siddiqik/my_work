from shapes import Rectangle, Circle, Triangle
from utils import cm2_to_m2, pretty_area, compare_two_areas


def welcome() -> None:
    print("This is the Shape Toolkit.")
    print("Available shapes: rectangle, circle, triangle")
    print("Make sure to enter all dimensions in centimeters.")
    print("Type 'quit' at any prompt to exit.\n")


def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt)
        if raw.strip().lower() == "quit":
            raise SystemExit
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number (or 'quit' to exit).")


def build_shape():
    kind = input("Which shape? (rectangle/circle/triangle): ").strip().lower()
    if kind == "quit":
        raise SystemExit

    if kind == "rectangle":
        w = read_float("Width (cm): ")
        h = read_float("Height (cm): ")
        return Rectangle(w, h)

    elif kind == "circle":
        r = read_float("Radius (cm): ")
        return Circle(r)

    elif kind == "triangle":
        b = read_float("Base (cm): ")
        h = read_float("Height (cm): ")
        return Triangle(b, h)

    else:
        print("Sorry, I don't recognize that shape.\n")
        return None


def main() -> None:
    """
    Main loop:
    - greet the user
    - repeatedly build a shape
    - print description and areas (cm^2 and m^2)
    - compare with previous shape
    - ask whether to continue
    """
    welcome()

    previous = None

    while True:
        shape = build_shape()
        if shape is None:
            continue

        print("\nYou created:", shape.describe())

        area_cm2 = shape.area()
        area_m2 = cm2_to_m2(area_cm2)

        print("Area in cm^2:", pretty_area(area_cm2, "cm^2"))
        print("Area in m^2: ", pretty_area(area_m2, "m^2"))

        if previous is not None:
            cmp = compare_areas(shape, previous)
            if cmp < 0:
                print("This shape is smaller than the previous one.")
            elif cmp > 0:
                print("This shape is larger than the previous one.")
            else:
                print("This shape is (approximately) the same size as the previous one.")

        previous = shape

        again = input("\nCreate another shape? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
