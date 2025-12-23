# Scraping functions
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def scrape_quotes(limit=5):
    url="https://quotes.toscrape.com/"
    #url="https://books.toscrape.com/"
    response=requests.get(url) # fetch webpage 
    if response.status_code!=200: # 200 is for successful fetch, 404 is for not found.
        logging.error("Failed to fetch website")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser" ) # parsing the HTML response that we recieved.
    #soup = BeautifulSoup(html_doc, 'html.parser')
    #print(soup.prettify())
    #<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>

    quotes = [q.text for q in soup.find_all("span", class_="text")] # find all the quotes. try to use filter() as code optimization.
    #print(quotes) --- This is how you test, but how you prove that unit testing or code testing is done - is thru a framework pytest.
    return quotes[:limit] # start=0, stop = limit and quotes is a list

# Pandas dataframe
def quotes_to_df(quotes):
    df = pd.DataFrame(quotes,columns=["Quote"])
    #converts the list into a Pandas dataframe:
    '''
    0 Quote 1
    1 Quote 2
    2 Quote 3
    '''
    return df 



