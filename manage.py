from app import manager, db, app

if __name__ == '__main__':
    db.init_app(app)
    manager.run()
