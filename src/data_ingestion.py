import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/araJ2/customer-database/master/Ecommerce%20Customers.csv')
df = df.iloc[:, 3:]
df = df[df['Length of Membership'] > 3]

# ✅ Create data/ folder if it doesn't exist
os.makedirs("data", exist_ok=True)

df.to_csv(os.path.join('data', 'customer.csv'), index=False)
