# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:13:20 2024

@author: yentz
"""
import os
import matplotlib.pyplot as plt

# 獲取桌面的路徑
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# 資料夾的路徑
my_folder_path = os.path.join(desktop_path, "algorithm homework")

# 文字檔路徑
rec_file_path = os.path.join(my_folder_path, "rec.txt")
dyn_file_path = os.path.join(my_folder_path, "dyn.txt")


# 儲存每一行文字 "seconds" 前的值
def get_values(file_path):
    with open(file_path, "r") as old_file:
        values = []
        # 對於每一行
        for line in old_file:
            # 找到 "Time: " 和 " seconds" 之間的數字
            start_index = line.find("Time: ") + len("Time: ")
            end_index = line.find(" seconds", start_index)
            time_value_str = line[start_index:end_index]
            # 將時間數值轉換為浮點數並添加到列表中
            time_value = float(time_value_str)
            values.append(time_value)
    return values

rec_values = get_values(rec_file_path)
dyn_values = get_values(dyn_file_path)

# 繪製折線圖
plt.plot(range(1, len(rec_values) + 1), rec_values,label='Recursive(n<=53)')
plt.plot(range(1, len(dyn_values) + 1), dyn_values,label='Dynamic(n<=100)')
plt.xlabel('n')
plt.ylabel('Time(s)')
plt.title('Execution Time of Fibonacci Calculation')
plt.legend()
plt.show()

