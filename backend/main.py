from flask import Flask, render_template, send_file, request
import os

app = Flask(__name__)

# 检测file目录是否存在
if not os.path.exists("file"):
    os.makedirs("file")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/v1/get_file_list", methods=["GET"])
def get_file_list():
    # 遍历查找防止分不清文件和目录
    file_list = []
    for item in os.listdir("file"):
        if os.path.isfile(os.path.join("file", item)):
            file_list.append({"name": item, "type": "file"})
        elif os.path.isdir(os.path.join("file", item)):
            file_list.append({"name": item, "type": "dir"})
        
    return {"file_list": file_list}

@app.route("/api/v1/download_file/<filename>", methods=["GET"])
def download_file(filename):
    return send_file(os.path.join("file", filename), as_attachment=True)

@app.route("/api/v1/upload_file", methods=["POST"])
def upload_file():
    # 从请求中获取文件
    file = request.files["file"]
    # 保存文件到指定目录
    file.save(os.path.join("file", file.filename))
    return {"message": "upload_file"}

@app.route("/api/v1/delete_file/<filename>", methods=["DELETE"])
def delete_file(filename):
    # 删除指定文件
    file_path = os.path.join("file", filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"message": "delete_success"}
    else:
        return {"message": "file_not_found"}, 404


if __name__ == "__main__":
    app.run(debug=True)