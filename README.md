# Quote-Scraping

Command line app, where a user receives four guesses to identify the author of a quote, aided by a series of hints.

## Description

The program uses the Beautiful Soup package to scrape quote data from this [website](http://quotes.toscrape.com/). It parses the HTML, identifying data by its class ID or anchor tab to load a list of structured tuples into memory. A quote is selected at random and displayed to the user, at which point they are prompted to input the author of the quote into the terminal.

- After the first incorrect guess, the author birth date and location are displayed to the user as a hint
- After the second incorrect guess, the first letter of the author's first name is displayed to the user as a hint
- After the third incorrect guess, the first letter of the author's surname name is displayed to the user as a hint
- After the fourth incorrect guess, the correct answer will display and the program will terminate

## Getting Started

### Dependencies

To clone and run this app, you'll need [Git](https://git-scm.com) and a [Python 3 installation](http://python.org/).

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
