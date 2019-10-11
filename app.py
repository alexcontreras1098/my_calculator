from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Loan Calculator')

@app.route('/calculate', methods=['GET', 'POST'])
def loan():
    if request.method == 'POST':
        form = request.form
        A = int(form['Loan_Amount'])
        n = int(form['Years'])*12
        i = float(form['Interest_Rate'])/12
        D = (((1+i)**n)-1)/(i*(1+i)**n)
        Payment =  A/D
        return render_template('index.html', display=Payment, pageTitle='Loan Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
