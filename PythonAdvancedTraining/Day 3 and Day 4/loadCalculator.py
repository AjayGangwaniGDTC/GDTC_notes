load = float(input("Enter the load(in MW):"))
a = 0.6 * load
b = (1-0.6) * load

print(f"Generator A can handle load up to: {a:.0f} MW")
print(f"Generator B can handle load up to: {b:.0f} MW")