import os
from config.config import app_config
from app import create_app

config_name = os.getenv("FLASK_ENV")

app = create_app(app_config[config_name])


if __name__ == '__main__':
    app.run(debug=True)
