# main.py
import circle

def main():
    # --- Feature 1: calculate sine and cosine from user input ---
    val = float(input("Enter a value in radians to compute sin and cos: "))
    s, c = circle.sin_cos(val)
    print(f"sin({val}) = {s}")
    print(f"cos({val}) = {c}")

    # --- Feature 2: compute area from diameter ---
    d = float(input("Enter the diameter of a circle: "))
    print(f"Area of circle with diameter {d} = {circle.area_from_diameter(d)}")

    # --- Original features: area and circumference from radius ---
    r = float(input("Enter the radius of a circle: "))
    print(f"Area: {circle.area(r)}")
    print(f"Circumference: {circle.circumference(r)}")

if __name__ == '__main__':
    main()