import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla
resources = [
    "LUT", "LUTRAM", "FF", "BRAM", "DSP", "IO", "GT",
    "BUFG", "MMCM", "PLL", "PCIe"
]
available = [242400, 112800, 484800, 600, 1920, 520, 20, 480, 10, 20, 3]
empty_impl = [93009, 8367, 163762, 176.5, 187, 343, 16, 27, 3, 6, 1]
wrapper_impl = [164480, 9431, 267771, 179, 603, 343, 16, 27, 3, 6, 1]

# Calcular porcentajes
empty_pct = [100 * e / a for e, a in zip(empty_impl, available)]
wrapper_pct = [100 * w / a for w, a in zip(wrapper_impl, available)]

# Preparar gráfico horizontal
y = np.arange(len(resources))
bar_height = 0.35

plt.figure(figsize=(10, 8))
plt.barh(y - bar_height / 2, empty_pct, height=bar_height, label="Empty")
plt.barh(y + bar_height / 2, wrapper_pct, height=bar_height, label="Wrapper + Kernels")

plt.xlabel("Utilization [%]")
plt.title("FPGA Resource Utilization (Percentage)")
plt.yticks(y, resources)
plt.gca().invert_yaxis()
plt.axvline(100, color='gray', linestyle='--', linewidth=1)
plt.grid(axis='x', linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

