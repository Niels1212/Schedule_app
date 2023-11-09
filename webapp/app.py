from flask import Flask, render_template
from blueprints.employees_blueprint import employees
from blueprints.shifts_blueprint import shifts
from blueprints.requirements_blueprint import requirements
from blueprints.output_blueprint import output

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # This should be a random byte string.

app.register_blueprint(employees, url_prefix='/employees')
app.register_blueprint(shifts, url_prefix='/shifts')
app.register_blueprint(requirements, url_prefix='/requirements')
app.register_blueprint(output, url_prefix='/output')

@app.route('/')
def view():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(threaded=False)
