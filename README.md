# cURL/Fetch to Python Transformer

## Project Description
This project is a web application that transforms cURL or Fetch commands into Python code using either the `requests` or `httpx` libraries. It is built with FastAPI for the backend and vanilla JavaScript for the frontend.

## Installation

### Prerequisites
- Python 3.11
- Docker (optional, for containerized deployment)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

4. (Optional) Run the application using Docker:
    ```sh
    docker build -t curl-fetch-transformer .
    docker run -p 8000:8000 curl-fetch-transformer
    ```

## Usage
1. Open your web browser and navigate to `http://localhost:8000`.
2. Enter your cURL or Fetch command in the respective input field.
3. Select the target library (`requests` or `httpx`).
4. Click the "CONVERT TO PYTHON" button to generate the Python code.
5. Copy the generated code using the "Copy Result" button.

## Project Structure
- `main.py`: Entry point of the FastAPI application.
- `api/router.py`: Contains the API routes and logic.
- `api/utils.py`: Utility functions for request execution.
- `api/schemas.py`: Pydantic models for request validation.
- `static/js/main.js`: JavaScript code for frontend interactions.
- `static/css/style.css`: CSS styles for the frontend.
- `templates/index.html`: HTML template for the main page.
- `Dockerfile`: Docker configuration for containerized deployment.
- `pyproject.toml`: Configuration for code formatting and linting.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.