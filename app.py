from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY

app = Flask(__name__)

# API endpoint
NEWS_API_URL = "https://newsapi.org/v2/everything"

@app.route("/", methods=["GET", "POST"])
def index():
    # Default search parameters
    query = "technology"
    from_date = None
    to_date = None
    sort_by = "publishedAt"  # Default sort order

    # Handle form submission
    if request.method == "POST":
        query = request.form.get("query", "technology")
        from_date = request.form.get("from_date", None)
        to_date = request.form.get("to_date", None)
        sort_by = request.form.get("sort_by", "publishedAt")

    # Build API parameters
    params = {
        "apiKey": NEWS_API_KEY,
        "q": query,
        "from": from_date,
        "to": to_date,
        "sortBy": sort_by,
        "pageSize": 20,  # Limit results
    }

    # Fetch news
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Raise error for bad responses
        news = response.json()
        articles = news.get("articles", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        articles = []

    return render_template("index.html", articles=articles, query=query)

if __name__ == "__main__":
    app.run(debug=True)
