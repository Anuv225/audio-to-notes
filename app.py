from flask import Flask, render_template, request, redirect
import tempfile
import os
from speechToSummary import createSummary, createTranscript

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ""
    summary = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        # If no file is uploaded
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        
        # If the user uploads a blank file
        if file.filename == "":
            return redirect(request.url)

        # Create a temporary directory to store the uploaded file
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, file.filename)

        # Save the uploaded file to the temporary directory
        file.save(temp_file_path)

        transcript = createTranscript(temp_file_path)
        summary = createSummary(transcript)

    return render_template('index.html', transcript=transcript, summary=summary)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
