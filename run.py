import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from tkinter import messagebox
import tkinter

# 驱动Chrome
dailiip = "222.74.202.229"
port = "8080"
options = webdriver.ChromeOptions()
driverpath = "D:\Chromedriver\chromedriver.exe"
# 设置具体信息m16375s
user_infos = ['18971439847#fl123456#32001', '15849432483#5201314long#32002', '13879753340#lzy961657389#32003',
              '15104861316#5201314long#32004', '15995934681#fl123456#32005',
              '15849296246#5201314long#32006', '15540021477#5201314long#32007', '18516657120#lianlian521#18888']
driver = None

# 设置不超时直接运行
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"


def run(isvritual, begin=0, end=0):
    if isvritual:
        options.add_argument("--proxy-server=http://27.190.80.120:8888")
        options.add_argument(
            '--user-agent=Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
        try:
            driver = webdriver.Chrome(executable_path=driverpath, chrome_options=options)
            print("Google驱动器驱动成功！")
        except:
            print("Google驱动器驱动失败，请检查文件位置以及版本号是否正确！")
            exit()
    else:
        try:
            driver = webdriver.Chrome(executable_path=driverpath)
            print("Google驱动器驱动成功！")
        except:
            print("Google驱动器驱动失败，请检查文件位置以及版本号是否正确！")
            exit()
    try:
        driver.get("https://yd.520e.com.cn/")
    except:
        print("打开网页超时，请检查网址是否正确！")
    try:
        print("--------------------第【%d】轮begin--------------------" % (begin / 3 + 1))
        wait_num = 0
        while(True):
            time.sleep(1)
            wait_num += 1
            if wait_num > 4 or driver.find_elements_by_class_name("layui-layer-btn0") != None:
                break
        time.sleep(1)
        for i in range(begin, end):
            time.sleep(2)
            user_info = user_infos[i]
            wel_win = driver.find_elements_by_class_name("layui-layer-btn0")[0]
            wel_win.click()
            xiaomi_win = driver.find_elements_by_class_name("nav-item")[1]
            xiaomi_win.click()
            WebDriverWait(driver, 50).until(EC.element_to_be_clickable([By.ID, "xiaomi_submit"]))
            print("->\t用户【" + user_info.split('#')[0] + "】开始执行。。。")
            user_name = driver.find_element_by_id("xiaomi_mobile")
            user_name.clear()
            user_name.send_keys(user_info.split("#")[0])
            password = driver.find_element_by_id("xiaomi_password")
            password.clear()
            password.send_keys(user_info.split("#")[1])
            step = driver.find_element_by_id("xiaomi_count")
            step.clear()
            step.send_keys(user_info.split("#")[2])
            # 提交并反馈信息
            submit = driver.find_element_by_id("xiaomi_submit")
            submit.click()
            WebDriverWait(driver, 50).until(EC.presence_of_element_located([By.CLASS_NAME, "layui-layer-btn0"]))
            result = driver.find_elements_by_class_name("layui-layer-ico2")
            if len(result) == 0:
                alert_info = "执行成功"
            else:
                alert_info = "执行失败"
            close = driver.find_elements_by_class_name("layui-layer-btn0")[0]
            close.click()
            print("\t\t执行完毕！执行结果：【" + alert_info + ":" + user_info.split("#")[2] + "】")
            driver.refresh()
    except Exception as e:
        print("网站页面可能改版！请手动检查！")
        print(e)
    finally:
        print("--------------------第【%d】轮end--------------------" % (begin / 3 + 1))
        # time.sleep(1)
    driver.quit()


def main():
    for i in range(3):
        if i < 2:
            run(False, i * 3, i * 3 + 3)
            root = tkinter.Tk()
            messagebox.showinfo("提示", "已执行完第【%d】轮,点击【确定】开启下一轮" % (i + 1))
            root.destroy()
        else:
            run(False, i * 3, i * 3 + 1)
    # 单个执行
    # run(False, 2, 3)

# run(True, 3, 6)  # 虚拟ip执行
# run(False, 0, 3)        # 真实ip执行
if __name__ == '__main__':
    main()
