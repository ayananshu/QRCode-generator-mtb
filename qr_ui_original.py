from flask import Flask, render_template, request, redirect
import qrcode
import io
import base64
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__, static_url_path='/static')

# Configure logging
if not app.debug:
    # Set up a file handler with rotation
    file_handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    file_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

@app.route('/show_qr')
def show_qr():
    url = request.args.get('url')
    app.logger.info('Generating QR code for URL: %s', url)  # Log the request

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img_io = io.BytesIO()
        img.save(img_io)
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return render_template('index2.html', img_data=img_base64)
    except Exception as e:
        app.logger.error('Error generating QR code: %s', str(e))  # Log the error
        return render_template('error.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        images = [image for image in os.listdir('static/images') if
                  image.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))]

        if request.method == 'POST':
            url = request.form['url']
            app.logger.info('Received URL for QR code generation: %s', url)  # Log the request
            return redirect(f'/show_qr?url={url}')

        return render_template('index3.html', images=images)
    except Exception as e:
        app.logger.error('Error on index page: %s', str(e))  # Log the error
        return render_template('error.html'), 500

if __name__ == '__main__':
    app.run(debug=True)