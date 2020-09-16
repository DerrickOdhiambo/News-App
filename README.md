# News App

- A news application that uses the news API to fetch the current news updates from various news sources.

## User Stories

- To see various news sources
- Select a news source and see all news articles from it.
- See the image, description and time the news was posted
- Click on an article and read the full article on the source website.

## Installation

### Requirements

- Python3.6 or a later version

#### Cloning

- Open the terminal/command prompt
- `git clone https://github.com/DerrickOdhiambo/News-App.git`
- `cd News-App`
- `code` or open through your preferred editor.

#### Running the application

- Run the following commands
- `python3.6 -m venv --without-pip virtual` to install the virtual environment
- `source virtual/bin/activate` to activate virtual environment
- `curl https://bootstrap.pypa.io/get-pip.py | python` donload the latest version of pip
- `pip install flask` install flask
- `chmod a+x start.sh`
- `./start.sh`

## Behavior Driven Development

| Behavior                            | Input                          | Output                                               |
| ----------------------------------- | ------------------------------ | ---------------------------------------------------- |
| Application loads                   | Clicks on the home button      | Displays news sources and a segment of trending news |
| Selects a news source               | Clicks on ABC News             | Displays various news articles on ABC News           |
| User wants to read the full article | Clicks on the read more button | Displays the whoe article on the main source website |

## Technologies Used

- Python/Flask

## Known bugs

- Some of the codes were very repeatative
- Some news articles do not have images

## Contact Information

- Email: odhiamboderrick56@gmail.com

## License

MIT License

Copyright (c) [2020] [DerrickOdhiambo]
