# HTTP Server Implementation

A multi-threaded HTTP server built from scratch in Python as part of the CodeCrafters tutorial series. Handles basic GET and POST requests with file operations.

## Features

- Multi-threaded request handling
- Supports HTTP/1.1 protocol
- Implements common HTTP methods:
  - GET for resource retrieval
  - POST for file creation
- File operations with directory parameter
- Proper HTTP status codes (200, 201, 404)
- Content-Type and Content-Length headers

## Usage

1. Start the server:
`python server.py`

2. With directory argument (for file operations):
`python server.py --directory /path/to/files/`

## Endpoints

- `/` - Basic health check
- `/echo/<message>` - Returns the message back
- `/files/<filename>` - File operations:
  - GET: Retrieves file contents
  - POST: Creates/updates file

## Example Requests

Get echo response:
`curl http://localhost:4221/echo/hello`

Get file contents:
`curl http://localhost:4221/files/sample.txt`

Post file contents:
`curl -X POST -d "file content" http://localhost:4221/files/sample.txt`

## Technical Details

- Uses Python's built-in `socket` module
- Thread-per-request model
- Handles basic HTTP headers
- Simple request routing
- File I/O operations

## Requirements

- Python 3.6+
- No external dependencies

## Notes

- Developed as part of CodeCrafters HTTP Server Challenge
- Basic implementation focused on core HTTP functionality
- Not production-grade (missing many HTTP features)
