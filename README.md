# FastAPI and OpenAI Streaming Demonstration

This project demonstrates how to use FastAPI and OpenAI to stream output to users. It utilizes Poetry as a package manager for easy dependency management. This README file will guide you through the installation and execution of the project.

## Prerequisites

Before you can run this project, you need to have the following installed:

- Python 3.10
- Poetry (Package Manager)

## Installation

1. **Install Python 3.10**: If you don't have Python 3.10 installed, download and install it from the official Python website: https://www.python.org/downloads/

2. **Install Poetry**: Poetry is a package manager for Python. You can install it using `pip`:

   ```bash
   pip install poetry
   ```

3. **Clone the Repository**: Clone this repository to your local machine:

   ```bash
   git clone (this repo)
   ```

4. **Change Directory**: Navigate to the project directory:

   ```bash
   cd aistreaming
   ```

5. **Install Dependencies**: Use Poetry to install project dependencies:

   ```bash
   poetry install
   ```

6. **ENV File**

```
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY=xxxxx

# This is the key for the Mark 1.0 API
APP_KEY="xxxx"
```

## Usage

Now that you have installed the project and its dependencies, you can run the FastAPI application. Make sure you are in the project directory.

```bash
poetry run uvicorn main:app --reload
```

This command will start the FastAPI development server, and your API will be accessible at `http://localhost:8000`.

## API Endpoint

The FastAPI application provides a single endpoint for streaming messages from OpenAI. You can access it using the following endpoint:

- **POST** `/generate-text`

### Request Payload

To make a request to the `/generate-text` endpoint, you need to provide the following JSON payload:

```json
{
  "api_key": "api_key",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What's the weather like today?"
    }
  ]
}
```

- `api_key`: APP API key (required).
- `messages`: An array of messages in the format of the OpenAI chat API (required). It should contain a system message and user messages.

## Authors

- Chatchai Wangwiwattana <redeian@gmail.com>

Feel free to explore the project further and adapt it to your needs. If you have any questions or encounter any issues, please don't hesitate to reach out to the author.
