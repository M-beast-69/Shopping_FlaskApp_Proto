from flask import Flask as fk

app = fk(__name__)

@app.route('/')
def home():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)