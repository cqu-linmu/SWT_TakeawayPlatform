from flask import Flask
from flask import render_template

app = Flask(
    __name__,
    # 这里是相对路径，不然找不到文件。
    template_folder="./frontend/dist",  # 修改默认的HTML文件夹
    static_folder="./frontend/dist",  # 修改默认的静态文件文件夹
    static_url_path=""
)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()