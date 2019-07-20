# Simple ZMQ-based Python Wrappers

This package provides simple wrappers for ZMQ Pub/Sub, Client/Server, and Push/Pull.

It sends/receives arbitrary python objects by pickling, and it is also compatible with Python 2 and 3.

See `examples` for usage.

*This package has security risks as it uses repr-eval to enable Python 2/3 string/bytes compatibility. Please use with caution.*