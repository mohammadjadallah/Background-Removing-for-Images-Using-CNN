# dependencies
from flask import Flask, render_template, request, send_file, \
    make_response, redirect, url_for
import os 
import shutil
# Importing Required Modules
from rembg import remove
from PIL import Image
import io

# Create instance
app = Flask(__name__)

# HTML file
index = "index.html"

@app.route('/', methods=['GET', 'POST'])
def render():
    # remove the two directories temp and output
    if os.path.exists("static/temp"):
        shutil.rmtree(os.path.join("static", "temp"), )
    if os.path.exists("static/output"): 
        shutil.rmtree(os.path.join("static", "output"))

    if request.method == 'POST':

        # remove the two directories temp and output
        if os.path.exists("static/temp"):
            shutil.rmtree(os.path.join("static", "temp"), )
        if os.path.exists("static/output"): 
            shutil.rmtree(os.path.join("static", "output"))

        # Get the selected image file from the form data
        selected_file = request.files.get('selected_file')
        
        # Save the selected file to a temporary directory on the server
        temp_dir = 'temp'
        output_dir = 'output'
        os.makedirs(f"static/{temp_dir}", exist_ok=True)
        os.makedirs(f"static/{output_dir}", exist_ok=True)

        selected_file.save(os.path.join("static", temp_dir, selected_file.filename))
        
        # Store path of the image in the variable input_path
        input_path = os.path.join("static", temp_dir, selected_file.filename)

        # Store path of the output image in the variable output_path
        output_path = 'output.png'

        # Processing the image
        input = Image.open(input_path)

        # Removing the background from the given Image
        output = remove(input)

        # Saving the image in the given path
        output.save(os.path.join("static", output_dir, output_path))

        # Send the output image in the response
        # This block for handling the headers...
        output_data = io.BytesIO()
        output.save(output_data, format='PNG')
        output_data.seek(0)

        response = make_response(output_data.getvalue())
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'inline', filename='output.png')

        return redirect(url_for('output'))

    return render_template(index)


@app.route('/output')
def output():
    return send_file(os.path.join("static", "output", "output.png"), as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
