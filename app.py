from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

guestbook_entries = [
    {"name": "แอดมินบอท", "message": "ยินดีต้อนรับสู่ระบบสอบถามข้อมูล!"}
]

@app.route('/')
def index():
    return render_template('index.html', entries=guestbook_entries)

@app.route('/send', methods=['POST'])
def send_message():
    user_name = request.form.get('name')
    user_message = request.form.get('message')

    if user_name and user_message:
        new_entry = {"name": user_name, "message": user_message}
        guestbook_entries.append(new_entry)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)