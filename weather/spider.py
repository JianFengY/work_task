"""
Created on 2018/5/16
@Author: Jeff Yang
"""
import requests
import re
import json

from weather.area_code import AREA_CODE


def get_html(url):
    """
    获取页面的源码
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def data_column():
    """
    返回数据字段
    """
    return {
        "actT": "温度",
        "actH": "相对湿度",
        "actR": "降水量",
        # "actW":"风力等级",
    }


def match_code_and_place():
    """
    返回代码所代表的地点
    """
    url = "http://www.tqyb.com.cn/data/gzWeather/obtDatas.js"
    html = get_html(url)
    pattern = re.compile('gz_obtDatas = (\{.*?\});\}catch\(e\)', re.S)
    data = re.findall(pattern, html)
    json_data = json.loads(data[0])
    # print(json_data)
    code_dict = {}
    for district, places in json_data['data'].items():
        for item in places:
            code_dict[item['obtid']] = item['obtName']
    return code_dict


def get_weather_data():
    """
    获取天气数据
    """
    url = "http://www.tqyb.com.cn/data/gzWeather/gz_autoStationLive.js"
    html = get_html(url)
    pattern = re.compile('gz_autoStationLive = (\{.*?\});\}catch\(e\)', re.S)
    data = re.findall(pattern, html)
    json_data = json.loads(data[0])
    print(json_data['moniDate'])  # 时段
    # print(json_data['hoursList'])  # 对应时间（小时）
    # print(json_data['data'])  # 数据
    # print(len(json_data['data']))
    # print(len(AREA_CODE))
    for k, v in json_data['data'].items():
        if k in AREA_CODE.keys():
            print(AREA_CODE[k], v['actT'][-1])


if __name__ == '__main__':
    # code_dict = match_code_and_place()
    # print(code_dict)
    get_weather_data()
