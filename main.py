from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HOME = """
<!DOCTYPE html>
<html>
<head>
    <title>MFEE AI - AI Solutions for African Businesses 🇬🇭</title>
    <style>
        body {font-family: 'Segoe UI', Arial; margin:0; background:#0F172A; color:white;}
        .hero {text-align:center; padding:80px 20px; background:linear-gradient(135deg, #FF6B35, #F97316);}
        h1 {font-size:48px; margin:0;}
        .btn {background:white; color:#FF6B35; padding:15px 30px; border-radius:10px; text-decoration:none; font-weight:bold; margin:10px; display:inline-block;}
        .section {padding:60px 20px; text-align:center; background:#1E293B;}
        .cards {display:flex; justify-content:center; gap:20px; flex-wrap:wrap;}
        .card {background:#334155; padding:30px; border-radius:15px; width:280px;}
        .orange {color:#FF6B35;}
    </style>
</head>
<body>
    <div class="hero">
        <h1>MFEE AI</h1>
        <p style="font-size:20px;">We build AI Assistants that answer customers, book appointments, and grow your business</p>
        <p class="orange">Made in Ghana 🇬🇭 | Built for Africa</p>
        <a href="/chat" class="btn">Try AI Demo</a>
        <a href="/contact" class="btn">Book a Call</a>
    </div>
    
    <div class="section">
        <h2>What We Do</h2>
        <div class="cards">
            <div class="card"><h3>🤖 AI Chatbots</h3><p>24/7 customer support in English, Twi, Ga</p></div>
            <div class="card"><h3>📱 WhatsApp Automation</h3><p>Auto-reply customers on WhatsApp</p></div>
            <div class="card"><h3>📊 Business AI Tools</h3><p>Save 10+ hours per week</p></div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME)

@app.route('/services')
def services():
    return "<div style='padding:50px; color:white; background:#0F172A;'><h1>Our Services</h1><p>AI Chatbots, WhatsApp Automation, Business Tools</p><a href='/'>Back Home</a></div>"

@app.route('/contact')
def contact():
    return "<div style='padding:50px; color:white; background:#0F172A;'><h1>Book a Call</h1><p>Email: hello@mfee.ai<br>WhatsApp: +233 XXX</p><a href='/'>Back Home</a></div>"

@app.route('/chat')
def chat():
    return "<div style='padding:50px; color:white; background:#0F172A; text-align:center;'><h1>Talk to MFEE AI Demo</h1><p>Ask me anything about your business!</p><p>[AI Chat coming in Step 2]</p><a href='/'>Back Home</a></div>"

if __name__ == "__main__":
    app.run()
