import circle

def main():
    radius = 3
    circle_area = circle.area_from_radius(radius)
    print(f"Area: {circle_area}")
    # print(f"Circumference: {circle.circumference(radius)}")

if __name__ == "__main__":
    main()