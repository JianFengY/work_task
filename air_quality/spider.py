"""
Created on 2018/5/16
@Author: Jeff Yang
"""
import requests
import json
import re


def get_html(url, data):
    """
    获取页面的源码（post请求）
    """
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.text
    return None


def get_data():
    """
    获取空气质量数据
    """
    url = "http://210.72.1.216:8080/gzaqi_new/MapData.cshtml"
    data = {'OpType': 'GetAllRealTimeData'}
    # result = '{"data":'+get_html(url, data)+'}'
    result = get_html(url, data)
    pattern = re.compile(r'new Date\((?P<datetime>\d*?)\)', re.S)
    result = pattern.sub(r'\g<datetime>', result)
    # print(result)
    list_data = json.loads(result)
    for item in list_data:
        print(item['DWNAME'], item['AQI'], item['QUALITY'], item['PRIMARY'], item['Msg'])


if __name__ == '__main__':
    get_data()
