from app import manager, app
from common.db import db

if __name__ == '__main__':
    db.init_app(app)
    manager.run()
