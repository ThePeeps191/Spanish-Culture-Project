needed_flask = [
	"Flask",
	"render_template",
	"redirect",
	"url_for",
	"request"
]
for needed_import in needed_flask:
	exec(f"from flask import {needed_import}")

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/festivals/")
def festivals():
	return render_template("festivals.html")

@app.route("/geography/")
def geography():
	return render_template("geography.html")

@app.route("/facts/")
def facts():
	return render_template("facts.html")

@app.route("/sources/<page>")
def sources(page):
	page = page.lower()
	if page == "all":
		return render_template("sources.html")
	elif page == "geography":
		return render_template("sources/geography.html")
	elif page in ["home", "index"]:
		return render_template("sources/index.html")
	elif page in ["list-of-cities", "list_of_cities"]:
		return render_template("sources/list_of_cities.html")
	elif "fact" in page:
		return render_template("sources/facts.html")
	elif "festival" in page:
		return render_template("sources/festivals.html")
	else:
		return render_template("404.html")

@app.route("/sources/")
def sources_no_arg():
	return redirect(url_for("sources", page="all"))

@app.route("/list-of-cities/")
def list_of_cities():
	return render_template("list_of_cities.html")
@app.route("/list_of_cities")
def list_of_cities_underscores():
	return redirect(url_for("list_of_cities"))

@app.route("/weblinks/")
def weblinks():
	return render_template("weblinks.html")
@app.route("/web-links/")
def web_links():
	return redirect(url_for("weblinks"))
@app.route("/web_links/")
def web_links_():
	return redirect(url_for("weblinks"))

@app.route("/about/")
def about_us():
	return render_template("about_us.html")
@app.route("/about_us/")
def about_us_():
	return redirect(url_for("about_us"))
@app.route("/about-us/")
def about_us__():
	return redirect(url_for("about_us"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8080)





'''
<link rel="icon"
      type="image/ico"
      href="static/favicon.ico">
'''