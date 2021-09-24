from typing import Optional
from flask import Flask, render_template

app = Flask(
	__name__,
	static_url_path='/static',
	static_folder='static',
	template_folder="templates"
)


@app.route("/")
@app.route("/<string:name>")
def index(name: Optional[str] = None):
	if not name:
		message = "Пидор кто ты?!"
	else:
		message = f"Привет красотулька, {name}!"
	return render_template('index.html', message=message)


if __name__ == "__main__":
	app.run()
