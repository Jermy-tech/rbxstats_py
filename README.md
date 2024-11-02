# RBXStats API Client

[![PyPI version](https://badge.fury.io/py/rbxstats-api.svg)](https://badge.fury.io/py/rbxstats-api)

A Python client for the RBXStats API, providing easy access to a variety of Roblox-related offsets, exploits, game information, and more. This package allows developers to integrate with RBXStats API effortlessly.

## Features

- Retrieve all Roblox offsets in JSON or plain text.
- Access specific offsets by name or prefix.
- Fetch camera offsets and game-specific information.
- Query available exploits and their statuses.
- Supports various data formats (JSON or plain text).
- Simple, flexible class-based design.

## Installation

Install the package via pip:

```bash
pip install rbxstats
```

## Usage

Import the client, initialize it with your API key, and use its methods to interact with different RBXStats API endpoints.

### Quick Start

```python
from rbxstats import RbxStatsClient

# Initialize the client
client = RbxStatsClient(api_key="YOUR_API_KEY")

# Get all offsets in JSON format
all_offsets = client.offsets.get_all()
print(all_offsets)

# Get a specific offset by name in plain text
specific_offset = client.offsets.get_offset_by_name_plain("RenderToEngine")
print(specific_offset)

# Get all camera-related offsets in JSON format
camera_offsets = client.offsets.get_camera()
print(camera_offsets)

# Get a list of all undetected exploits
undetected_exploits = client.exploits.get_undetected()
print(undetected_exploits)
```

## API Reference

Each endpoint is encapsulated in its own class within the `RbxStatsClient`. Here’s a rundown of available classes and methods.

### 1. `Offsets`

Methods to access Roblox offsets.

- **Get all offsets**
  ```python
  client.offsets.get_all()
  ```
  Returns all offsets in JSON format.

- **Get all offsets in plain text**
  ```python
  client.offsets.get_all_plain()
  ```
  Returns all offsets in plain text format.

- **Get a specific offset by name**
  ```python
  client.offsets.get_offset_by_name("RenderToEngine")
  ```
  Returns a single offset in JSON format by name.

- **Get a specific offset by name in plain text**
  ```python
  client.offsets.get_offset_by_name_plain("RenderToEngine")
  ```

- **Get offsets by prefix**
  ```python
  client.offsets.get_offsets_by_prefix("Camera")
  ```

- **Get camera-related offsets**
  ```python
  client.offsets.get_camera()
  ```
  Returns all camera-related offsets in JSON format.

### 2. `Exploits`

Methods to get current Roblox exploit data.

- **Get all exploits**
  ```python
  client.exploits.get_all()
  ```

- **Get Windows exploits**
  ```python
  client.exploits.get_windows()
  ```

- **Get Mac exploits**
  ```python
  client.exploits.get_mac()
  ```

- **Get undetected exploits**
  ```python
  client.exploits.get_undetected()
  ```

- **Get detected exploits**
  ```python
  client.exploits.get_detected()
  ```

- **Get free exploits**
  ```python
  client.exploits.get_free()
  ```

### 3. `Versions`

Methods to get the latest and future versions of Roblox.

- **Get the latest Roblox version**
  ```python
  client.versions.get_latest()
  ```
  Returns the latest version information for Windows and Mac in JSON format.

- **Get the future Roblox version**
  ```python
  client.versions.get_future()
  ```
  Returns the upcoming version information for Windows and Mac in JSON format.

### 4. `Game`

Retrieve game-specific information based on game ID.

- **Get game details by ID**
  ```python
  client.game.get_game_by_id(12345)
  ```
  Replace `12345` with the desired game ID.

## Error Handling

API calls that fail will raise an exception with a description of the issue. Make sure to handle exceptions, especially if you’re working with user-provided input or network-dependent environments.

Example:

```python
try:
    offsets = client.offsets.get_all()
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