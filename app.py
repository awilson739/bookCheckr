from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/add_book")
def add_book(Book book):
    pass
@app.route("/list_books")
def list_book():
    pass

if __name__ == "__main__":
  app.run()
