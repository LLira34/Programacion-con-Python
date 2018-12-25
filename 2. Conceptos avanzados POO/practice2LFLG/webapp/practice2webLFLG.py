# vspeddweb.py
from flask import Flask, render_template, request
from practice2LFLG import calculate

app = Flask(__name__)

@app.route('/speed', methods = ['POST'])
def do_search() -> 'html':
    distance = float(request.form['distance'])
    time = float(request.form['time'])
    title = 'Here are your results:'
    
    results = str(calculate(distance, time))
    return render_template('results.html',
                           the_title = title,
                           the_distance = distance,
                           the_time = time,
                           the_results = results,)

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title = 'Welcome to the calculation of speed on the web!')
 
app.run(debug = True)

