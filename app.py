from flask import Flask, render_template, url_for, flash

app = Flask(__name__)


@app.route('/')
def main_page():
	return render_template('main_page.html')


@app.route('/documents', methods=('GET', 'POST'))
def document_page():
	return render_template('document_page.html')


@app.route('/discussion', methods=('GET', 'POST'))
def discussion_page():
	return render_template('discussion_page.html')


@app.route('/settings', methods=('GET', 'POST'))
def setting_page():
	flash_text = ''
	flash(flash_text)
	return render_template('setting_page.html')


if __name__ == '__main__':
	app.secret_key = 'admin123'
	app.run()