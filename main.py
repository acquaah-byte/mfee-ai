from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MFEE AI - Made in Ghana 🇬🇭</title>
        <style>
            body {font-family: Arial; background: #f5f5f5; text-align: center; padding: 50px;}
            .box {background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);}
            h1 {color: #FF6B35;}
            .btn {background: #FF6B35; color: white; padding: 12px 25px; border-radius: 8px; text-decoration: none; margin: 10px; display: inline-block;}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>MFEE AI</h1>
            <p>Welcome to MFEE AI - Made in Ghana 🇬🇭</p>
            <p>Your AI Business Assistant</p>
            <a href="/services" class="btn">Our Services</a>
            <a href="/contact" class="btn">Contact Us</a>
            <a href="/chat" class="btn">Chat with AI</a>
        </div>
    </body>
    </html>
    """

@app.route('/services')
def services():
    return "<div style='padding:50px'><h1>Our Services</h1><p>1. AI Chatbots<br>2. Website Automation<br>3. Business AI Tools</p><a href='/'>Back Home</a></div>"

@app.route('/contact')
def contact():
    return "<div style='padding:50px'><h1>Contact MFEE AI</h1><p>Email: hello@mfee.ai<br>WhatsApp: +233 XXX</p><a href='/'>Back Home</a></div>"

@app.route('/chat')
def chat():
    return "<div style='padding:50px'><h1>Chat with MFEE AI</h1><p>Coming Soon! Our AI will reply to you here.</p><a href='/'>Back Home</a></div>"

if __name__ == "__main__":
    app.run()
