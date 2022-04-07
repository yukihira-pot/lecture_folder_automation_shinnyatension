from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from settings import CHROME_DRIVER_DIR, ECS_ID, PASSWORD, BASE_DIR

print(CHROME_DRIVER_DIR)
driver = webdriver.Chrome(CHROME_DRIVER_DIR)

def Login_KULASIS():
    driver.get("https://www.k.kyoto-u.ac.jp/student/la/top")
    driver.set_window_size(750, 1000)

    ecs_id = driver.find_element(by=By.NAME,  value="j_username")
    ecs_id.send_keys(ECS_ID)

    password = driver.find_element(by=By.NAME, value="j_password")
    password.send_keys(PASSWORD)

    login_btn = driver.find_element(by=By.NAME, value="_eventId_proceed")
    login_btn.click()

    sleep(2)

def proceed_to_timeslot_list():
    driver.get("https://www.k.kyoto-u.ac.jp/student/la/timeslot/timeslot_list")
    sleep(1)

def create_lecture_folders():
    base_dir = BASE_DIR
    cnt = 0
    lecture_set = set()
    lectures = driver.find_elements(by=By.XPATH, value='//a[contains(@href, "student")]')

    for lecture in lectures:
        name = str(lecture.get_attribute("title")).rstrip()
        if len(name) == 0 or name in lecture_set:
            continue
        lecture_set.add(name)
        cnt += 1
        dir_name = str(cnt) + "_" + name
        new_dir = base_dir + str(dir_name)
        os.mkdir(new_dir)
    
    driver.close()

def main():
    Login_KULASIS()
    proceed_to_timeslot_list()
    create_lecture_folders()

if __name__ == "__main__":
    main()
