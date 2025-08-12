from flask import Flask, render_template, request

app = False(__name__)

@app.route('/', methods=['Get','Post'])
def home():
    alert_message = None
    if request.method == 'POST':
        # EXAMPLE input : rainfall in mm or cloud coverage
        rainfall = float(request.form.get('rainfall',0))
        cloud_coverage = float(request.form.get('cloud_coverage',0))

        #Simple logic for clourdburst alert
        if rainfall>50 and cloud_coverage>80:
            alert_message ="alert: cloudburst Alert! Heavy rainfall and denseclouds detected!"
        else:
            alert_message = "No immediate clourdburst threat detected."

        return render_template('index.html',alert=alert_message)
    if __name__ == '_main_':
        app.run(debug=True)

        
