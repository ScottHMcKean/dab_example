# Databricks Asset Bundle Example
An example of using Databricks Asset Bundles to scrape stock data and save it as a Delta table.

## Requirements
To set up a local development environment using Hatch:

1. Install Hatch:
   ```bash
   pip install hatch
   ```

2. Create a new Hatch environment:
   ```bash
   hatch env create
   ```

3. Activate the Hatch environment:
   ```bash
   hatch shell
   ```

4. Install the required packages (if not automatically installed):
   ```bash
   hatch run pip install -r requirements.txt
   ```

## Optional Developer Dependencies
To install additional dependencies for development purposes, such as linters or testing tools, use the following command:

```bash
hatch run pip install -r dev-requirements.txt
```

## Running Tests
To run tests using `pytest`, run `pytest` in the terminal.

## Code Quality Tools

### Formatting with Black
To format your code:
```bash
black .
```

To check if files would be reformatted without actually changing them:
```bash
black . --check
```

### Type Checking with MyPy
To run type checking:
```bash
mypy src
```

### Linting with Flake8
To check code style and quality:
```bash
flake8 src
```

### Running All Checks
To run all code quality checks at once:
```bash
black . --check && flake8 src && mypy src
```
