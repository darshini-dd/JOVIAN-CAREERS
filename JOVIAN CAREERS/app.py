from flask import Flask,render_template,jsonify

app=Flask(__name__)

JOBS=[
    {
        'id': 1,
        'title':'Data Analyst',
        'location': 'Bengaluru,India',
        'salary':'Rs. 10,00,000',
    },
    {
        'id': 2,
        'title':'Data Scientist',
        'location': 'Delhi,India',
        'salary':'Rs. 12,00,000',
    },
    {
        'id': 3,
        'title':'Backend Engineer',
        'location': 'Remote',
        'salary':'Rs. 9,00,000',
    },
    {
        'id': 4,
        'title':'Frontend Engineer',
        'location': 'Mumbai, India',
        'salary':'Rs. 5,00,000',
    }
]
@app.route("/")
def hello_jovian():
    return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__=='__main__':
    app.run(debug=True)