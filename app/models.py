from app import db
import config

import os
import traceback
from datetime import datetime
import uuid
from werkzeug.utils import secure_filename
import pandas as pd


class UploadFile(db.Model):
    """File upload model.

    Attributes:
        id (str): database primary key
        file_name (str): sanitized file name. NOTE: file_name must be unique.
        created_at (datetime): database sysdate record was created

    """
    id = db.Column(db.String(250), primary_key=True)
    file_name = db.Column(db.String(1000), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, file_name):
        # sanitize file name before storing
        self.file_name = secure_filename(file_name)
        self.id = str(uuid.uuid4())

    @classmethod
    def all(cls):
        """Returns all upload files."""
        return cls.query.all()

    @classmethod
    def find_by_name(cls, file_name):
        """Returns upload file for given file name."""
        return cls.query.filter_by(file_name=file_name).first()

    @property
    def absolute_path(self):
        """Returns absolute path of file."""
        return os.path.join(config.UPLOAD_FOLDER, self.file_name)

    def save(self):
        """Save upload file object to db."""
        # update
        self.updated_at = datetime.now()

        # save to db
        # TODO add error handling here
        db.session.add(self)
        db.session.commit()

    @property
    def df(self):
        """Load csv into memory.

        Also performs limited data cleaning
            - Fills blank state values with "BLANK"
            - Converts "date" column to datetime dtype

        Returns:
            DataFrame: CSV file
        """
        return pd.read_csv(
            self.absolute_path, 
            parse_dates=['date'], 
            infer_datetime_format=True
        ).fillna({'state': 'BLANK'})

    def head(self, **kwargs):
        """Returns rows from begining of CSV to display.

        Args:
            rows (int, optional): number of rows to display. Defaults to 20.

        Returns:
            DataFrame: Dataframe limited to number of rows.
        """
        rows_to_display = kwargs.get('rows_to_display', 20)
        return self.df.head(rows_to_display)

    def agg_by_year(self):
        """Returns CSV aggregated by year based on 'date' column.

        Returns:
            DataFrame: Data frame aggregated by year and sorted descending by number of records.
        """
        tmp_df = self.df.groupby(self.df.date.dt.year).agg({'guid': 'count'}).sort_values(by='guid', ascending=False).reset_index()
        tmp_df.columns = ['year','guid']
        return tmp_df