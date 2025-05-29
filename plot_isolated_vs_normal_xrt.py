import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Cargar los datos desde los archivos binarios
normal_runtimes = np.fromfile("./data/normal_runtimes.bin", dtype=np.int64)
isolated_runtimes = np.fromfile("./data/isolated_runtimes.bin", dtype=np.int64)

# Crear una figura con subplots
plt.figure(figsize=(14, 6))

# Boxplot
#plt.subplot(1, 2, 1)
#sns.boxplot(data=[normal_runtimes, isolated_runtimes])
#plt.xticks([0, 1], ['Normal', 'Isolated'])
#plt.ylabel('Latency (ns)')
#plt.title('Boxplot of Latency Distributions')

# Violinplot
sns.violinplot(data={
    "Normal": normal_runtimes,
    "Isolated": isolated_runtimes
}, orient='h')

plt.xlabel('Latency (ns)')
plt.ylabel('Execution Context')
plt.title('Violin Plot of Latency Distributions')

# Histograma
##plt.subplot(1, 2, 2)
#sns.histplot(normal_runtimes, bins=50, color='red', label='Normal', kde=True, stat="density")
#sns.histplot(isolated_runtimes, bins=50, color='blue', label='Isolated', kde=True, stat="density")
#plt.xlabel('Latency (ns)')
#plt.ylabel('Density')
#plt.title('Histogram of Latencies')
#plt.legend()

plt.tight_layout()
plt.show()

