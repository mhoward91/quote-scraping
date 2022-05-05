# Quote-Scraping

Command line program, where a user receives four guesses to identify the author of a quote, aided by a series of hints.

## Description

The program uses the Beautiful Soup package to scrape data from this [website](http://quotes.toscrape.com/). It parses the HTML, identifying quote data by its class ID or anchor tab to load a list of structured tuples into memory. A quote is selected at random and displayed to the user, at which point they are prompted to input the author of the quote into the terminal.

| After the... | the outcome is... |
| --- | --- |
| First incorrect guess | the author birth date and location are displayed to the user |
| Second incorrect guess | the first letter of the author's first name is displayed to the user |
| Third incorrect guess | the first letter of the author's surname name is displayed to the user |
| Fourth incorrect guess | the correct answer is displayed and the program terminates |

## Getting Started

### Dependencies

To clone and run this app on your machine, you'll need [Git](https://git-scm.com) and [Python 3](http://python.org/).

### Installation & running the program 


1. Fork and clone this repository
```
$ git clone https://github.com/mhoward91/quote-scraping.git
```

2. Change directory to this repository
```
$ cd quote-scraping
```

3. Create and activate a virtual environment
```
$ python -m venv .venv

$ .venv\scripts\activate
```

4. Install the required packages
```
$ pip install -r requirements.txt
```

5. Run the program
```
python quote_scrape.py
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
