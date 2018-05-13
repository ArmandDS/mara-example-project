"""Configures what to download from bigquery"""

import pathlib

import bigquery_downloader.config
from mara_config.config_system import patch

import app.config


@patch(bigquery_downloader.config.data_sets)
def data_sets():
    return [
        bigquery_downloader.config.DataSet(
            query_file_path=pathlib.Path('app/bigquery_downloader/pypi-downloads.sql'),
            json_credentials_path='app/bigquery_downloader/bigquery-credentials.json',
            first_date=app.config.first_date(),
            output_file_name='pypi/downloads-v1.csv.gz',
            use_legacy_sql=False,
            data_dir=app.config.data_dir()),
        bigquery_downloader.config.DataSet(
            query_file_path=pathlib.Path('app/bigquery_downloader/github-repo-activity.sql'),
            json_credentials_path='app/bigquery_downloader/bigquery-credentials.json',
            first_date=app.config.first_date(),
            output_file_name='github/repo-activity-v1.csv.gz',
            use_legacy_sql=False,
            data_dir=app.config.data_dir())
    ]
