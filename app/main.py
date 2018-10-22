from os import environ, path
from flask import Flask, render_template, send_from_directory

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update({
        "variable_start_string": "[[",
        "variable_end_string": "]]"
    })
app = CustomFlask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    contentful_api_token = environ.get('CONTENTFUL_API_TOKEN')
    contentful_space_id = environ.get('SPACE_ID')
    
    return render_template('index.html', 
                           space=contentful_space_id, 
                           token=contentful_api_token)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
