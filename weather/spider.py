"""
Created on 2018/5/16
@Author: Jeff Yang
"""
import requests
import re
import json
import datetime

from weather.area_code import AREA_CODE
from config.db_config import conn


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
    code_area = {}
    value_list = []
    dict = {
        'panyu': '番禺区',
        'yuexiu': '越秀区',
        'liwan': '荔湾区',
        'huadu': '花都区',
        'haizhu': '海珠区',
        'tianhe': '天河区',
        'baiyun': '白云区',
        'huangpu': '黄埔区',
        'zengcheng': '增城区',
        'conghua': '从化区',
        'nansha': '南沙区'
    }
    for district, places in json_data['data'].items():
        for item in places:
            value_list.append(dict[district])
            value_list.append(item['obtName'])
            code_area[item['obtid']] = value_list.copy()
            value_list.clear()
    return code_area


def get_weather_data():
    """
    获取天气数据
    """
    url = "http://www.tqyb.com.cn/data/gzWeather/gz_autoStationLive.js"
    html = get_html(url)
    pattern = re.compile('gz_autoStationLive = (\{.*?\});\}catch\(e\)', re.S)
    data = re.findall(pattern, html)
    json_data = json.loads(data[0])
    # print(json_data['moniDate'])  # 时段
    print(json_data['moniDate'][-14:-1] + ':00:00')
    # print(json_data['hoursList'])  # 对应时间（小时）
    # print(json_data['data'])  # 数据
    # print(len(json_data['data']))
    # print(len(AREA_CODE))

    cursor = conn.cursor()
    try:
        for k, v in json_data['data'].items():
            if k in AREA_CODE.keys():
                # print(AREA_CODE[k], v['actT'][-1])
                # 2018-05-16 15时 至 2018-05-17 14时
                dt = json_data['moniDate'][-14:-1] + ':00:00'
                time = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
                sql = "INSERT INTO weather (district, area, temperature, time) VALUES ('%s','%s','%s','%s')" % (
                    AREA_CODE[k][0], AREA_CODE[k][1], v['actT'][-1] if v['actT'][-1] else '', time)
                cursor.execute(sql)
                print(AREA_CODE[k][1], "插入成功！")
                conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    # code_area = match_code_and_place()
    # print(code_area)
    get_weather_data()
