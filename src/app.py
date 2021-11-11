from app import app


if __name__ == "__main__":
    app.env = 'development'
    app.run(host='0.0.0.0', port=8000)
