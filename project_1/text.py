import numpy as np
from scipy.optimize import curve_fit

# Dữ liệu từ câu hỏi
t = np.array([8.67, 6.55, 4.53, 3.29, 2.56, 1.95, 1.43, 1.04, 0.76])
V = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Định nghĩa hàm mô hình
def model(t, K, tau):
    return K * np.exp(-1 / t)

# Ước lượng tham số K và t từ dữ liệu
popt, pcov = curve_fit(model, t, V)

# Kết quả ước lượng
K, t = popt
print(f"Estimated K: {K}")
print(f"Estimated t: {t}")