# RBXStats API Client

[![PyPI version](https://badge.fury.io/py/rbxstats.svg)](https://badge.fury.io/py/rbxstats)

A Python client for the RBXStats API, providing easy access to various Roblox-related data like offsets, exploits, game information, and more. This package allows developers to integrate with the RBXStats API effortlessly, now with advanced error handling and customization options.

## Features

- Retrieve Roblox offsets, exploits, game information, and version data.
- Enhanced error handling for network issues, JSON decoding, and HTTP errors.
- Customizable headers and request timeouts for flexible integration.

## Installation

Install the package via pip:

```bash
pip install rbxstats
```

## Usage

Import the client, initialize it with your API key, and use its methods to interact with different RBXStats API endpoints.

### Quick Start

```python
from rbxstats_api import RbxStatsClient

# Initialize the client
client = RbxStatsClient(api_key="YOUR_API_KEY")

# Get all offsets
all_offsets = client.offsets().all()
print(all_offsets)

# Get a specific offset by name
specific_offset = client.offsets().by_name("RenderToEngine")
print(specific_offset)

# Get undetected exploits
undetected_exploits = client.exploits().undetected()
print(undetected_exploits)
```

## Customization Options

You can add custom headers or adjust the request timeout to suit your application’s needs.

- **Custom Headers**: Use the `set_headers` method to add or update headers dynamically.
- **Request Timeout**: Use the `set_timeout` method to set a custom timeout (in seconds) for requests.

Example:

```python
# Initialize the client
client = RbxStatsClient(api_key="YOUR_API_KEY")

# Customize headers and timeout
client.set_headers({"X-Custom-Header": "MyHeaderValue"})
client.set_timeout(10)  # Set a custom timeout (in seconds)
```

## API Reference

Each endpoint is encapsulated in its own class within the `RbxStatsClient`. Here’s an overview of the available classes and methods.

### Offsets

Methods to access Roblox offsets.

- **Get all offsets**  
  ```python
  client.offsets().all()
  ```

- **Get a specific offset by name**  
  ```python
  client.offsets().by_name("RenderToEngine")
  ```

- **Get offsets by prefix**  
  ```python
  client.offsets().by_prefix("Camera")
  ```

- **Get camera-related offsets**  
  ```python
  client.offsets().camera()
  ```

### Exploits

Methods to get current Roblox exploit data.

- **Get all exploits**  
  ```python
  client.exploits().all()
  ```

- **Get undetected exploits**  
  ```python
  client.exploits().undetected()
  ```

- **Get free exploits**  
  ```python
  client.exploits().free()
  ```

### Versions

Methods to get the latest and future versions of Roblox.

- **Get the latest Roblox version**  
  ```python
  client.versions().latest()
  ```

- **Get the future Roblox version**  
  ```python
  client.versions().future()
  ```

### Game

Retrieve game-specific information based on game ID.

- **Get game details by ID**  
  ```python
  client.game().by_id(12345)
  ```

## Error Handling

This client includes robust error handling for common issues:

- **HTTP Errors**: Handles client and server errors (e.g., 404 Not Found, 500 Internal Server Error).
- **Timeouts**: Prevents requests from hanging indefinitely.
- **JSON Decoding Errors**: Manages cases where the response isn’t a valid JSON.

Error responses are returned as structured JSON with details about the issue:

```python
try:
    offsets = client.offsets().all()
except Exception as e:
    print(f"An error occurred: {e}")
```

## Dependencies

This package requires `requests` to handle HTTP requests. It will be automatically installed as a dependency.

## Development

If you’d like to contribute, clone the repository and install the dependencies:

```bash
git clone https://github.com/Jermy-tech/rbxstats_api
cd rbxstats_api
pip install -e .
```

### Running Tests

You can add tests in the `tests/` directory (not included in this setup). Run tests using `pytest`:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
