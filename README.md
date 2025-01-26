# Personalized News Dashboard

## Overview

The **Personalized News Dashboard** is a dynamic web application that allows users to search and filter news articles based on personalized criteria. Built with Python using the Flask framework, the application integrates with the [NewsAPI](https://newsapi.org/) to fetch real-time news articles. Users can customize their dashboard by specifying search queries, date ranges, and sorting preferences, offering them a tailored news browsing experience.

## Features

- **Customizable Search**: Users can enter their own search queries to find news articles related to specific topics (e.g., "technology," "business," etc.).
- **Date Filters**: Users can filter news articles based on a custom date range (from and to).
- **Sort Options**: The dashboard offers sorting options to display news based on publication date or relevance.
- **Personalized Dashboard**: The application remembers user preferences for future sessions, making it easy for users to track their interests.
- **Responsive Design**: The user interface is mobile-friendly and adapts to different screen sizes.

## Requirements

- Python 3.x
- Flask
- Requests
- A NewsAPI key (get your API key from [NewsAPI.org](https://newsapi.org/))

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/personalized-news-dashboard.git
   cd personalized-news-dashboard
   ```

2. Create a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your NewsAPI key:
   
   - Create a file named `config.py` in the root of the project.
   - Inside `config.py`, define your `NEWS_API_KEY`:

   ```python
   NEWS_API_KEY = 'your-api-key-here'
   ```

5. Run the Flask app:

   ```bash
   python app.py
   ```

   The app will run on `http://127.0.0.1:5000/` by default.

## Project Structure

```
personalized-news-dashboard/
├── app.py               # Main Flask application
├── config.py            # Configuration file for API key
├── requirements.txt     # List of dependencies
├── templates/
│   └── index.html       # HTML template for displaying news articles
└── static/              # Static files like CSS, images, etc.
```

### File Descriptions

- **`app.py`**: This is the main Python file where the Flask app is set up. It contains the logic for handling HTTP requests, interacting with the NewsAPI, and rendering the web page.
- **`config.py`**: Stores the NewsAPI key used to authenticate API requests.
- **`requirements.txt`**: Lists the Python dependencies required for the project, including Flask and Requests.
- **`templates/index.html`**: The HTML file used to render the search interface and display news articles.
- **`static/`**: Contains any static files (CSS, images) used for styling the application.

## Usage

### Home Page
- Upon accessing the homepage (`http://127.0.0.1:5000/`), users will find an input form with the following fields:
  - **Search Query**: A text input where users can type a topic (default: "technology").
  - **Date Range**: Optional date filters (from and to) to restrict articles by a specific time period.
  - **Sort By**: A dropdown to choose the sorting order of results (`publishedAt` or `relevance`).

### Viewing News Articles
- After submitting the form, the app queries the NewsAPI with the specified filters.
- The search results are displayed below the form, showing:
  - Article Title
  - Source
  - Description
  - Published Date
  - Link to the full article

### Error Handling
- If there’s an error with the API request, the app will display a message letting the user know about the issue (e.g., invalid API key, no internet connection).

## Customization

- **Default Query**: You can change the default search query by modifying the `query` variable in the `index()` function in `app.py`.
- **Date Filters**: Users can adjust the from and to dates via input fields to focus on articles within a specific time period.
- **Sort Options**: You can modify the default sort order (`publishedAt`) by updating the `sortBy` parameter in the API request.
