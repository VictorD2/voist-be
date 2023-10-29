from chat.routes import chat_bp
from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask
from waitress import serve


class App:
    def __init__(self, port=4001):
        load_dotenv()
        self.port = port
        self.app = Flask(__name__)
        self.config()
        self.routes()

    def config(self):
        CORS(self.app)
        # self.app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
        # self.app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")


    def routes(self):
        # self.app.register_blueprint(contact_bp)
        # self.app.register_blueprint(folder_bp)
        # self.app.register_blueprint(class_bp)
        # self.app.register_blueprint(user_bp)
        # self.app.register_blueprint(auth_bp)
        self.app.register_blueprint(chat_bp)

    def run(self):
        if __name__ == "__main__":
            print("SERVER ON PORT " + str(self.port))
            serve(self.app, port=self.port)
            print("SERVER ON PORT " + str(self.port))
            # self.app.run(port=self.port, debug=True)


App().run()
