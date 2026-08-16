from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)
leads = [] # This saves client emails

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
    </style>
</head>
<body>
    <div class="hero">
        <h1>MFEE AI</h1>
        <p style="font-size:20px;">We build AI Assistants that answer customers, book appointments, and grow your business</p>
        <p>🇬🇭 Made in Ghana | Built for Africa</p>
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

CHAT = """
<!DOCTYPE html>
<html>
<head><title>Chat with MFEE AI</title>
<style>
body {font-family:Arial; background:#0F172A; color:white; padding:20px; text-align:center;}
#chatbox {background:#1E293B; width:90%; max-width:600px; margin:20px auto; padding:20px; border-radius:15px; height:400px; overflow-y:scroll; text-align:left;}
.msg {margin:10px 0; padding:10px; border-radius:10px;}
.user {background:#FF6B35; color:white; text-align:right;}
.bot {background:#334155; color:white;}
input {width:70%; padding:12px; border-radius:8px; border:none;}
button {padding:12px 20px; background:#FF6B35; color:white; border:none; border-radius:8px; cursor:pointer;}
</style>
</head>
<body>
<h1>Talk to MFEE AI Demo</h1>
<div id="chatbox"><div class="msg bot">Hello! I'm MFEE AI. I help Ghanaian businesses automate with AI. Ask me about pricing, WhatsApp bots, or anything!</div></div>
<input id="userInput" placeholder="Ask me anything...">
<button onclick="sendMsg()">Send</button>
<br><br><a href="/" style="color:#FF6B35;">← Back Home</a>

<script>
function sendMsg(){
  let input = document.getElementById('userInput');
  let msg = input.value;
  if(msg=='') return;
  document.getElementById('chatbox').innerHTML += `<div class="msg user">${msg}</div>`;
  input.value='';
  fetch('/get_reply', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({message:msg})})
  .then(res => res.json())
  .then(data => {
    document.getElementById('chatbox').innerHTML += `<div class="msg bot">${data.reply}</div>`;
    document.getElementById('chatbox').scrollTop = document.getElementById('chatbox').scrollHeight;
  });
}
</script>
</body></html>
"""

CONTACT = """
<!DOCTYPE html>
<html>
<head><title>Book a Call - MFEE AI</title>
<style>
body {font-family:Arial; background:#0F172A; color:white; padding:50px; text-align:center;}
form {background:#1E293B; padding:40px; border-radius:15px; width:90%; max-width:500px; margin:auto;}
input {width:90%; padding:12px; margin:10px 0; border-radius:8px; border:none;}
button {padding:15px 30px; background:#FF6B35; color:white; border:none; border-radius:8px; font-weight:bold; cursor:pointer;}
</style>
</head>
<body>
<h1>Book a Free AI Consultation</h1>
<p>Let us build an AI assistant for your business</p>
<form id="leadForm">
<input type="text" id="name" placeholder="Your Name" required><br>
<input type="email" id="email" placeholder="Your Email" required><br>
<input type="text" id="whatsapp" placeholder="WhatsApp Number" required><br>
<button type="submit">Book My Free Call</button>
</form>
<p id="msg"></p>
<a href="/" style="color:#FF6B35;">← Back Home</a>

<script>
document.getElementById('leadForm').onsubmit = function(e){
  e.preventDefault();
  let data = {name: name.value, email: email.value, whatsapp: whatsapp.value};
  fetch('/save_lead', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(data)})
  .then(res => res.json())
  .then(d => {document.getElementById('msg').innerHTML = "✅ Thank you! We'll WhatsApp you in 24 hours."});
}
</script>
</body></html>
"""

@app.route('/')
def home():
    return render_template_string(HOME)

@app.route('/chat')
def chat():
    return render_template_string(CHAT)

@app.route('/contact')
def contact():
    return render_template_string(CONTACT)

@app.route('/get_reply', methods=['POST'])
def get_reply():
    data = request.json
    user_msg = data['message'].lower()
    if 'price' in user_msg or 'cost' in user_msg:
        reply = "Our AI Chatbots start from GHS 500/month. They handle customer questions 24/7 and save you 10+ hours. Want me to book you a free demo call?"
    elif 'whatsapp' in user_msg:
        reply = "Yes! We build WhatsApp AI assistants that auto-reply in English, Twi, and Ga. Click 'Book a Call' and we’ll set it up for you."
    elif 'hello' in user_msg or 'hi' in user_msg:
        reply = "Hi there! 👋 I'm MFEE AI. What kind of business do you run? I can show you how AI can help."
    else:
        reply = "Great question! MFEE AI builds custom AI tools for African businesses. Click 'Book a Call' and let's talk."
    return jsonify({'reply': reply})

@app.route('/save_lead', methods=['POST'])
def save_lead():
    data = request.json
    leads.append(data)
    print("NEW LEAD:", data) # You can see leads in Render logs
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run()
