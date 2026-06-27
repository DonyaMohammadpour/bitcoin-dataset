import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# خوندن فایل
df = pd.read_csv('BTC-USD.csv')

# اطلاعات پایه
print('Total days:', len(df))
print('Columns:', list(df.columns))
print()

# آمار Open و Close
for col in ['Open', 'Close']:
    print(f'--- {col} ---')
    print('Mean is :', np.mean(df[col])) # میانگین
    print('Median is :', np.median(df[col])) # میانه
    print('Std is :', np.std(df[col])) # انحراف معیار
    print('Variance is :', np.var(df[col])) # واریانس
    print('Min is :', np.min(df[col])) # حداقل (مینیمم)
    print('Max is :', np.max(df[col])) # حداکثر (ماکسیمم)
    print("-----------------------------------")

# رسم نمودار
plt.plot(df['Date'], df['Open'], label='Open')
#plt.plot(df['Date'], df['Close'], label='Close')

plt.axhline(y=np.mean(df['Open']), color='blue', linestyle='--', label='Open Mean')
#plt.axhline(y=np.mean(df['Close']), color='yellow', linestyle='--', label='Close Mean') # چون حس کردم روی هم میوفته کامنتش کردم ، نمیدونستم چجوری پنجره جدا بزارم

plt.legend() # راهنما
plt.show() # دستور نمایش

# اطلاعات دیتابیس
df.info()