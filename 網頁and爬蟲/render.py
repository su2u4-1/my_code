import flask, time

app = flask.Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return flask.render_template("home.html")


@app.route("/web.1")
@app.route("/web/1")
@app.route("/web1")
def web1():
    return flask.render_template("web1.html")


@app.route("/show.<name>", methods=["GET"])
@app.route("/show/<name>", methods=["GET"])
def show(name):
    return f"<html><body><h1>{name}</h1><h3><a href='http://127.0.0.1:5000'>home</a></h3></body></html>"


@app.route("/time")
def t():
    while True:
        t = time.localtime()
        return flask.render_template(
            "time.html", ti=f"{t[0]}/{t[1]}/{t[2]} {t[3]}:{t[4]}:{t[5]}"
        )


@app.route("/道德經")
def TaoTeChing():
    return flask.render_template("道德經.html")


@app.route("/質數.<n>", methods=["GET"])
@app.route("/質數/<n>", methods=["GET"])
def PrimeNumber(n):
    n = int(n)
    if n < 0:
        a = "Error"
    elif n == 2:
        a = True
    elif n == 1 or n == 0:
        a = False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                a = False
                break
        else:
            a = True
    if a == "error":
        a = "輸入錯誤"
    elif a:
        a = f"{n}是質數"
    else:
        a = f"{n}不是質數"
    return f"<html><body><h1>{a}</h1><h3><a href='http://127.0.0.1:5000'>home</a></h3></body></html>"


if __name__ == "__main__":
    app.run()
