/*
Navicat MySQL Data Transfer

Source Server         : MySql
Source Server Version : 50712
Source Host           : localhost:3306
Source Database       : pymysql

Target Server Type    : MYSQL
Target Server Version : 50712
File Encoding         : 65001

Date: 2018-05-28 11:02:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for air_quality
-- ----------------------------
DROP TABLE IF EXISTS `air_quality`;
CREATE TABLE `air_quality` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(255) DEFAULT NULL,
  `so2_1h` varchar(255) DEFAULT NULL COMMENT '最近1小时均值',
  `so2_24h` varchar(255) DEFAULT NULL COMMENT '24小时均值',
  `no2_1h` varchar(255) DEFAULT NULL,
  `no2_24h` varchar(255) DEFAULT NULL,
  `pm10_1h` varchar(255) DEFAULT NULL,
  `pm10_24h` varchar(255) DEFAULT NULL,
  `co_1h` varchar(255) DEFAULT NULL,
  `co_24h` varchar(255) DEFAULT NULL,
  `o3_1h` varchar(255) DEFAULT NULL,
  `pm2_5_1h` varchar(255) DEFAULT NULL,
  `pm2_5_24h` varchar(255) DEFAULT NULL,
  `AQI` varchar(255) DEFAULT NULL,
  `quality` varchar(255) DEFAULT NULL COMMENT '空气质量',
  `primary_` varchar(255) DEFAULT NULL COMMENT '首要污染物',
  `msg` varchar(255) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for traffic_cong_road
-- ----------------------------
DROP TABLE IF EXISTS `traffic_cong_road`;
CREATE TABLE `traffic_cong_road` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cong_road` varchar(255) DEFAULT NULL COMMENT '重要主干道拥堵路段',
  `refresh_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for traffic_district
-- ----------------------------
DROP TABLE IF EXISTS `traffic_district`;
CREATE TABLE `traffic_district` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zone_name` varchar(255) DEFAULT NULL COMMENT '区域名称',
  `cong_index` varchar(255) DEFAULT NULL COMMENT '交通指数',
  `cong_name` varchar(255) DEFAULT NULL COMMENT '拥堵级别',
  `road_speed` double DEFAULT NULL COMMENT '平均速度(km/h)',
  `refresh_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for traffic_road
-- ----------------------------
DROP TABLE IF EXISTS `traffic_road`;
CREATE TABLE `traffic_road` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `road_name` varchar(255) DEFAULT NULL COMMENT '通道名称',
  `dir` varchar(255) DEFAULT NULL COMMENT '方向',
  `road_TTI` varchar(255) DEFAULT NULL COMMENT '行程时间比',
  `cong_name` varchar(255) DEFAULT NULL COMMENT '拥堵级别',
  `road_speed` varchar(255) DEFAULT NULL COMMENT '平均速度(km/h)',
  `refresh_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=257 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for traffic_zone
-- ----------------------------
DROP TABLE IF EXISTS `traffic_zone`;
CREATE TABLE `traffic_zone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zone_name` varchar(255) DEFAULT NULL COMMENT '区域名称',
  `cong_index` varchar(255) DEFAULT NULL COMMENT '交通指数',
  `cong_name` varchar(255) DEFAULT NULL COMMENT '拥堵级别',
  `road_speed` varchar(255) DEFAULT NULL COMMENT '平均速度(km/h)',
  `refresh_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for weather
-- ----------------------------
DROP TABLE IF EXISTS `weather`;
CREATE TABLE `weather` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `district` varchar(255) DEFAULT NULL COMMENT '区域',
  `area` varchar(255) DEFAULT NULL COMMENT '地点',
  `temperature` varchar(255) DEFAULT NULL COMMENT '温度',
  `time` datetime DEFAULT NULL COMMENT '时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1376 DEFAULT CHARSET=utf8;
