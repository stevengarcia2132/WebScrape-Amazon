#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
from bs4 import BeautifulSoup

# read the index.html file
with open('index.html', 'r',encoding =  'utf-8') as f:
    html = f.read()

# parse the html with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# find all divs with the specified class
divs = soup.find_all('div', {'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'})

# initialize an empty list to store the results
results = []

# loop through the divs and extract the desired information
for div in divs:
    # find the image link
    img = div.find('img', {'class': 's-image'})
    link = img['src'] if img else ''
    
    # find the title
    title_span = div.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    title = title_span.text if title_span else ''
    
    # find the rating
    rating_span = div.find('span', {'class': 'a-icon-alt'})
    rating = rating_span.text if rating_span else ''
    
    # find the price
    price_span = div.find('span', {'class': 'a-price-whole'})
    price = price_span.text.strip() if price_span else ''

    # find the num of reviews
    review_span = div.find('span', {'class': 'a-size-base s-underline-text'})
    review = review_span.text if review_span else ''
    



    # add the results to the list
    results.append({
        'link': link,
        'title': title,
        'rating': rating,
        'price': price,
        'review': review
    })

# write the results to a json file
with open('data13.json', 'w') as f:
    json.dump(results, f)


# In[ ]:




