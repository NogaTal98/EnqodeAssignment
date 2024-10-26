# Data Collection Backend

## Overview

This API is a data collection backend that allows to add and query data from a database.

## API Description

The API is a RESTful API that allows to add and quesry data from the database. The API has the following endpoints:

- `/getById` - This endpoint takes a `id` parameter and returns the data for the given id.
- `/add` - This endpoint receives a JSON object with the data to be added to the database.

## API Installation

To install the API, follow these steps:

1. Clone the repository.
2. Move to the PART 2 directory: `cd PART 4`
3. Install the required packages: `pip install -r requirements.txt`
4. Initialize the database: `python init_db.py`
5. Run the API: `flask --app api run`

## API Usage

To use the API, send a GET request to the `/getByID` or `/add` endpoint with the `url`. For example:

```bash
curl http://localhost:5000/getById?id=1
```

This will return structured data for the given id.


