## Prerequisites:
This project requires several libraries that are listed and can be installed from requirements.txt

## Use:
The WP `username`, `password`, and `url` variables in document_transfer must be added before running the job. URL should link to the media library, i.e. wp-json/wp/v2/media
Then, run `python3 course_cronjob.py` to initiate the cronjob. The cronjob runs the tasks in document_transfer.py. It will output a file `access.txt` with the date and time everytime the job is done. 

