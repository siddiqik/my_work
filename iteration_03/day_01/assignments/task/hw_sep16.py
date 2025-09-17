from flask import Flask, request
import requests

app = Flask(__name__)

API_URL = "http://colormind.io/api/"

@app.route("/")
def home():
    return """
        <h1> Colormind Palette</h1>
        <form action="/palette">
            <label>Choose model:</label>
            <select name="model">
                <option value="default">Default</option>
                <option value="ui">UI</option>
                <option value="nature">Nature</option>
            </select>
            <button type="submit">Generate</button>
        </form>
    """

@app.route("/palette")
def palette():
    model = request.args.get("model", "default")
    data = {"model": model}
    r = requests.post(API_URL, json=data)

    if r.status_code == 200:
        return str(r.json())
    else:
        return f"Error: {r.status_code}"

if __name__ == "__main__":
    app.run(debug=True)
