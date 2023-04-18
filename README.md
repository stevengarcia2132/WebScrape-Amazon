# WebScrape-Amazon
The index.html file is all the html code for the amazon page of which im scraping from. In this case it was the top motivational self-help books, but it can be any page on the amazon website that lists all the result for a product. 

The work.py file is the first file i started when creating this project. It contains all the code to scrape the values I wanted and placed them into a json file. I would execute the work.py file with the index.html file as the input for a page. After the Json file was created I would save the html code for the next page and run it again with new values that were contained in the new html code. Every time I moved from one page to the next I edited one of the last lines of the work.py file to make the output 'data2.json'. If I was on the 7th page of the amazon website that line would read 'data7.json'. 

The beginning of the Cleaning.pynb contains code to read every json file I in my downloads folder and adding all the values to a dataframe. I saved the final data frame as self-help books.csv. 

The EDA file contains the code I used to create five visualizaitions with the self-help books.csv. I used seaborn, matplot to create the visuals. 
