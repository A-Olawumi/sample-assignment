import requests
from bs4 import BeautifulSoup
import pandas as pd

products=[]
prices =[]
ratings =[]

# Send a GET request to the website
sp =  requests.get("https://www.jumia.com.ng/womens-shoes/")

    # Parse the HTML content of the page
sp = BeautifulSoup(sp.text, 'html.parser')

    # Identify HTML attributes for the data points you want to pull
    # For example, let's assume you want to extract product names and prices
for each in sp.find_all('a',href =True,attrs ={'class':'cbs'}):
    name =each.find('div',attrs ={'class':'df -i-ctr -pts'})
    price =each.find('div',attrs ={'class':'df -i-ctr -fw-w'})
    rate =each.find('div',attrs ={'class':'stars _m _al'})

    # Create a Pandas DataFrame
data = {'Product Name': name, 'Product Price': price}
df = pd.DataFrame(data)

    # Display the DataFrame
print(df)

    # Visualize the data (you can choose any plot of your choice)
import matplotlib.pyplot as plt

    
df['Product Price'] = df['Product Price'].str.replace('₦', '').astype(float)

    # Plotting
plt.figure(figsize=(10, 6))
plt.bar(df['Product Name'], df['Product Price'])
plt.xlabel('Product Name')
plt.ylabel('Product Price (₦)')
plt.title('Women\'s Shoes Prices on Jumia')
plt.xticks(rotation=45, ha='right')
plt.show()
