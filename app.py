from flask import Flask, render_template, send_from_directory

# Initialize the Flask application
app = Flask(__name__, static_folder=None)

# --- DEVELOPMENT CONFIGURATIONS ---
# Force templates to automatically reload when you save them in VS Code
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Disable caching for static files (CSS, Images, etc.) so the browser always fetches the newest version
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# --- IN-MEMORY CSS CACHE ---
# style.css is read once into memory here, at startup, instead of being
# re-read from the FUSE-mounted Google Drive folder on every request.
# This avoids the flaky/partial reads that were causing ERR_CONTENT_LENGTH_MISMATCH.
# NOTE: if you edit static/style.css, restart the server to pick up the change.
with open('static/style.css', 'rb') as f:
    STYLE_CSS = f.read()

# --- MAIN ROUTES ---

# The root route now correctly displays your main presentation page.
@app.route('/')
def index():
    return render_template('index.html')

# This is the entry point to the dissertation pages
@app.route('/dissertation/')
def dissertation():
    # This will render the new dissertation welcome page
    return render_template('dissertation.html')


# --- DISSERTATION SECTION ROUTES ---
# These routes are necessary for the navigation links inside the dissertation pages to work.

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

# --- Articles ---
@app.route('/articles')
def articles():
    return render_template('articles.html')

# --- REFERENCES ---
@app.route('/references/')
def references():
    return render_template('references.html')

@app.route('/final-considerations/')
def final_considerations():
    return render_template('final_considerations.html')

# --- STATIC FILE ROUTES ---

# style.css is served from memory (see STYLE_CSS above) to avoid FUSE read issues.
# This specific route takes precedence over the generic one below for this exact path.
@app.route('/static/style.css', endpoint='static_style')
def static_style():
    return STYLE_CSS, 200, {'Content-Type': 'text/css'}

# All other static files (images, pdfs, etc.) are still served normally from disk,
# with conditional=False to avoid range-request (206) handling on the FUSE mount.
# endpoint='static' preserves url_for('static', filename=...) working exactly as before.
@app.route('/static/<path:filename>', endpoint='static')
def static_files(filename):
    return send_from_directory('static', filename, conditional=False)


# This section is good practice to keep for local development.
if __name__ == '__main__':
    # reloader_type='stat' uses polling instead of inotify, which is more
    # reliable when the project lives on a FUSE-mounted filesystem (Google Drive)
    app.run(debug=True, reloader_type='stat')
