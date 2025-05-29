import numpy as np
import matplotlib.pyplot as plt

# Número de muestras
num_rows = 256
num_columns = 5

data = np.fromfile("cpp_data_error/cmake-build-debug/result.bin", dtype=np.float64, count=num_rows*num_columns)

print(data)

sin_double = data[0::5]
sin_factor = data[1::5]
sinf_factor = data[2::5]
sinf_float_factor = data[3::5]
sinf_factorf = data[4::5]

# Calcular errores absolutos
error_0 = np.abs(sin_double - sin_factor)
error_1 = np.abs(sin_double - sinf_factor)
error_2 = np.abs(sin_double - sinf_float_factor)
error_3 = np.abs(sin_double - sinf_factorf)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(error_3, label="Explicit cast<float>(M_PI*i/32)", linewidth=2)
plt.plot(error_0, label="Truncated M_PI*i/32", linewidth=2)
#plt.plot(error_1, label="sinf(float(pi*i/32))", linewidth=2)
#plt.plot(error_2, label="sinf(float(factor))", linewidth=2)

plt.xlabel("Sample index")
plt.ylabel("Absolute error")
plt.title("Effect of Implicit vs Explicit Float Promotions")
plt.legend()
plt.grid(True)

# Aumentar tamaño de la leyenda del eje Y (notación científica si aparece)
plt.gca().yaxis.offsetText.set_fontsize(12)

plt.tight_layout()
plt.show()

