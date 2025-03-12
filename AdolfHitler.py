import matplotlib.pyplot as plt

# Данные
intervals = ['1030-1040', '1040-1050', '1050-1060', '1060-1070', '1070-1080', '1080-1090', '1090-1100']
frequencies = [0.12, 0.22, 0.22, 0.00, 0.22, 0.00, 0.22]

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.bar(intervals, frequencies, color='skyblue', edgecolor='black')

# Настройки графика
plt.title('Гистограмма распределения частот', fontsize=16)
plt.xlabel('Интервалы', fontsize=14)
plt.ylabel('Частота', fontsize=14)
plt.ylim(0, 0.25)  # Ограничение по оси Y
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Сетка

# Отображение графика
plt.show()
