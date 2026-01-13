from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent').lower()
    device_type = 'other'
    
    if 'iphone' in user_agent or 'ipad' in user_agent or 'macintosh' in user_agent:
        device_type = 'apple'
    elif 'android' in user_agent:
        device_type = 'android'
    elif 'windows' in user_agent:
        device_type = 'windows'

    return render_template('index.html', device_type=device_type)

@app.route('/download/profile')
def download_profile():
    return send_from_directory('static', 'wifi.mobileconfig', 
                               mimetype='application/x-apple-aspen-config',
                               as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)