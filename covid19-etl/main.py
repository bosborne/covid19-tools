import os

from importlib import import_module

if __name__ == "__main__":
    base_url = "http://revproxy-service"
    token = os.environ.get("ACCESS_TOKEN")
    if not token:
        raise Exception(
            "Need ACCESS_TOKEN environment variable (token for user with read and write access)"
        )

    job_name = os.environ.get("JOB_NAME")
    if not job_name:
        raise Exception(
            "Need JOB_NAME environment variable (specification on which ETL job to run)"
        )

    job_module = job_name.lower()
    job_class = job_name.upper()

    etl_module = import_module(f"etl.{job_module}")
    etl = getattr(etl_module, job_class)

    job = etl(base_url, token)
    job.files_to_submissions()
    job.submit_metadata()
