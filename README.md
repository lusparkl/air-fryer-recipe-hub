# Air Fryer Recipe Hub 🍗

A sophisticated web scraping system that collects and organizes air fryer recipes from popular cooking websites. Built with Python, this project automates recipe collection, standardizes formats, and uses AI for intelligent categorization.

## 🚀 Features

- Automated recipe collection from major cooking websites
- Intelligent recipe categorization using AI
- Standardized recipe format and storage
- Nutritional information parsing
- Cooking time calculations
- Database storage and management

## 🛠 Tech Stack

- Python 3.8+
- BeautifulSoup4 for web scraping
- Selenium for dynamic content
- SQLAlchemy + MySQL for data storage
- FastAPI for API endpoints
- OpenAI for recipe categorization
- Pytest for testing

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL Server
- Chrome WebDriver for Selenium

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/air-fryer-recipe-hub.git
cd air-fryer-recipe-hub
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with:
```env
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=airfryer_recipes
OPENAI_API_KEY=your_openai_key
```

## 🚦 Usage

1. Initialize the database:
```bash
python setup_db.py
```

2. Run the scraper:
```bash
python main.py
```

## 📊 Supported Websites

- AllRecipes
- EatingWell
- SeriousEats
- SimplyRecipes
- SpruceEats

## 🧪 Testing

Run tests using pytest:
```bash
pytest
```

## 📝 Project Structure

```
app/
├── ai/                 # AI integration components
├── db/                 # Database models and CRUD operations
└── scrapers/          # Web scraping implementations
    ├── _abstract.py   # Abstract base classes
    ├── _utils.py      # Utility functions
    └── [sites].py     # Site-specific scrapers
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## ✨ Acknowledgments

- Recipe websites for providing valuable content
- OpenAI for AI capabilities
- Python community for amazing libraries