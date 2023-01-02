#!/usr/bin/env python
from app import app
from config import DevConfig as config


# That "if" cycle starting server with debugging
if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
