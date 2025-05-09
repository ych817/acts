# circle.py
import math

def area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2

def circumference(radius):
    """Return the circumference of a circle given its radius."""
    return 2 * math.pi * radius

def sin_cos(value):
    """Return the sine and cosine of the given value (in radians)."""
    return math.sin(value), math.cos(value)

def area_from_diameter(diameter):
    """Return the area of a circle given its diameter."""
    radius = diameter / 2
    return math.pi * radius ** 2

if __name__ == '__main__':
    # Example usage of existing functions
    radius = 2
    print(f"Area (r=2): {area(radius)}")
    print(f"Circumference (r=2): {circumference(radius)}")

    # --- New feature 1: calculate sine and cosine ---
    val = float(input("Enter a value in radians to compute sin and cos: "))
    s, c = sin_cos(val)
    print(f"sin({val}) = {s}")
    print(f"cos({val}) = {c}")

    # --- New feature 2: compute area from diameter ---
    d = float(input("Enter the diameter of a circle: "))
    print(f"Area of circle with diameter {d} = {area_from_diameter(d)}")