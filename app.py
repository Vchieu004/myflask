from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Chào mừng đến với Lab 3</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f2f2f2;
            }
            .navbar {
                background: linear-gradient(90deg, #4CAF50, #2196F3, #9C27B0);
                color: white;
                padding: 30px;
                text-align: center;
                box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
            }
            .navbar h1 {
                margin: 0;
                font-size: 2em;
            }
            .navbar p {
                font-size: 1.2em;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="navbar">
            <h1>🎉 Chào mừng Võ Công Hiếu - MSSV 22DH111085 🎉</h1>
            <p>Chào mừng đến với Lab 3 - Hãy sẵn sàng học tập và khám phá!</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    # Đọc PORT từ Render hoặc fallback về 5000 khi chạy local
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
