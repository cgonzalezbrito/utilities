import math

jlow = 0
table = [math.sin(math.pi * (i - jlow + 1) / 32.0) for i in range(64)]
with open("sin_table.h", "w") as f:
    f.write("static const double sin_table[64] = {\n")
    for i, value in enumerate(table):
        f.write(f"    {value:.16f}")
        if i != 63:
            f.write(",\n")
    f.write("\n};\n")
