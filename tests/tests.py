import pathlib
import sys

# This is a hack to load the flask app into behave's context
# Grab the current file and go up one levels. This is the app/repo's root.
app_root_dir = str(pathlib.Path(__file__).parents[1])
# insert into python sys path so app module is importable.
sys.path.insert(0, app_root_dir)

import unittest
from hamcrest import *
from app import models


class TestUploadFile(unittest.TestCase):
    """Upload File unit tests"""

    def test_agg_by_year(self):
        """Test yearly aggregation of upload file."""
        upload_file = models.UploadFile('example.csv')
        
        # validate first data row, first column is 1911 and 1264.
        assert_that(upload_file.agg_by_year().loc[0][0], equal_to([1911]))

         # validate first data row, second column is 1264.
        assert_that(upload_file.agg_by_year().loc[0][1], equal_to([1264]))


if __name__ == '__main__':
    unittest.main()