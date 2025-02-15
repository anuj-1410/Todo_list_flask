from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a list of tasks (in-memory storage)
tasks = []

@app.route('/')
def index():
    # Render the index page with the list of tasks
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    # Get the task from the form and add it to the tasks list
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    # Delete the task by its index
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

