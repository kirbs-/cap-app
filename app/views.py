from app import app, models
import config

import os
from flask import render_template, request, redirect, abort, flash, jsonify, url_for, send_file
import traceback


@app.route('/')
@app.route('/index')
def index():
    """Main page - Display all uploaded files."""
    return render_template('index.haml', files=models.UploadFile.all())


@app.route('/upload', methods=['POST'])
def upload():
    """File upload handler.
    
        This is confiugred to read a multipart form upload.
    """    
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file')
        return

    # grab file object from request
    f = request.files['file']

    # if user does not select file, browser also submits a empty part without filename
    if f.filename == '':
        flash('No file selcted')
        return 

    if f: # TODO add server side file extension check. e.g. allowed_file(file.filename)
        upload_file = models.UploadFile(f.filename)

        # trap any errors during file saving and show users error message if necessary.
        try:
            # save object to db
            upload_file.save()

            # save actual file to file system.
            # TODO validate file format.
            f.save(upload_file.absolute_path)
        except:
            flash("Error saving file.")
            traceback.print_exc()
        
        return render_template('file-table-row.haml', files=[upload_file]) # pass table row partial

@app.route('/download')
def download():
    file_name = request.args.get('file_name')
    if file_name:
        return send_file(models.UploadFile.find_by_name(file_name), as_attachment=True, attachment_filename=file_name)


@app.route('/display-csv/<file_name>')
def dislay_csv(file_name):
    """Fetch part of the file for display

    The main work here is handle by the model. #to_html is a pandas function. No need to write a template.
    See https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.to_html.html
    """
    return models.UploadFile.find_by_name(file_name).head().to_html(classes='table', index=False)


@app.route('/stats/<file_name>')
def stats(file_name):
    """Fetch yearly aggregate counts for display."""
    return models.UploadFile.find_by_name(file_name).agg_by_year().to_html(classes='table')