from app import create_app
import os
app = create_app()

if __name__ == '__main__':
    # app.run("localhost", 1001, debug=True) # local
    host = os.getenv("HOST", "127.0.0.1")
    port = os.getenv("PORT", 5000)
    debug = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(host, port, debug)
