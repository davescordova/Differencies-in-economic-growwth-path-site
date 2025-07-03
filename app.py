import sys
from flask import Flask, render_template
from flask_frozen import Freezer # Import the Freezer class

# Initialize the Flask application
app = Flask(__name__)
# Optional: Set the destination folder to 'docs', ideal for GitHub Pages.
# If you prefer the 'build' folder, you can remove or comment out the line below.
app.config['FREEZER_DESTINATION'] = 'docs'
# Added to ensure trailing slash URLs work correctly
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True


# Initialize the Freezer with your application
freezer = Freezer(app)

# --- MAIN AND SECTION ROUTES ---
# The root route already works correctly as an index.
@app.route('/')
def index():
    return render_template('index.html')

# Added a trailing slash to indicate it's a directory/index.
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


# Modified to handle freezing or running the server
if __name__ == '__main__':
    # Check if the 'freeze' argument was passed on the command line
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        print("Starting the site freezing process...")
        freezer.freeze() # This line runs the freezer
        print("Static site successfully generated in the 'docs/' folder.")
    else:
        # If no argument is passed, start the development server
        print("Starting development server at http://127.0.0.1:5000")
        print("Use 'python app.py freeze' to generate the static version.")
        app.run(debug=True)
