# FLask Dashboard setup
from flask import Flask, render_template
# reder the scraped data as a table
from scraper import scrape_quotes, quotes_to_df

app = Flask(__name__) 
#app - just a variable holding the web server.

@app.route("/")
def dashboard():
    quotes = scrape_quotes(limit=10)
    df = quotes_to_df(quotes)
    return render_template("dashboard.html",tables=[df.to_html(classes='data')],titles=df.columns.values)
    # converts the Dataframe DF into an HTML table.
    #Jinja2 - flask's template engine.

# enhancements - add more pages using app.route decorator for eg about myself. @app.route("/about") so after this write the about function. /api_data.
#@app.route("/about")
#def about_myself():
#    pass

# mini-amazon, products, orders,

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200, debug=True) # use 5000
    # the code inside this if cond ONLY runs when executed directly not when imported.


    

