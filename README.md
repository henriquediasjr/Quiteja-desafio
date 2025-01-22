# How to Run the Script and API

This guide explains how to run the provided Python script to process data and start the Flask API.

## Prerequisites

Before you start, make sure you have the following installed:
- Python (3.8 or later)
- Pip (Python package manager)

## Steps to Set Up and Run

### 1. Set Up a Virtual Environment
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the following commands to create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # For macOS/Linux
   myenv\Scripts\activate     # For Windows
    ```

### 2. Install Required Libraries
After activating the virtual environment, install the necessary Python libraries:
```bash
pip install pandas flask
```


### 3. Prepare the Files
1. Place the dados.zip file in the same directory as the script.
2. Ensure that dados.zip contains the following files:
    - origem-dados.csv
    - tipos.csv

### 4. Run the Script
Run the Python script using the following command:
```bash
python app.py
```

### 5. Check the Generated Files
- After running the script, a file named insert-dados.sql will be generated in the same directory.
- This file contains SQL INSERT statements based on the processed data.


### 6. Use the Flask API
The Flask API will start running locally on http://127.0.0.1:5000. You can test it using the following endpoints:

#### Get Tipo by ID
Fetch the name of a type based on its ID:

```bash
curl http://127.0.0.1:5000/tipo/<id>
```

Replace <id> with the desired type ID. For example:

```bash
curl http://127.0.0.1:5000/tipo/1
```

### 7. Stop the API
To stop the API, press CTRL+C in the terminal where the script is running.

Happy coding! 🚀
