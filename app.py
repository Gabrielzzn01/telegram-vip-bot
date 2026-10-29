from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Nexus Pag Online!"

@app.route("/webhook", methods=["POST"])
def webhook():

    dados = request.json

    print(dados)

    return {
        "status": "ok"
    }, 200

if __name__ == "__main__":
    app.run()
