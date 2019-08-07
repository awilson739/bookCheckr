from flask import Flask
app = Flask(__name__)

books = []
@app.route("/")
def hello():
  return "Hello World!"

@app.route("/add_book/<book>", methods=["POST"])
def add_book(book):
  books.append(book)
  return "ok",200
@app.route("/list_books")
def list_book():
  for i in books:
    return i

if __name__ == "__main__":
  app.run()
