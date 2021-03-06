import selenium
from selenium import webdriver
import urllib
import urllib.request
from selenium.common.exceptions import NoSuchElementException
import argparse

# Global Var for New Episode handling
NEW_EP = True

# 폴더
target_dir = '[img] 프로야구 생존기'

# 제목
name = '프로야구생존기'
# 몇화까지
ep_start = 1
ep_end = 1
ep_idx = 0
new_ep = 214

# 첫화 URL
if NEW_EP:
    URL = f'https://github.com/seungkilee-cs/fuck-kakao-page/blob/master/%5Bmd%5D%20%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC%20%EC%83%9D%EC%A1%B4%EA%B8%B0/{new_ep:03}.md'
else:
    URL = f'https://github.com/seungkilee-cs/fuck-kakao-page/blob/master/%5Bmd%5D%20%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC%20%EC%83%9D%EC%A1%B4%EA%B8%B0/{ep_start:03}.md'

# 크롬 드라이버 셋업
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'D:\Utility\chromedriver\chromedriver.exe', options=options)
driver.implicitly_wait(time_to_wait=1)
driver.get(URL)

print("\n\nWarning: 본 프로그램은 오직 카카오의 비상식적인 컨텐츠 소유정책에 대한 해법으로서 작성되었습니다. 저작권 법을 지키면서 사용하십시오.\n\n")

print(name + '을 다운로드 시작합니다\n')

if NEW_EP:
    print(f'{new_ep:03}' + '화를 다운로드 중 ...')
    img_num = 1
    while True:
        try:
            img = driver.find_element_by_xpath('//*[@id="readme"]/article/p[1]/a[' + str(img_num) + ']/img')
            src = img.get_attribute('src')
            urllib.request.urlretrieve(src, f'./{target_dir}/{name}_{new_ep:03}화_{img_num:03}.jpg')

        except NoSuchElementException:
            print("All image downloaded\n\n")
            break

        img_num = img_num + 1

else:
    links = ['https://github.com/seungkilee-cs/fuck-kakao-page/blob/master/%5Bmd%5D%20%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC%20%EC%83%9D%EC%A1%B4%EA%B8%B0/' + f'{x:03}' + '.md' for x in range(ep_start, ep_end+1)]

    for ep in range(ep_start, ep_end+1):
        print(str(ep) + '화를 다운로드 중 ...')
        img_num = 1
        while True:
            try:
                img = driver.find_element_by_xpath('//*[@id="readme"]/article/p[1]/a[' + str(img_num) + ']/img')
                src = img.get_attribute('src')
                urllib.request.urlretrieve(src, f'./{target_dir}/{name}_{ep:03}화_{img_num:03}.jpg')

            except NoSuchElementException:
                print("All image downloaded\n\n")
                break

            img_num = img_num + 1

        driver.get(links[ep_idx])
        ep_idx += 1

    # If I need to crawl random url progression
    # next_ep = driver.find_element_by_xpath(r'//*[@id="readme"]/article/p[2]/a[2]')
    # next_ep.click()

print("\n\nWarning: 본 프로그램은 오직 카카오의 비상식적인 컨텐츠 소유정책에 대한 해법으로서 작성되었습니다. 저작권 법을 지키면서 사용하십시오.\n\n")
print("P.S.\n\n")
print("씨발 카카오 좆같은 것들아 내가 이겼다 凸(^0^)凸")