# merch-distribution

This is the merchandise distribution system for BPHC, with a centralised database using RethinkDB.

## Installation

Clone the repository and cd into the folder.
Run the command `pip3 install -r requirements.txt`

Then go to the [RethinkDB Website](https://www.rethinkdb.com/docs/install/) and install the driver application for your operating system.

## Running the server

Into a new terminal window, type `rethinkdb --bind all`
From a browser window, you can access the dashboard at http://localhost:8080/

## Adding to a database

From the dashboard, navigate to the Tables tab, and add a database called test, if it doesn't exist already.
Then, in a terminal window different from the one that has the server running, run the command `python3 maketable.py /path/to/tshirt.txt`
The database with the details should now be ready.


