from flask import Flask

app = Flask(__name__)
@app.route('/api/item/<item_id>', methods=['GET'])
def get_path_item(item_id):
    output = ""
    path_item = item_id
    output += f"<h1>{path_item}</h1>"
    return output

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)