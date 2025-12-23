from scraper import scrape_quotes, quotes_to_df

def test_scrape_quotes():
    quotes = scrape_quotes(limit=3)
    assert len(quotes) == 3 # if we are able to fetch the limit=3 rows or quptes in this eg, then assert will mark it as PASS

def test_quotes_to_df():
    df = quotes_to_df(["Hello","World"])
    assert df.shape[0] == 2
    assert "Quote" in df.columns