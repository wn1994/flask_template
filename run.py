from app import create_app
from net_setting import *
import config

app = create_app(config.user_config)

if __name__ == '__main__':
    app.run(host=DEV_HOST, port=DEV_PORT)
