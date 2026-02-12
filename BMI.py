import tkinter as tk
from tkinter import messagebox


#--------Function------------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "کمبود وزن"
            color = "#3498db"
            suggestion = "پیشنهاد: کمی افزایش وزن سالم داشته باشید."
        elif bmi < 25:
            category = "نرمال"
            color = "#2ecc71"
            suggestion = "عالیه! وزنت نرماله 👌"
        elif bmi < 30:
            category = "اضافه وزن"
            color = "#f39c12"
            ideal_weight = 24.9 * (height_m ** 2)
            lose = round(weight - ideal_weight, 1)
            suggestion = f"برای رسیدن به محدوده نرمال حدود {lose} کیلو کاهش وزن پیشنهاد می‌شود."
        else:
            category = "چاقی"
            color = "#e74c3c"
            ideal_weight = 24.9 * (height_m ** 2)
            lose = round(weight - ideal_weight, 1)
            suggestion = f"برای رسیدن به محدوده نرمال حدود {lose} کیلو کاهش وزن پیشنهاد می‌شود."

        result_label.config(
            text=f"BMI: {bmi}\nوضعیت: {category}\n{suggestion}",
            fg=color
        )

    except ValueError:
        messagebox.showerror("خطا", "لطفاً عدد معتبر وارد کنید")

#---------screen--------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x400")
root.configure(bg="#FAF9EE")


title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 16, "bold"),
    bg="#DCCFC0",
    fg="#2c3e50"
)
title_label.pack(pady=15)

#------weight-----
weight_label = tk.Label(root, text="وزن (کیلوگرم):", bg="#DCCFC0")
weight_label.pack()
weight_entry = tk.Entry(root, width=25)
weight_entry.pack(pady=5)

#------height-----
height_label = tk.Label(root, text="قد (سانتی‌متر):", bg="#DCCFC0")
height_label.pack()
height_entry = tk.Entry(root, width=25)
height_entry.pack(pady=5)

#------button------
calc_button = tk.Button(
    root,
    text="محاسبه",
    bg="#6c5ce7",
    fg="white",
    width=20,
    height=2,
    command=calculate_bmi
)
calc_button.pack(pady=15)


result_label = tk.Label(
    root,
    text="",
    bg="#f5f6fa",
    font=("Arial", 11),
    wraplength=300,
    justify="center"
)
result_label.pack(pady=10)

root.mainloop()