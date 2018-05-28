"""
Created on 2018/5/16
@Author: Jeff Yang
"""
import requests
import json
import re
import time
import datetime

from config.db_config import conn

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

    cursor = conn.cursor()
    try:
        for item in list_data:
            # print(item['DWNAME'], item['AQI'], item['QUALITY'], item['PRIMARY'], item['Msg'])
            ts = item['AQITIME'] / 1000
            dt = time.localtime(ts)
            t = time.strftime("%Y-%m-%d %H:%M:%S", dt)
            sql = "INSERT INTO air_quality (area, so2_1h, so2_24h, no2_1h, no2_24h, pm10_1h, pm10_24h, co_1h, co_24h, o3_1h, pm2_5_1h, pm2_5_24h, AQI, quality, primary_, msg, time) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                item['DWNAME'], item['SO2_1H'], item['SO2_24H'], item['NO2_1H'], item['NO2_24H'], item['PM10_1H'],
                item['PM10_24H'], item['CO_1H'], item['CO_24H'], item['O3_1H'], item['PM2_5_1H'], item['PM2_5_24H'],
                item['AQI'], item['QUALITY'], item['PRIMARY'], item['Msg'], t)
            cursor.execute(sql)
            print(item['DWNAME'], "插入成功！")
            conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    get_data()
