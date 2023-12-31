# src/LoggingMicroServ/app/app.py
from flask import Flask, request, after_this_request

app = Flask(__name__)

# Create a logger
import logging
from logging.handlers import RotatingFileHandler

# Configure logging to write to a shared file
log_handler = RotatingFileHandler(r'src\LoggingMicroserv\app\log_files\shared.log', maxBytes=10000, backupCount=1)
log_handler.setLevel(logging.INFO)
app.logger.addHandler(log_handler)

# @app.before_request
# def log_request_info():
#     app.logger.info('Request URL: %s', request.url)
#     app.logger.info('Request method: %s', request.method)
#     app.logger.info('Request headers: %s', request.headers)
#     app.logger.info('Request data: %s', request.data)

@app.route('/upload', methods=['POST'])
def log_response_info(response):
    app.logger.info('Response status: %s', response.status)
    app.logger.info('Response headers: %s', response.headers)
    app.logger.info('Response data: %s', response.get_data(as_text=True))
    return response


# Log 404 errors
@app.errorhandler(404)
def page_not_found(e):
    app.logger.error('404 Error: %s' % e)
    return "404 - Not Found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5007)
