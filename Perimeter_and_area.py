print("=" * 40)
print("Hi, This is Calculation of geometric shapes")
print("=" * 40)

def calculator():
    print("Available shapes:")
    shapes = [
        "1) Square",
        "2) Rectangle", 
        "3) Triangle",
        "4) Circle",
        "5) Parallelogram",
        "6) Trapezoid",
        "7) Rhombus"
    ]
    
    for shape in shapes:
        print(shape)
    
    print("=" * 40)
    
    i = input("Choose your shape (enter number 1-7): ")
    
    if i == "1":  # مربع
        a = float(input("Input side length: "))
        print(f"Shape perimeter: {4 * a}")
        print(f"Area of the shape: {a ** 2}")
    
    elif i == "2":  # مستطیل
        a = float(input("Input length: "))
        b = float(input("Input width: "))
        print(f"Shape perimeter: {(a + b) * 2}")
        print(f"Area of the shape: {a * b}")
    
    elif i == "3":  # مثلث
        print("Triangle calculation")
        method = input("Calculate with: 1) Base and height  2) Three sides (Heron's formula): ")
        
        if method == "1":
            base = float(input("Input base: "))
            height = float(input("Input height: "))
            area = 0.5 * base * height
            print(f"Area of the shape: {area}")
            #  محیط نیاز به سه ضلع داریم
            a = float(input("Input side a: "))
            b = float(input("Input side b: "))
            c = float(input("Input side c: "))
            print(f"Shape perimeter: {a + b + c}")
        
        elif method == "2":
            a = float(input("Input side a: "))
            b = float(input("Input side b: "))
            c = float(input("Input side c: "))
            perimeter = a + b + c
            s = perimeter / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            print(f"Shape perimeter: {perimeter}")
            print(f"Area of the shape: {area}")
    
    elif i == "4":  # دایره
        r = float(input("Input radius: "))
        pi = 3.14159
        print(f"Circumference (perimeter): {2 * pi * r}")
        print(f"Area of the shape: {pi * r ** 2}")
    
    elif i == "5":  # متوازی‌الاضلاع
        a = float(input("Input base: "))
        b = float(input("Input side length: "))
        height = float(input("Input height: "))
        print(f"Shape perimeter: {2 * (a + b)}")
        print(f"Area of the shape: {a * height}")
    
    elif i == "6":  # ذوزنقه
        a = float(input("Input base1: "))
        b = float(input("Input base2: "))
        c = float(input("Input side1: "))
        d = float(input("Input side2: "))
        height = float(input("Input height: "))
        print(f"Shape perimeter: {a + b + c + d}")
        print(f"Area of the shape: {(a + b) * height / 2}")
    
    elif i == "7":  # لوزی
        a = float(input("Input side length: "))
        d1 = float(input("Input diagonal1: "))
        d2 = float(input("Input diagonal2: "))
        print(f"Shape perimeter: {4 * a}")
        print(f"Area of the shape: {d1 * d2 / 2}")
    
    else:
        print("Wrong number!!")
        return

calculator()

while True:
    print("\n" + "=" * 40)
    again = input("Do you want to calculate another shape? (yes/no): ").lower()
    if again == "yes" or again == "y":
        calculator()
    else:
        print("Goodbye!")
        break