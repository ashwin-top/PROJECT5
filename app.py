from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    age = int(request.form['age'])
    gender = request.form['gender'].lower()
    
    if age <= 22:
        category = 'Intern'
    else:
        category = 'Employee'
    
    result = f'{gender.capitalize()} {category}!'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
