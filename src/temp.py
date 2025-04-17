import os

h = [0, 1, 2, 4]
header = "hour_of_day, day, row, col\n"
data_files = [("train", h)]

output_dir = "artifacts/processed"
os.makedirs(output_dir, exist_ok=True)  # اطمینان از ایجاد دایرکتوری

output_file = os.path.join(output_dir, "output.csv")  # مسیر دقیق فایل

with open(output_file, "w") as f:
    f.write(header)
    for row in h:
        f.write(f"{row},{row},{row},{row}\n")  # اصلاح نحوه نوشتن داده‌ها
