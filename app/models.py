from app import db
import config

import glob
import traceback
from datetime import datetime
import uuid
from werkzeug.utils import secure_filename


class UploadFile(db.Model):
    """[summary]

    Args:
        db ([type]): [description]

    Returns:
        [type]: [description]
    """
    id = db.Column(db.String(250), primary_key=True, default=uuid.uuid4)
    file_name = db.Column(db.String(1000), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, file_name, **kwargs):
        self.file_name = secure_filename(file_name)

    @property
    def all(self):
        return self.query.all()

