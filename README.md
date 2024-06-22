# Disney Character Data Project

This project fetches information about Disney characters from the Disney API and stores the data in a SQLite database. It also allows users to search for characters and list the films they are associated with.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- pip (Python package installer)

### Libraries to Install

Install the required libraries using pip:

```sh
pip install requests pandas sqlalchemy
```
###  Environmental Variables

No environment variables are needed for this project.

## How to Run the Code
#### Running 'panda.py'
This script fetches data for a specific character (ID: 25) from the Disney API, processes it, and stores it in a SQLite database.

To run the script:
```sh
python panda.py
```
#### Running 'test.py'
This script allows users to search for a Disney character by name and lists the films associated with that character.

To run the script:
```sh
python test.py
```
You will be prompted to enter a character name. The script will then fetch and display the list of films associated with the entered character name.

### Overview of How the Code Works
##### panda.py

  1. Fetching Data:
    - Uses the _requests_ library to fetch data from the Disney API for a character with ID 25.
  
  2. Processing Data:
    - Extracts specific data fields ('_id' and 'films') from the fetched data
    - Creates a pandas DataFrame from the extracted data.
  
  3. Storing Data:
    - Uses SQLAlchemy to create a SQLite database and store the data in a table named 'characters'.
  
  4. Querying Data:
    - Queries the 'characters' table to fetch all stored data and prints it as a pandas DataFrame.

##### test.py

  1. User Input:
    - Prompts user to enter a character name.
  
  2. Fetching Data:
    - Constructs the API URL using the base URL and the entered character name.
    - Uses the 'requests' library to fetch data from the Disney API for the specified character name.
  
  3. Processing and Displaying Data:
    - Checks the response status and processes the data if the response is successful.
    - Extracts and prints the list of films associated with the entered character name.



_This file should provide clear instructions and an overview for anyone looking to understand or use your project._

