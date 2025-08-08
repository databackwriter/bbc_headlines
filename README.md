# BBC Headlines

A Python script to fetch and display the latest BBC News headlines using web scraping.

## Features

- Scrapes BBC News homepage for current headlines
- Outputs headlines in a readable format
- Simple command-line usage

## Requirements
- Python 3.11+
- Install dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    Or, for Conda users, from `environment.yml`:

    ```bash
    conda env create -f environment.yml
    conda activate bbc_headlines_env
    ```

Install dependencies:

## Usage

Run the script:

```bash
python bbc_headlines.py
```

## Testing

To run unit tests:

```bash
pytest tests
```

Ensure you have the required dependencies installed before running tests.

## Example Output

```
1. Headline Title 1
2. Headline Title 2
...
```

## License

MIT License

## Disclaimer

This project is for educational purposes. Please respect BBC's terms of service.