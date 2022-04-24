import requests
import random
import sys
from bs4 import BeautifulSoup
from time import sleep


def _make_request(site):
    response = requests.get(site)
    my_soup = BeautifulSoup(response.text, "html.parser")
    return my_soup


def scrape():
    next_page = True
    url = "http://quotes.toscrape.com"
    master_quotes = []

    while next_page:
        soup = _make_request(url)
        all_quotes = soup.find_all(class_="quote")
        for quote in all_quotes:
            text = quote.find(class_="text").get_text()
            author = quote.find(class_="author").get_text()
            bio_url = quote.find("a")["href"]
            master_quotes.append([text, author, bio_url])

        next_page = soup.find(class_="next")
        new_url = next_page.find("a")["href"] if next_page else None
        url = f"https://quotes.toscrape.com{new_url}"
        sleep(2)

    return master_quotes


def author_bio(site):
    soup_object = _make_request(site)
    birth_date = soup_object.find(class_="author-born-date").get_text()
    birth_location = soup_object.find(class_="author-born-location").get_text()
    first_name = soup_object.find(class_="author-title").get_text()[0]
    last_name_prep = soup_object.find(class_="author-title").get_text()
    last_name = last_name_prep.split()[1][0]
    return f"Here's a hint: The author was born on {birth_date} {birth_location}", \
        f"Here's a hint: The author's first name starts with {first_name}", \
        f"Here's a hint: The author's last name starts with {last_name}"


def play_game():
    print("Scraping, be patient!")
    print()
    quote_list = scrape()
    selected_quote = random.choice(quote_list)
    guesses_remaining = 4
    print(selected_quote[0])
    answer = None
    while answer != selected_quote[1]:
        if guesses_remaining == 0:
            print(f"You have not guessed correctly. The correct answer is {selected_quote[1]}. Game over!")
            sys.exit(0)
        print(f"Who said this? Guesses remaining: {guesses_remaining} ")
        bio_url = f"https://quotes.toscrape.com{selected_quote[2]}"
        if guesses_remaining == 3:
            print(author_bio(bio_url)[0])
        elif guesses_remaining == 2:
            print(author_bio(bio_url)[1])
        elif guesses_remaining == 1:
            print(author_bio(bio_url)[2])
        answer = input()
        guesses_remaining -= 1

    play_again = ""
    print("You guessed correctly! Congratulations!")
    while play_again.casefold() not in ("y", "n", "yes", "no"):
        play_again = input("Would you like to play again (y/n)? ")
    if play_again.casefold() in ("no", "n"):
        print("Ok! See you next time!")
    else:
        play_game()


play_game()
