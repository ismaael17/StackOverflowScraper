
# StackOverflow Scraper API

## Overview

This is a Flask-based REST API that scrapes data from the StackOverflow website using BeautifulSoup. The API provides information about questions, including tags, owner details, answer counts, view counts, and whether an answer has been accepted. The data is dynamically scraped from StackOverflow in real-time.

## Features

- Scrapes questions from StackOverflow, including:
  - Tags
  - Owner details (reputation, user ID, profile link, etc.)
  - Answer count and view count
  - Whether the question has an accepted answer
  - Metadata such as question creation date, last activity date, and score
- Outputs data in a structured JSON format
- Handles edge cases where certain elements may be missing

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/stackoverflow-scraper-api.git
   cd stackoverflow-scraper-api
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

## Usage

Once the API is running, you can access it via HTTP requests. Below is an example of how to use the API.

### Endpoints

#### `GET /questions`

Fetches a list of StackOverflow questions with details such as tags, owner information, answer count, view count, etc.

##### Example Request

```bash
curl http://127.0.0.1:5000/questions
```

##### Example Response

```json
{
  "items": [
    {
      "tags": ["c#", ".net"],
      "owner": {
        "account_id": 60430,
        "reputation": 6042,
        "user_id": 180493,
        "user_type": "registered",
        "accept_rate": 81,
        "profile_image": "https://www.gravatar.com/avatar/17f6876079483f54c5ff4977f65f9997?s=256&d=identicon&r=PG",
        "display_name": "TimS",
        "link": "https://stackoverflow.com/users/180493/tims"
      },
      "is_answered": true,
      "view_count": 1419,
      "accepted_answer_id": 3469245,
      "answer_count": 3,
      "score": 3,
      "last_activity_date": 1724334801,
      "creation_date": 1269598893,
      "last_edit_date": 1724334801,
      "question_id": 2522436,
      "link": "https://stackoverflow.com/questions/2522436/net-sdk-or-samples-for-opensrs-api",
      "closed_date": 1365835201,
      "closed_reason": "off topic",
      "title": ".Net SDK or samples for OpenSRS API?"
    }
  ]
}
```

## Project Structure

```
.
├── app.py                     # Main Flask app
├── stackoverflow_scraper.py    # Scraper logic
├── requirements.txt            # Python dependencies
└── README.md                   # Project README
```

## Dependencies

- **Flask**: Python microframework for creating web APIs.
- **BeautifulSoup**: Python library for parsing HTML and scraping web data.
- **Requests**: Python library for making HTTP requests.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Thanks to [StackOverflow](https://stackoverflow.com) for providing such a valuable resource for developers.
- This project was built using [Flask](https://flask.palletsprojects.com/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).
