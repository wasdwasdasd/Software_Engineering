#Tema4_SR3

import time
from datetime import datetime

for _ in range(5):
    current_time = datetime.now().strftime('%H:%M:%S')

    print(f"Текущее время: {current_time}")

    # Усыпляем программу на 1 секундуЫ
    time.sleep(1)