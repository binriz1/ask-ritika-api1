from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "✅ Ritika Rai API is active."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_question = data.get("question", "")

    prompt = f"तपाईं Ritika Rai हुनुहुन्छ – Bichardhara.com की एक AI पत्रकार। {user_question} भन्ने प्रश्नको स्पष्ट, तथ्यमा आधारित उत्तर दिनुहोस्।"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"answer": answer})
    except Exception as e:
        print("🔥 Internal Server Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)