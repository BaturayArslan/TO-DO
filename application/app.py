from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__)
	
	if test_config:
		app.config.from_object("application.config.TestConfig")
	else:
		app.config.from_object("application.config.DevConfig")

	@app.route("/hello")
	def hello():
		return "Hello World."

	return app	