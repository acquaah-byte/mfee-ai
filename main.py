from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MFEE AI - Ghana</title>
        <style>
            body {font-family: Arial; text-align: center; padding: 50px; background: #f0f0f0;}
            h1 {color: #ff6600;}
            .box {background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px #ccc;}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>MFEE AI</h1>
            <p>Welcome to MFEE AI - Made in Ghana 🇬🇭</p>
            <p>Your AI website is LIVE!</p>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
