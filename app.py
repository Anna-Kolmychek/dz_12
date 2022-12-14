from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint, search_blueprint
from loader.views import post_form_blueprint, post_uploaded_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(post_form_blueprint, url_prefix='/post')
app.register_blueprint(post_uploaded_blueprint, url_prefix='/post')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

