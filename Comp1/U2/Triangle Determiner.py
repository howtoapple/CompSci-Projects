h = float(input("What is the height of the triangle?\n"));
l = float(input("What is the legnth of the triangle?\n"));
a = float(input("What is the side of the triangle??\n"));
valid = h + l
if  valid <= a:
    print("Invalid!");
    exit();
if h == l:
    if h == a:
        print("Equilateral Traingle");
if h != l:
    if l != a:
        print("Scalene Triangle");
if h == l:
    if h != a:
        print("Isosoles");
if a == h:
    if h != l:
        print("isosceles triangle");
if a == l:
    if h != l:
        print("isosceles triangle.");