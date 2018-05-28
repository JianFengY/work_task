"""
Created on 2018/5/16
@Author: Jeff Yang
"""
import requests
from config.db_config import conn

def get_html(url):
    """
    获取页面的源码（json）
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_traffic_data():
    """
    获取交通路况数据
    """
    url = "http://219.136.133.162/gztraffic/GetData.ashx"
    json_data = get_html(url)
    refreshTime = json_data['refreshTime']  # 更新时间
    zoneStateData = json_data['zoneStateData']  # 全市概况
    topCongRoadData = json_data['topCongRoadData']  # 重要主干道拥堵路段实时播报
    AreaData = json_data['AreaData']  # 重点区域
    RoadData = json_data['RoadData']  # 重点通道
    print('更新时间：', refreshTime)
    refresh_time = refreshTime.replace('年', '-').replace('月', '-').replace('日', '').replace('时', ':').replace('分', '')

    cursor = conn.cursor()
    try:
        print("=============")
        print('区域名称 交通指数 拥堵级别 平均速度(km/h)')
        for zone in zoneStateData:
            sql = "INSERT INTO traffic_district (zone_name, cong_index, cong_name, road_speed, refresh_time) VALUES ('%s','%s','%s','%s','%s')" % (
                zone['ZoneName'], zone['CongIndex'], zone['CongName'], zone['RoadSpeed'], refresh_time)
            cursor.execute(sql)
            conn.commit()
            print(zone['ZoneName'], zone['CongIndex'], zone['CongName'], zone['RoadSpeed'])
        print("=============")
        print("重要主干道拥堵路段实时播报：")
        for cong_road in topCongRoadData:
            sql = "INSERT INTO traffic_cong_road (cong_road, refresh_time) VALUES ('%s','%s')" % (
                cong_road, refresh_time)
            cursor.execute(sql)
            conn.commit()
            print(cong_road)
        print("=============")
        print("重点区域：")
        print('区域名称 交通指数 拥堵级别 平均速度(km/h)')
        for area in AreaData:
            sql = "INSERT INTO traffic_zone (zone_name, cong_index, cong_name, road_speed, refresh_time) VALUES ('%s','%s','%s','%s','%s')" % (
                area['ZoneName'], area['CongIndex'], area['CongName'], area['ZoneSpeed'], refresh_time)
            cursor.execute(sql)
            conn.commit()
            print(area['ZoneName'], area['CongIndex'], area['CongName'], area['ZoneSpeed'])
        print("=============")
        print("重点通道：")
        print("通道名称 方向 行程时间比 拥堵级别 平均速度(km/h)")
        for road in RoadData:
            sql = "INSERT INTO traffic_road (road_name, dir, road_TTI, cong_name, road_speed, refresh_time) VALUES ('%s','%s','%s','%s','%s','%s')" % (
                road['RoadName'], road['Dir'], road['RoadTTI'], road['CongName'], road['RoadSpeed'], refresh_time)
            cursor.execute(sql)
            conn.commit()
            print(road['RoadName'], road['Dir'], road['RoadTTI'], road['CongName'], road['RoadSpeed'])
        print("=============")
    except Exception as e:
        print(e)
        conn.rollback()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    get_traffic_data()
