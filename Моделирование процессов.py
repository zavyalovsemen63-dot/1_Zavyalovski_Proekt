import math
import matplotlib.pyplot as plt

# Константы
g = 9.8  # ускорение свободного падения, м/с²

def calculate_trajectory(v0, alpha_deg):
    # Перевод угла в радианы
    alpha_rad = math.radians(alpha_deg)
    
    # Расчет времени полета
    t_pol = (2 * v0 * math.sin(alpha_rad)) / g
    
    # Расчет дальности полета
    x_max = v0 * math.cos(alpha_rad) * t_pol
    
    # Расчет максимальной высоты
    t_max_height = t_pol / 2
    y_max = v0 * math.sin(alpha_rad) * t_max_height - (g * t_max_height**2) / 2
    
    # Генерация массива времени для построения графика
    t = [i * t_pol / 100 for i in range(101)]
    
    # Расчет координат траектории
    x = [v0 * math.cos(alpha_rad) * ti for ti in t]
    y = [v0 * math.sin(alpha_rad) * ti - (g * ti**2) / 2 for ti in t]
    
    return x_max, y_max, t_pol, x, y

def main():
    # Ввод данных
    v0 = float(input("Введите начальную скорость (м/с): "))
    alpha_deg = float(input("Введите угол броска (градусы): "))
    
    # Расчет параметров
    x_max, y_max, t_pol, x, y = calculate_trajectory(v0, alpha_deg)
    
    # Вывод результатов
    print(f"\nРезультаты расчета:")
    print(f"Дальность полета: {x_max:.2f} м")
    print(f"Максимальная высота: {y_max:.2f} м")
    print(f"Время полета: {t_pol:.2f} с")
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Траектория полета тела")
    plt.xlabel("Расстояние, м")
    plt.ylabel("Высота, м")
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.show()

if __name__ == "__main__":
    main()
