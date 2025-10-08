# Django News App

A Django-based news aggregation application that scrapes news from various categories from Inshorts.com and displays them in both English and Hindi.

## About This Project

This was my **first Django project** that I created during my college years in **2021**. It holds special significance as it marked the beginning of my web development journey. The project demonstrates my early understanding of web scraping, Django framework, and full-stack development concepts.

### Future Plans
I'm planning to completely revamp this project with:
- ✨ **Modern UI/UX Design** - Contemporary and responsive interface
- 🚀 **Optimized Code** - Clean, efficient, and well-documented codebase
- 🔧 **New Features** - Enhanced functionality and user experience
- 📱 **Better Mobile Support** - Improved responsive design
- 🎯 **Performance Improvements** - Faster loading and better error handling
- 🆕 **New Repository** - Fresh start with modern development practices

This repository represents the original version, showcasing the growth and learning journey from a college project to professional-level development.

## Features

- **Web Scraping**: Scrapes news from Inshorts.com website
- **Multiple Categories**: Supports various news categories including:
  - General News
  - Business
  - Sports
  - Technology
  - Politics
  - Entertainment
  - World News
  - Startup News
  - Miscellaneous
- **Multi-language Support**: Available in both English and Hindi
- **Responsive Design**: Clean and responsive web interface
- **Error Handling**: Robust error handling for web scraping operations

## Technology Stack

- **Backend**: Django (Python web framework)
- **Web Scraping**: BeautifulSoup4, requests
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default Django database)

## Required Python Packages

```
beautifulsoup4
bs4
Django
lxml
requests
```

## Project Structure

```
Django-News/
├── DjangoNews/          # Main Django project directory
├── news/                # News app
│   ├── getnews/         # Web scraping modules
│   │   ├── getnews.py   # Main scraping logic
│   │   └── news_sites/  # Site-specific scrapers
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   └── urls.py          # URL patterns
├── static/              # Static files
│   ├── css/             # CSS stylesheets
│   └── images/          # Image assets
├── templates/           # HTML templates
├── requirements.txt     # Python dependencies
└── manage.py           # Django management script
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/Karanjot786/Django-News.git
cd Django-News
```

2. **Create and activate virtual environment** (recommended)
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run database migrations**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

5. **Start the development server**
```bash
python3 manage.py runserver
```

6. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - For Hindi news, visit `http://127.0.0.1:8000/hindi/`

## Screenshots

### English Version
![English Homepage](static/images/en/image.png)
*Main homepage showing English news articles*

![English News Interface](static/images/en/image_1.png)
*News interface with detailed article view*

### Hindi Version
![Hindi Homepage](static/images/hi/image.png)
*Main homepage showing Hindi news articles*

![Hindi News Interface](static/images/hi/image_1.png)
*Hindi news interface with detailed article view*

## Usage

- The application automatically scrapes news from Inshorts.com when you visit the homepage
- News articles are stored in the database and displayed on the web interface
- The app fetches fresh news each time the scraping functions are called
- Images and content are dynamically loaded from the scraped data

## Recent Updates

- **Bug Fixes**: Fixed AttributeError issues in web scraping functions
- **Error Handling**: Added comprehensive error handling for missing HTML elements
- **Code Improvements**: Enhanced error resilience in both English and Hindi news scrapers

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This application is for educational purposes only. Please ensure you comply with the website's terms of service and robots.txt when scraping data.
