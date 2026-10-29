from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "VIP BOT ONLINE"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    print("NOVO PAGAMENTO:")
    print(data)

    if data.get("event") == "payment.confirmed":
        print("Pagamento aprovado!")

    return {"success": True}, 200

if __name__ == "__main__":
    app.run()
