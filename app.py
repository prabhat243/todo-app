from flask import Flask, request, redirect
app = Flask(__name__)

todos = []

@app.route("/")
def home():
    items = "".join(f'<li>{t} <a href="/delete/{i}">❌</a></li>' for i, t in enumerate(todos))
    return f"""
    <html>
    <head><title>Todo App</title>
    <style>
      body {{ font-family: Arial; max-width: 500px; margin: 60px auto; background: #f0f4f8; }}
      h1 {{ color: #2d3748; }}
      input {{ padding: 8px; width: 70%; border: 1px solid #cbd5e0; border-radius: 4px; }}
      button {{ padding: 8px 16px; background: #4299e1; color: white; border: none; border-radius: 4px; cursor: pointer; }}
      ul {{ list-style: none; padding: 0; }}
      li {{ background: white; padding: 12px; margin: 8px 0; border-radius: 6px; display: flex; justify-content: space-between; }}
      a {{ color: red; text-decoration: none; }}
    </style>
    </head>
    <body>
      <h1>📝 My Todo App</h1>
      <form action="/add" method="post">
        <input name="task" placeholder="Add a new task..." required/>
        <button type="submit">Add</button>
      </form>
      <ul>{items}</ul>
      
    </body>
    </html>"""

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todos.append(task)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)