from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import wget  # URL에서 다운로드 받는 모듈
import os

driver = webdriver.Chrome('chromedriver.exe')

time.sleep(3)
# 네이버 이동
driver.get('https://www.naver.com')

# 검색창
input_search = driver.find_element_by_id('query')
time.sleep(1)
# input_search = driver.find_element_by_name('query')
# input_search = driver.find_element_by_class_name('input_text')
# input_search = driver.find_element_by_css_selector('#query')
# input_search = driver.find_element_by_css_selector('.input_text')

# 검색어 입력
input_search.send_keys('네이버 영화')
time.sleep(1)

# 엔터키 입력
input_search.send_keys(Keys.ENTER)
time.sleep(1)

# 네이버 영화링크
link = driver.find_element_by_css_selector('.link_name')
print('Link Address:', link.get_attribute('href'))
link.click()
time.sleep(1)

# 상영자/예정작 클릭
driver.switch_to.window(driver.window_handles[-1])
running_film = driver.find_element_by_xpath('//*[@id="scrollbar"]/div[1]/div/div/ul/li[2]/a')
running_film.click()
time.sleep(1)

# 영화목록 리스트 상단 엘리먼트
ul = driver.find_element_by_class_name('lst_detail_t1')
li_list = ul.find_elements_by_tag_name('li') # lst_detail_t1 하위에 있는 li 태그 리스트
# li_list = driver.find_elements_by_tag_name('li') # 전체 li 태그 리스트

for li in li_list:
    detail_link = li.find_element_by_tag_name('a')
    detail_link = 'https://movie.naver.com' + detail_link.get_attribute('href')
    print('Detail Link:', detail_link)

    code = detail_link.split('=')[1]
    print('Code:', code)

    thumb = li.find_element_by_tag_name('img')
    thumb = thumb.get_attribute('src')
    print('Thumbnail url:', thumb)

    title = li.find_element_by_class_name('tit')

    # Rating이 존재하지 않는 영화가 있음
    # rating = title.find_element_by_tag_name('span')
    # rating = rating.text
    # print('Rating:', rating)

    try:
        rating = title.find_element_by_tag_name('span')
        rating = rating.text
        print('Rating:', rating)
    except:
        rating = ''

    title = title.find_element_by_tag_name('a')
    title = title.text
    print('Title:', title)

    if os.path.exists('./images') is False:
        os.mkdir('images')

    # Thumbnail Image
    # wget.download(thumb, './images/%s.jpg' % code)
    # Original Image
    wget.download(thumb.split('?')[0], './images/%s.jpg' % code)
    print('#' * 100)

print('Crawling is done!')
driver.quit()







