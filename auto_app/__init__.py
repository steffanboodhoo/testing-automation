from flask import Flask
import config
auto_app = Flask(__name__)
auto_app.secret_key = config.APP_SECRET
import routes