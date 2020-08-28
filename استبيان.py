from bidi.algorithm import get_display
from selenium import webdriver
import time
import arabic_reshaper
url = 'http://www.scialex.org/S/09701091-72f9-4a28-8a89-98b78c18fa3b/Student/2018'
webBrowser = webdriver.Chrome("chromedriver.exe")


def login():
    username = input('Enter username : ')
    password = input('Enter password : ')
    webBrowser.get(url)
    # time.sleep(3)
    webBrowser.find_element_by_id("InputUsername").send_keys(username)
    webBrowser.find_element_by_id("InputPassword").send_keys(password)
    webBrowser.find_element_by_id("loginAcc").click()
    time.sleep(3)


def init():
    subjectNum = int(input("How many subject ? "))
    Slist = [input('subject-'+str(i+1)+": ") for i in range(subjectNum)]
    return Slist


def start():
    webBrowser.find_element_by_link_text("السجل الأكاديمي").click()
    time.sleep(3)
    list = init()
    for i in list:
        webBrowser.find_element_by_link_text(i).click()
        time.sleep(3)
        for i in webBrowser.find_elements_by_css_selector("input[type='radio'][value='1']"):
            i.click()
        webBrowser.find_element_by_id(
            "ContentPlaceHolder1_HeadContentPlaceHolder_RegistCourseGenerlPollButton").click()


login()
start()
# init()


bidi_text = get_display(arabic_reshaper.reshape("حسن محمود حسن"))
print(bidi_text)
input(bidi_text)
# webBrowser.find_element_by_id("username").send_keys("sdf5e1sf785yyy")
# webBrowser.find_element_by_name("Passwd").send_keys("123456102030")
# webBrowser.find_element_by_name("ConfirmPasswd").send_keys("123456102030")
# webBrowser.find_element_by_class_name("CwaK9").click()
# webBrowser.find_element_by_xpath('//*[@title="التالي"]').click()
# webBrowser.find_element_by_xpath('//*[@title="التالي"]').click()
# webBrowser.find_element_by_xpath('//*[@title="التالي"]').click()
# Slist=[input('subject-'+str(i+1)+": ") for i in range(2)]
# print(Slist)
