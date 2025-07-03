# Note: All lines related to Flask-Frozen have been removed.
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# --- MAIN AND SECTION ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/introduction/')
def introduction():
    return render_template('introduction.html')

@app.route('/theoretical-framework/')
def theoretical_framework():
    return render_template('theoretical_framework.html')

@app.route('/institutional-changes/')
def institutional_changes():
    return render_template('institutional_changes.html')

@app.route('/outcomes-and-discussions/')
def outcomes_and_discussions():
    return render_template('outcomes_discussions.html')

# --- THEORETICAL FRAMEWORK SUBPAGES ---
@app.route('/theoretical-framework/new-institutional-economy/')
def new_institutional_economy():
    return render_template('new_institutional_economy.html')

@app.route('/theoretical-framework/economic-growth-from-institutional-changes/')
def economic_growth_institutional_changes():
    return render_template('economic_growth_institutional_changes.html')

@app.route('/theoretical-framework/mato-grosso-production-function/')
def mato_grosso_production_function():
    return render_template('mato_grosso_production_function.html')

# --- INSTITUTIONAL CHANGES SUBPAGES ---
@app.route('/institutional-changes/land-market/')
def land_market():
    return render_template('land_market.html')

@app.route('/institutional-changes/transports/')
def transports():
    return render_template('transports.html')

@app.route('/institutional-changes/production-function-components/')
def production_function_components():
    return render_template('production_function_components.html')

# --- OUTCOMES AND DISCUSSIONS SUBPAGES ---
@app.route('/outcomes-and-discussions/exploratory-statistics/')
def exploratory_statistics():
    return render_template('exploratory_statistics.html')

@app.route('/outcomes-and-discussions/econometric-analysis/')
def econometric_analysis():
    return render_template('econometric_analysis.html')

@app.route('/outcomes-and-discussions/demographic-analysis/')
def demographic_analysis():
    return render_template('demographic_analysis.html')

@app.route('/outcomes-and-discussions/economic-growth-21st-century/')
def economic_growth_21st_century():
    return render_template('economic_growth_21st_century.html')

# --- REFERENCES ---
@app.route('/references/')
def references():
    return render_template('references.html')

@app.route('/final-considerations/')
def final_considerations():
    return render_template('final_considerations.html')


# This section is no longer needed for production on Render,
# but it's good practice to keep it for local development.
if __name__ == '__main__':
    app.run(debug=True)