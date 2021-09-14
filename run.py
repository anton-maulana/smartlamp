import sys
import os
import logging

moddir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
sys.path.append(moddir)


# print(moddir)

from logging.handlers import RotatingFileHandler
from smartlamp import create_app

app = create_app()

if __name__ == "__main__":    
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'smartlamp.log')
    handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

app.run(debug=True, host='0.0.0.0', port=5002)