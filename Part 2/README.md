# Darkweb Scanner API

## Overview

This API is a darkweb scanner that allows you to scan a website in darkweb api. It implements a cURL-based API that can query dark web data relevant to a specified domain or company. It uses the IntelX API to scan the website and return structured results.

## API Description

The API is a RESTful API that uses cURL to query the IntelX API. The API takes a domain or company name as input and returns structured results from the IntelX API. The API is implemented in Python using the Flask framework.
The API has the following endpoints:

- `/info` - This endpoint takes a domain or company name as input and returns structured results from the IntelX API. Parameters:
  - `url` - The domain or company name to scan.
  - `limit` - The number of results to return (default is 100).

## API Installation

To install the API, follow these steps:

1. Clone the repository.
2. Move to the PART 2 directory: `cd PART 2`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the API: `flask --app api run`

## API Usage

To use the API, send a GET request to the `/info` endpoint with the `url` parameter set to the domain or company name you want to scan. For example:

```bash
curl http://localhost:5000/info?url=example.com
```

This will return structured results from the IntelX API for the domain `example.com`.


