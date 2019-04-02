/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : netshop

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-07-09 14:38:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add goods', '7', 'add_goods');
INSERT INTO `auth_permission` VALUES ('20', 'Can change goods', '7', 'change_goods');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete goods', '7', 'delete_goods');
INSERT INTO `auth_permission` VALUES ('22', 'Can add category', '8', 'add_category');
INSERT INTO `auth_permission` VALUES ('23', 'Can change category', '8', 'change_category');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete category', '8', 'delete_category');
INSERT INTO `auth_permission` VALUES ('25', 'Can add goods details item', '9', 'add_goodsdetailsitem');
INSERT INTO `auth_permission` VALUES ('26', 'Can change goods details item', '9', 'change_goodsdetailsitem');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete goods details item', '9', 'delete_goodsdetailsitem');
INSERT INTO `auth_permission` VALUES ('28', 'Can add color', '10', 'add_color');
INSERT INTO `auth_permission` VALUES ('29', 'Can change color', '10', 'change_color');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete color', '10', 'delete_color');
INSERT INTO `auth_permission` VALUES ('31', 'Can add size', '11', 'add_size');
INSERT INTO `auth_permission` VALUES ('32', 'Can change size', '11', 'change_size');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete size', '11', 'delete_size');
INSERT INTO `auth_permission` VALUES ('34', 'Can add goods details', '12', 'add_goodsdetails');
INSERT INTO `auth_permission` VALUES ('35', 'Can change goods details', '12', 'change_goodsdetails');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete goods details', '12', 'delete_goodsdetails');
INSERT INTO `auth_permission` VALUES ('37', 'Can add inventory', '13', 'add_inventory');
INSERT INTO `auth_permission` VALUES ('38', 'Can change inventory', '13', 'change_inventory');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete inventory', '13', 'delete_inventory');
INSERT INTO `auth_permission` VALUES ('40', 'Can add user', '14', 'add_user');
INSERT INTO `auth_permission` VALUES ('41', 'Can change user', '14', 'change_user');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete user', '14', 'delete_user');
INSERT INTO `auth_permission` VALUES ('43', 'Can add address', '15', 'add_address');
INSERT INTO `auth_permission` VALUES ('44', 'Can change address', '15', 'change_address');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete address', '15', 'delete_address');
INSERT INTO `auth_permission` VALUES ('46', 'Can add cart item', '16', 'add_cartitem');
INSERT INTO `auth_permission` VALUES ('47', 'Can change cart item', '16', 'change_cartitem');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete cart item', '16', 'delete_cartitem');
INSERT INTO `auth_permission` VALUES ('49', 'Can add choice', '17', 'add_choice');
INSERT INTO `auth_permission` VALUES ('50', 'Can change choice', '17', 'change_choice');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete choice', '17', 'delete_choice');
INSERT INTO `auth_permission` VALUES ('52', 'Can add question', '18', 'add_question');
INSERT INTO `auth_permission` VALUES ('53', 'Can change question', '18', 'change_question');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete question', '18', 'delete_question');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$100000$E0GIQ4B2tqjE$sGiNIjw0FhEFsO6o0QlCZoHQX9CsUa/572PAUdMojWw=', '2018-05-22 04:05:06', '1', 'admin', '', '', 'admin@admin.com', '1', '1', '2018-05-22 03:56:41');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for cart_cartitem
-- ----------------------------
DROP TABLE IF EXISTS `cart_cartitem`;
CREATE TABLE `cart_cartitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goodsid` int(11) NOT NULL,
  `colorid` int(11) NOT NULL,
  `sizeid` int(11) NOT NULL,
  `count` int(10) unsigned NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cart_cartitem_goodsid_colorid_sizeid_0b632a19_uniq` (`goodsid`,`colorid`,`sizeid`),
  KEY `cart_cartitem_user_id_292943b8_fk_User_user_id` (`user_id`),
  CONSTRAINT `cart_cartitem_user_id_292943b8_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cart_cartitem
-- ----------------------------
INSERT INTO `cart_cartitem` VALUES ('1', '1', '1', '1', '6', '1', '3');
INSERT INTO `cart_cartitem` VALUES ('2', '2', '5', '5', '1', '1', '3');
INSERT INTO `cart_cartitem` VALUES ('3', '3', '7', '9', '1', '1', '3');
INSERT INTO `cart_cartitem` VALUES ('4', '7', '13', '6', '5', '1', '3');
INSERT INTO `cart_cartitem` VALUES ('5', '4', '10', '6', '1', '0', '3');
INSERT INTO `cart_cartitem` VALUES ('8', '12', '25', '6', '3', '1', '1');
INSERT INTO `cart_cartitem` VALUES ('12', '8', '14', '5', '7', '1', '1');
INSERT INTO `cart_cartitem` VALUES ('16', '9', '17', '5', '2', '1', '1');
INSERT INTO `cart_cartitem` VALUES ('17', '10', '21', '5', '1', '1', '1');
INSERT INTO `cart_cartitem` VALUES ('22', '11', '22', '5', '1', '0', '3');
INSERT INTO `cart_cartitem` VALUES ('26', '22', '43', '5', '1', '0', '1');
INSERT INTO `cart_cartitem` VALUES ('29', '6', '12', '5', '2', '1', '1');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-05-22 06:01:52', '1', '这是什么', '1', '[{\"added\": {}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-05-22 06:02:17', '2', 'who are you', '1', '[{\"added\": {}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-05-22 06:02:35', '3', 'what is this', '1', '[{\"added\": {}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2018-05-22 06:03:21', '1', '这是好东西', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2018-05-22 06:03:56', '2', 'I am you', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2018-05-22 06:43:47', '3', '哈哈哈', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2018-05-22 08:00:11', '4', '今天天气怎么样', '1', '[{\"added\": {}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2018-05-22 08:00:19', '5', '吃了吗', '1', '[{\"added\": {}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2018-05-22 08:00:39', '4', '不知道', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2018-05-22 08:01:10', '5', 'i dont know', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2018-05-22 08:01:21', '6', 'hehehe', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2018-05-22 08:01:32', '7', '晴天', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2018-05-22 08:01:39', '8', '阴天', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2018-05-22 08:01:51', '9', '晴转多云', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2018-05-22 08:02:02', '10', '大雨', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2018-05-22 08:02:09', '11', '吃了', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2018-05-22 08:02:15', '12', '没吃', '1', '[{\"added\": {}}]', '17', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2018-05-22 08:02:29', '13', '吃了没吃饱', '1', '[{\"added\": {}}]', '17', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('16', 'cart', 'cartitem');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('8', 'goods', 'category');
INSERT INTO `django_content_type` VALUES ('10', 'goods', 'color');
INSERT INTO `django_content_type` VALUES ('7', 'goods', 'goods');
INSERT INTO `django_content_type` VALUES ('12', 'goods', 'goodsdetails');
INSERT INTO `django_content_type` VALUES ('9', 'goods', 'goodsdetailsitem');
INSERT INTO `django_content_type` VALUES ('13', 'goods', 'inventory');
INSERT INTO `django_content_type` VALUES ('11', 'goods', 'size');
INSERT INTO `django_content_type` VALUES ('17', 'polls', 'choice');
INSERT INTO `django_content_type` VALUES ('18', 'polls', 'question');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('15', 'User', 'address');
INSERT INTO `django_content_type` VALUES ('14', 'User', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-03-15 01:18:39');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-03-15 01:18:42');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-03-15 01:18:43');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-03-15 01:18:43');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2018-03-15 01:18:43');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2018-03-15 01:18:43');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2018-03-15 01:18:44');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2018-03-15 01:18:44');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2018-03-15 01:18:44');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2018-03-15 01:18:44');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2018-03-15 01:18:44');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2018-03-15 01:18:44');
INSERT INTO `django_migrations` VALUES ('13', 'goods', '0001_initial', '2018-03-15 01:18:46');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2018-03-15 01:18:47');
INSERT INTO `django_migrations` VALUES ('15', 'User', '0001_initial', '2018-03-15 07:01:36');
INSERT INTO `django_migrations` VALUES ('16', 'User', '0002_address', '2018-03-16 06:46:53');
INSERT INTO `django_migrations` VALUES ('17', 'cart', '0001_initial', '2018-03-16 08:37:11');
INSERT INTO `django_migrations` VALUES ('18', 'polls', '0001_initial', '2018-05-21 11:25:39');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('b8zde5mwk4jxhj911kqxcgu48ofu8ntr', 'MzM3YzgyZTM1YWViZjNhMzdmMDExNmQwOGE3NTU1NTI5NTQyYjgxMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5N2UzYTA3NTZmMGE1OThjZWI1YjU1ZmZmNTE4MWI4NjAwZWY2ZGI1In0=', '2018-06-05 04:05:06');

-- ----------------------------
-- Table structure for goods_category
-- ----------------------------
DROP TABLE IF EXISTS `goods_category`;
CREATE TABLE `goods_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_category
-- ----------------------------
INSERT INTO `goods_category` VALUES ('13', '内衣');
INSERT INTO `goods_category` VALUES ('2', '女装');
INSERT INTO `goods_category` VALUES ('8', '家纺');
INSERT INTO `goods_category` VALUES ('7', '居家');
INSERT INTO `goods_category` VALUES ('11', '数码');
INSERT INTO `goods_category` VALUES ('9', '文体');
INSERT INTO `goods_category` VALUES ('5', '母婴');
INSERT INTO `goods_category` VALUES ('12', '电器');
INSERT INTO `goods_category` VALUES ('1', '男装');
INSERT INTO `goods_category` VALUES ('4', '箱包');
INSERT INTO `goods_category` VALUES ('6', '美妆');
INSERT INTO `goods_category` VALUES ('10', '美食');
INSERT INTO `goods_category` VALUES ('14', '装饰');
INSERT INTO `goods_category` VALUES ('3', '鞋子');

-- ----------------------------
-- Table structure for goods_color
-- ----------------------------
DROP TABLE IF EXISTS `goods_color`;
CREATE TABLE `goods_color` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `value` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_color
-- ----------------------------
INSERT INTO `goods_color` VALUES ('1', '红色', 'color/hong_Dm4fQ6U.jpg');
INSERT INTO `goods_color` VALUES ('2', '绿色', 'color/lv_cTMJg2K.jpg');
INSERT INTO `goods_color` VALUES ('3', '黄色', 'color/huang_bvCMlhn.jpg');
INSERT INTO `goods_color` VALUES ('4', '黑色', 'color/hei_rFOWelp.jpg');
INSERT INTO `goods_color` VALUES ('5', '白色', 'color/bai_mt1VrH5.jpg');
INSERT INTO `goods_color` VALUES ('6', '三号色', 'color/san.jpg');
INSERT INTO `goods_color` VALUES ('7', '红色', 'color/hong_y7wQwRw.jpg');
INSERT INTO `goods_color` VALUES ('8', '黄色', 'color/huang_NKcgOlT.jpg');
INSERT INTO `goods_color` VALUES ('9', '紫色', 'color/zi_umktLLD.jpg');
INSERT INTO `goods_color` VALUES ('10', '蓝色', 'color/lan_BKQdpOj.jpg');
INSERT INTO `goods_color` VALUES ('11', '红色', 'color/hong_zHPXVqY.jpg');
INSERT INTO `goods_color` VALUES ('12', '蓝色', 'color/lan_IThSO4Z.jpg');
INSERT INTO `goods_color` VALUES ('13', '蓝色', 'color/lan_ELubwxG.jpg');
INSERT INTO `goods_color` VALUES ('14', '绿色', 'color/lv_H5hkmmq.jpg');
INSERT INTO `goods_color` VALUES ('15', '红色', 'color/hong_4FhJTrJ.jpg');
INSERT INTO `goods_color` VALUES ('16', '蓝色', 'color/lan_7rd4yDs.jpg');
INSERT INTO `goods_color` VALUES ('17', '灰色', 'color/hui.jpg');
INSERT INTO `goods_color` VALUES ('18', '蓝色', 'color/lan.jpg');
INSERT INTO `goods_color` VALUES ('19', '红色', 'color/hong_UO2LzHh.jpg');
INSERT INTO `goods_color` VALUES ('20', '黑色', 'color/hei_cOOnNKI.jpg');
INSERT INTO `goods_color` VALUES ('21', '黑色', 'color/hei_kYyKPNv.jpg');
INSERT INTO `goods_color` VALUES ('22', '绿色', 'color/lv_sxlJZTq.jpg');
INSERT INTO `goods_color` VALUES ('23', '白色', 'color/bai_B7tmsjh.jpg');
INSERT INTO `goods_color` VALUES ('24', '黑色', 'color/hei_sNOao2p.jpg');
INSERT INTO `goods_color` VALUES ('25', '橘色', 'color/ju.jpg');
INSERT INTO `goods_color` VALUES ('26', '紫色', 'color/zi.jpg');
INSERT INTO `goods_color` VALUES ('27', '斑马色', 'color/ban_fSqFE03.jpg');
INSERT INTO `goods_color` VALUES ('28', '黑色', 'color/hei_ZyxMfgc.jpg');
INSERT INTO `goods_color` VALUES ('29', '白色', 'color/bai.jpg');
INSERT INTO `goods_color` VALUES ('30', '黑色', 'color/hei_goVnbhs.jpg');
INSERT INTO `goods_color` VALUES ('31', '绿色', 'color/lv_eFlravj.jpg');
INSERT INTO `goods_color` VALUES ('32', '红色', 'color/hong_nwQGdMd.jpg');
INSERT INTO `goods_color` VALUES ('33', '棕色', 'color/zong_v7JDaAc.jpg');
INSERT INTO `goods_color` VALUES ('34', '斑马色', 'color/ban.jpg');
INSERT INTO `goods_color` VALUES ('35', '黑色', 'color/hei_3vOTo3s.jpg');
INSERT INTO `goods_color` VALUES ('36', '绿色', 'color/lv.jpg');
INSERT INTO `goods_color` VALUES ('37', '黄', 'color/huang.jpg');
INSERT INTO `goods_color` VALUES ('38', '黑色', 'color/hei_JeBWGjF.jpg');
INSERT INTO `goods_color` VALUES ('39', '黑色', 'color/hei_LfSKcUV.jpg');
INSERT INTO `goods_color` VALUES ('40', '黑色', 'color/hei_1d7yrVm.jpg');
INSERT INTO `goods_color` VALUES ('41', '黑色', 'color/hei.jpg');
INSERT INTO `goods_color` VALUES ('42', '红色', 'color/hongse.jpg');
INSERT INTO `goods_color` VALUES ('43', '黑色', 'color/h_2og4uJv.jpg');
INSERT INTO `goods_color` VALUES ('44', '红色', 'color/hong.jpg');
INSERT INTO `goods_color` VALUES ('45', '棕色', 'color/zong.jpg');

-- ----------------------------
-- Table structure for goods_goods
-- ----------------------------
DROP TABLE IF EXISTS `goods_goods`;
CREATE TABLE `goods_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` varchar(100) NOT NULL,
  `price` decimal(5,2) NOT NULL,
  `oldprice` decimal(5,2) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_goods_category_id_da3507dd_fk_goods_category_id` (`category_id`),
  CONSTRAINT `goods_goods_category_id_da3507dd_fk_goods_category_id` FOREIGN KEY (`category_id`) REFERENCES `goods_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_goods
-- ----------------------------
INSERT INTO `goods_goods` VALUES ('1', '90绒大毛领保暖羽绒服', '梦娜世家2017女式新款修身中长款毛领时尚显瘦欧美气质羽绒服A88', '99.00', '499.00', '2');
INSERT INTO `goods_goods` VALUES ('2', '秋时尚印花两件套装裙', '秋装时尚印花复古时尚休闲两件套装裙子', '35.00', '100.00', '2');
INSERT INTO `goods_goods` VALUES ('3', '韩版侧开叉宽松毛衣', '新款韩版前短后长 侧开叉宽松圆领 纯色大码套头针织衫外套', '39.00', '369.00', '2');
INSERT INTO `goods_goods` VALUES ('4', '无袖套头毛衣马甲女秋', '2017秋季新款上衣潮 笑脸学院风针织背心无袖套头毛衣马甲女春秋', '39.00', '296.00', '2');
INSERT INTO `goods_goods` VALUES ('5', '红色原宿bf风小外套', '诗赫姿秋新款红色原宿bf风牛仔小外套女', '69.00', '229.00', '2');
INSERT INTO `goods_goods` VALUES ('6', '不规则毛边喇叭牛仔裤', '诗赫姿秋新款不规则毛边喇叭长裤牛仔裤', '65.00', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('7', '宽松短款牛仔外套', '诗赫姿秋新款宽松短款时尚绣花牛仔外套女', '79.00', '259.00', '2');
INSERT INTO `goods_goods` VALUES ('8', '气质收腰显瘦连衣裙', '诗赫姿秋新款气质时尚收腰显瘦连衣裙女', '69.00', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('9', '针织袖拼接毛呢打底裙', '诗赫姿秋新款针织袖时尚拼接毛呢打底裙', '69.00', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('10', '双排扣假两件连衣裙', '诗赫姿秋新款简约双排扣假两件连衣裙女', '69.00', '299.00', '2');
INSERT INTO `goods_goods` VALUES ('11', '修身包臀蕾丝打底裙', '诗赫姿秋新款修身包臀蕾丝打底裙连衣裙', '69.00', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('12', '修身显瘦格子打底裙', '诗赫姿秋新款修身显瘦格子打底裙连衣裙', '69.90', '259.00', '2');
INSERT INTO `goods_goods` VALUES ('13', '条纹显瘦网纱连衣裙', '诗赫姿秋新款条纹时尚显瘦网纱连衣裙女', '69.90', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('14', '显瘦蕾丝中长连衣裙', '诗赫姿秋新款时尚显瘦蕾丝中长连衣裙女', '69.00', '255.00', '2');
INSERT INTO `goods_goods` VALUES ('15', '时尚修身两件套装裙', '诗赫姿秋新款时尚修身两件套装连衣裙女', '68.90', '299.00', '2');
INSERT INTO `goods_goods` VALUES ('16', '条纹针织包臀连衣裙', '诗赫姿秋条纹时尚针织包臀打底裙连衣裙', '65.00', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('17', '系带显瘦宽松套装', '诗赫姿秋系带显瘦宽松时尚套装阔腿裤女', '69.90', '259.00', '2');
INSERT INTO `goods_goods` VALUES ('18', '秋季V领镂空蕾丝衫', '新款大码女装蕾丝衫韩版修身V领长袖打底衫网纱镂空上衣', '28.00', '124.00', '2');
INSERT INTO `goods_goods` VALUES ('19', '松紧腰PU皮短裤', '秋冬时尚百搭高腰PU皮阔腿短裤女打底皮裤', '19.90', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('20', '高腰刺绣PU皮短裙', '秋冬时尚高腰刺绣PU皮短裙女打底半身裙', '29.90', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('21', '修身短款呢子小外套', '秋装新款女装毛呢短外套女 时尚修身短款呢子小西装潮', '39.00', '199.00', '2');
INSERT INTO `goods_goods` VALUES ('22', '中长款双面呢毛呢外套', '中长款双面呢毛呢外套', '33.00', '256.00', '2');

-- ----------------------------
-- Table structure for goods_goodsdetails
-- ----------------------------
DROP TABLE IF EXISTS `goods_goodsdetails`;
CREATE TABLE `goods_goodsdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_goodsdetails
-- ----------------------------
INSERT INTO `goods_goodsdetails` VALUES ('1', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('2', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('3', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('4', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('5', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('6', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('7', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('8', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('9', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('10', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('11', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('12', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('13', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('14', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('15', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('16', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('17', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('18', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('19', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('20', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('21', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('22', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('23', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('24', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('25', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('26', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('27', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('28', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('29', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('30', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('31', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('32', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('33', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('34', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('35', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('36', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('37', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('38', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('39', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('40', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('41', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('42', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('43', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('44', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('45', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('46', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('47', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('48', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('49', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('50', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('51', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('52', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('53', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('54', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('55', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('56', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('57', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('58', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('59', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('60', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('61', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('62', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('63', '模特实拍');
INSERT INTO `goods_goodsdetails` VALUES ('64', '参数规格');
INSERT INTO `goods_goodsdetails` VALUES ('65', '整体款式');
INSERT INTO `goods_goodsdetails` VALUES ('66', '模特实拍');

-- ----------------------------
-- Table structure for goods_goodsdetailsitem
-- ----------------------------
DROP TABLE IF EXISTS `goods_goodsdetailsitem`;
CREATE TABLE `goods_goodsdetailsitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `values` varchar(100) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `goodsdetails_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_goodsdetailsitem_goods_id_61ac315c_fk_goods_goods_id` (`goods_id`),
  KEY `goods_goodsdetailsit_goodsdetails_id_accc05ce_fk_goods_goo` (`goodsdetails_id`),
  CONSTRAINT `goods_goodsdetailsit_goodsdetails_id_accc05ce_fk_goods_goo` FOREIGN KEY (`goodsdetails_id`) REFERENCES `goods_goodsdetails` (`id`),
  CONSTRAINT `goods_goodsdetailsitem_goods_id_61ac315c_fk_goods_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `goods_goods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=257 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_goodsdetailsitem
-- ----------------------------
INSERT INTO `goods_goodsdetailsitem` VALUES ('1', '/static/images/B5_03.png', '1', '1');
INSERT INTO `goods_goodsdetailsitem` VALUES ('2', '/static/images/B5_06.png', '1', '2');
INSERT INTO `goods_goodsdetailsitem` VALUES ('3', '/media/1_mpwtoGA.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('4', '/media/2_UuQkY4b.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('5', '/media/3_ViMgWv6.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('6', '/media/4_BDmgdFv.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('7', '/media/5_ozWIsej.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('8', '/media/6_Pny8yTQ.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('9', '/media/7_K4tB09L.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('10', '/media/8_60MJMwS.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('11', '/media/9_8YomGSk.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('12', '/media/10_vonnLjk.jpg', '1', '3');
INSERT INTO `goods_goodsdetailsitem` VALUES ('13', '/static/images/B5_03.png', '2', '4');
INSERT INTO `goods_goodsdetailsitem` VALUES ('14', '/static/images/B5_06.png', '2', '5');
INSERT INTO `goods_goodsdetailsitem` VALUES ('15', '/media/1_DNiW0D5.jpg', '2', '6');
INSERT INTO `goods_goodsdetailsitem` VALUES ('16', '/media/2_eHi0Rix.jpg', '2', '6');
INSERT INTO `goods_goodsdetailsitem` VALUES ('17', '/media/3_2e1cWcs.jpg', '2', '6');
INSERT INTO `goods_goodsdetailsitem` VALUES ('18', '/media/4_D0ck80V.jpg', '2', '6');
INSERT INTO `goods_goodsdetailsitem` VALUES ('19', '/media/5_bxMyxv5.jpg', '2', '6');
INSERT INTO `goods_goodsdetailsitem` VALUES ('20', '/media/6_Z4j72Ft.jpg', '2', '6');
INSERT INTO `goods_goodsdetailsitem` VALUES ('21', '/media/7_3QbFC0z.jpg', '2', '6');
INSERT INTO `goods_goodsdetailsitem` VALUES ('22', '/media/8_OQGcrwL.jpg', '2', '6');
INSERT INTO `goods_goodsdetailsitem` VALUES ('23', '/static/images/B5_03.png', '3', '7');
INSERT INTO `goods_goodsdetailsitem` VALUES ('24', '/static/images/B5_06.png', '3', '8');
INSERT INTO `goods_goodsdetailsitem` VALUES ('25', '/media/1_QoLgPlj.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('26', '/media/2_lHY8mE9.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('27', '/media/3_GiFc4gk.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('28', '/media/4_IBO3QkF.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('29', '/media/5_NjssJjH.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('30', '/media/6_TJDGChY.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('31', '/media/7_Sv0tWHZ.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('32', '/media/8_MDhSM1I.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('33', '/media/9_BUoWkrL.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('34', '/media/10_k9f1eEK.jpg', '3', '9');
INSERT INTO `goods_goodsdetailsitem` VALUES ('35', '/static/images/B5_03.png', '4', '10');
INSERT INTO `goods_goodsdetailsitem` VALUES ('36', '/static/images/B5_06.png', '4', '11');
INSERT INTO `goods_goodsdetailsitem` VALUES ('37', '/media/1_ORTzeTY.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('38', '/media/2_RbgTYId.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('39', '/media/3_1CyOSyR.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('40', '/media/4_0490Pq4.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('41', '/media/5_gk51Yc1.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('42', '/media/6_MNo76Wb.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('43', '/media/7_4JyLPNO.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('44', '/media/8_VX32aT2.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('45', '/media/9_x8mkplo.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('46', '/media/10_1OVaH2E.jpg', '4', '12');
INSERT INTO `goods_goodsdetailsitem` VALUES ('47', '/static/images/B5_03.png', '5', '13');
INSERT INTO `goods_goodsdetailsitem` VALUES ('48', '/static/images/B5_06.png', '5', '14');
INSERT INTO `goods_goodsdetailsitem` VALUES ('49', '/media/1_0IilSTS.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('50', '/media/2_dU6RLKQ.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('51', '/media/3_eLYKeSJ.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('52', '/media/4_mwUqQ7u.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('53', '/media/5_AOfqMfX.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('54', '/media/6_LE1Qg19.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('55', '/media/7_7RVZFif.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('56', '/media/8_W5zUBfp.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('57', '/media/9_Py3cDKv.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('58', '/media/10_w9OXfoC.jpg', '5', '15');
INSERT INTO `goods_goodsdetailsitem` VALUES ('59', '/static/images/B5_03.png', '6', '16');
INSERT INTO `goods_goodsdetailsitem` VALUES ('60', '/static/images/B5_06.png', '6', '17');
INSERT INTO `goods_goodsdetailsitem` VALUES ('61', '/media/1_f8GP2Js.jpg', '6', '18');
INSERT INTO `goods_goodsdetailsitem` VALUES ('62', '/media/2_mewqiym.jpg', '6', '18');
INSERT INTO `goods_goodsdetailsitem` VALUES ('63', '/media/3_T3najRK.jpg', '6', '18');
INSERT INTO `goods_goodsdetailsitem` VALUES ('64', '/media/4_Zn7OFjf.jpg', '6', '18');
INSERT INTO `goods_goodsdetailsitem` VALUES ('65', '/media/5_z6JRqPe.jpg', '6', '18');
INSERT INTO `goods_goodsdetailsitem` VALUES ('66', '/media/6_96JhJlq.jpg', '6', '18');
INSERT INTO `goods_goodsdetailsitem` VALUES ('67', '/media/7_eNtOUP3.jpg', '6', '18');
INSERT INTO `goods_goodsdetailsitem` VALUES ('68', '/media/8_B13UoeN.jpg', '6', '18');
INSERT INTO `goods_goodsdetailsitem` VALUES ('69', '/static/images/B5_03.png', '7', '19');
INSERT INTO `goods_goodsdetailsitem` VALUES ('70', '/static/images/B5_06.png', '7', '20');
INSERT INTO `goods_goodsdetailsitem` VALUES ('71', '/media/1_bmqDR3N.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('72', '/media/2_72CrUqv.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('73', '/media/3_FVVk5kE.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('74', '/media/4_LNKrlRN.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('75', '/media/5_qHsL809.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('76', '/media/6_EXgGQLK.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('77', '/media/7_lJD2O84.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('78', '/media/8_TM4De6X.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('79', '/media/9_gLF6TGo.jpg', '7', '21');
INSERT INTO `goods_goodsdetailsitem` VALUES ('80', '/static/images/B5_03.png', '8', '22');
INSERT INTO `goods_goodsdetailsitem` VALUES ('81', '/static/images/B5_06.png', '8', '23');
INSERT INTO `goods_goodsdetailsitem` VALUES ('82', '/media/1_VJ7ZAQ6.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('83', '/media/2_w4cxzhY.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('84', '/media/3_U55lgsP.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('85', '/media/4_EzoxL21.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('86', '/media/5_Rewgb01.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('87', '/media/6_ze76f9K.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('88', '/media/7_6Wq1Bgx.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('89', '/media/8_R2uMfUz.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('90', '/media/9_D7uVd9z.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('91', '/media/10_0RIywDD.jpg', '8', '24');
INSERT INTO `goods_goodsdetailsitem` VALUES ('92', '/static/images/B5_03.png', '9', '25');
INSERT INTO `goods_goodsdetailsitem` VALUES ('93', '/static/images/B5_06.png', '9', '26');
INSERT INTO `goods_goodsdetailsitem` VALUES ('94', '/media/1_mfc1bTY.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('95', '/media/2_GohidDO.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('96', '/media/3_mFj1A5X.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('97', '/media/4_H23ayWL.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('98', '/media/5_SGzSxZZ.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('99', '/media/6_li3hJqN.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('100', '/media/7_lK1M9SF.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('101', '/media/8_7L4e40W.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('102', '/media/9_TW7TlmY.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('103', '/media/10_woLP7jo.jpg', '9', '27');
INSERT INTO `goods_goodsdetailsitem` VALUES ('104', '/static/images/B5_03.png', '10', '28');
INSERT INTO `goods_goodsdetailsitem` VALUES ('105', '/static/images/B5_06.png', '10', '29');
INSERT INTO `goods_goodsdetailsitem` VALUES ('106', '/media/1_oeshNKk.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('107', '/media/2_iQ7dNj1.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('108', '/media/3_8WGGwE5.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('109', '/media/4_m2QcMFM.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('110', '/media/5_m3BYUyr.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('111', '/media/6_mJhhcKP.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('112', '/media/7_NKEyR9K.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('113', '/media/8_gRR4RHz.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('114', '/media/9_YhUmuWF.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('115', '/media/10_8H4hKoc.jpg', '10', '30');
INSERT INTO `goods_goodsdetailsitem` VALUES ('116', '/static/images/B5_03.png', '11', '31');
INSERT INTO `goods_goodsdetailsitem` VALUES ('117', '/static/images/B5_06.png', '11', '32');
INSERT INTO `goods_goodsdetailsitem` VALUES ('118', '/media/1_Rqdz7U7.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('119', '/media/2_wyGJ4ta.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('120', '/media/3_NNxcobt.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('121', '/media/4_LOhSXlh.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('122', '/media/5_OEepnkc.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('123', '/media/6_om0yrNS.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('124', '/media/7_va0yr9Y.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('125', '/media/8_egWx7Pl.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('126', '/media/9_JJPOi3d.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('127', '/media/10_yXoBnL0.jpg', '11', '33');
INSERT INTO `goods_goodsdetailsitem` VALUES ('128', '/static/images/B5_03.png', '12', '34');
INSERT INTO `goods_goodsdetailsitem` VALUES ('129', '/static/images/B5_06.png', '12', '35');
INSERT INTO `goods_goodsdetailsitem` VALUES ('130', '/media/1_EPbLlsh.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('131', '/media/2_CG1HTi2.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('132', '/media/3_LrJ1TCJ.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('133', '/media/4_ppO44fs.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('134', '/media/5_3tIgCS6.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('135', '/media/6_KN6SOts.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('136', '/media/7_7vLJg1T.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('137', '/media/8_BaXff43.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('138', '/media/9_AexcCbE.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('139', '/media/10_yG5bZ6x.jpg', '12', '36');
INSERT INTO `goods_goodsdetailsitem` VALUES ('140', '/static/images/B5_03.png', '13', '37');
INSERT INTO `goods_goodsdetailsitem` VALUES ('141', '/static/images/B5_06.png', '13', '38');
INSERT INTO `goods_goodsdetailsitem` VALUES ('142', '/media/1_X1vUHuX.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('143', '/media/2_rQvH5hc.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('144', '/media/3_T5aiJXo.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('145', '/media/4_VYfCSBP.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('146', '/media/5_KdbwcPL.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('147', '/media/6_7stuZRI.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('148', '/media/7_WB2mznP.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('149', '/media/8_7HnFJUe.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('150', '/media/9_HN634xt.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('151', '/media/10_Gs7AS8Z.jpg', '13', '39');
INSERT INTO `goods_goodsdetailsitem` VALUES ('152', '/static/images/B5_03.png', '14', '40');
INSERT INTO `goods_goodsdetailsitem` VALUES ('153', '/static/images/B5_06.png', '14', '41');
INSERT INTO `goods_goodsdetailsitem` VALUES ('154', '/media/1_qhSeLSP.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('155', '/media/2_T1EYNmq.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('156', '/media/3_M5MK3Rp.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('157', '/media/4_Qsb0wFi.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('158', '/media/5_8L7yPar.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('159', '/media/6_Xaip1y1.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('160', '/media/7_MEUf1z0.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('161', '/media/8_KtL5Rj0.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('162', '/media/9_yFn3P2g.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('163', '/media/10_TmP9DXa.jpg', '14', '42');
INSERT INTO `goods_goodsdetailsitem` VALUES ('164', '/static/images/B5_03.png', '15', '43');
INSERT INTO `goods_goodsdetailsitem` VALUES ('165', '/static/images/B5_06.png', '15', '44');
INSERT INTO `goods_goodsdetailsitem` VALUES ('166', '/media/1_YVRqAfG.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('167', '/media/2_rJP2AdH.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('168', '/media/3_gQdONuG.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('169', '/media/4_7T0yj4F.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('170', '/media/5_DI2p1Wl.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('171', '/media/6_CmqXZLW.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('172', '/media/7_XOIrJSq.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('173', '/media/8_ZqFUlsq.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('174', '/media/9_CwxVXnR.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('175', '/media/10_gn66t3j.jpg', '15', '45');
INSERT INTO `goods_goodsdetailsitem` VALUES ('176', '/static/images/B5_03.png', '16', '46');
INSERT INTO `goods_goodsdetailsitem` VALUES ('177', '/static/images/B5_06.png', '16', '47');
INSERT INTO `goods_goodsdetailsitem` VALUES ('178', '/media/1_v57UFo5.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('179', '/media/2_nT3X3Gi.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('180', '/media/3_C9361FH.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('181', '/media/4_KPjviHC.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('182', '/media/5_j9H6NUg.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('183', '/media/6_0yvtHsK.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('184', '/media/7_OyIqVRu.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('185', '/media/8_zaePCtI.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('186', '/media/9_zDqfKRE.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('187', '/media/10_o3nc5fU.jpg', '16', '48');
INSERT INTO `goods_goodsdetailsitem` VALUES ('188', '/static/images/B5_03.png', '17', '49');
INSERT INTO `goods_goodsdetailsitem` VALUES ('189', '/static/images/B5_06.png', '17', '50');
INSERT INTO `goods_goodsdetailsitem` VALUES ('190', '/media/1_vXCGxCI.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('191', '/media/2_54gKgQP.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('192', '/media/3_eNxYhCr.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('193', '/media/4_BprQkfJ.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('194', '/media/5_qsc95lP.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('195', '/media/6_UAGLwbX.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('196', '/media/7_F6hIwWB.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('197', '/media/8_a2kJabS.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('198', '/media/9_SZ0wMpy.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('199', '/media/10_MeWXSKs.jpg', '17', '51');
INSERT INTO `goods_goodsdetailsitem` VALUES ('200', '/static/images/B5_03.png', '18', '52');
INSERT INTO `goods_goodsdetailsitem` VALUES ('201', '/static/images/B5_06.png', '18', '53');
INSERT INTO `goods_goodsdetailsitem` VALUES ('202', '/media/1_NMUUNXC.jpg', '18', '54');
INSERT INTO `goods_goodsdetailsitem` VALUES ('203', '/media/2_Ouot4Pr.jpg', '18', '54');
INSERT INTO `goods_goodsdetailsitem` VALUES ('204', '/media/3_Gz1jfea.jpg', '18', '54');
INSERT INTO `goods_goodsdetailsitem` VALUES ('205', '/media/4_I75CkJ3.jpg', '18', '54');
INSERT INTO `goods_goodsdetailsitem` VALUES ('206', '/media/5_o83wrz9.jpg', '18', '54');
INSERT INTO `goods_goodsdetailsitem` VALUES ('207', '/media/6_a6urQrM.jpg', '18', '54');
INSERT INTO `goods_goodsdetailsitem` VALUES ('208', '/media/7_Wj7Dhuj.jpg', '18', '54');
INSERT INTO `goods_goodsdetailsitem` VALUES ('209', '/static/images/B5_03.png', '19', '55');
INSERT INTO `goods_goodsdetailsitem` VALUES ('210', '/static/images/B5_06.png', '19', '56');
INSERT INTO `goods_goodsdetailsitem` VALUES ('211', '/media/1_hYKWHNU.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('212', '/media/2_HG8qNBO.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('213', '/media/3_aDwC2Ql.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('214', '/media/4_Rj4l1L8.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('215', '/media/5_23MIkpl.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('216', '/media/6_q3Kpy4T.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('217', '/media/7_9VDJMAo.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('218', '/media/8_aIKJvFt.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('219', '/media/9_InpWyDb.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('220', '/media/10_5jDjWzb.jpg', '19', '57');
INSERT INTO `goods_goodsdetailsitem` VALUES ('221', '/static/images/B5_03.png', '20', '58');
INSERT INTO `goods_goodsdetailsitem` VALUES ('222', '/static/images/B5_06.png', '20', '59');
INSERT INTO `goods_goodsdetailsitem` VALUES ('223', '/media/1_elE8eIp.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('224', '/media/2_4vn9XVx.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('225', '/media/3_D1iL18X.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('226', '/media/4_i3s0HY6.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('227', '/media/5_fjAcCOl.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('228', '/media/6_ECsXNEg.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('229', '/media/7_7pnv5eG.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('230', '/media/8_dDvDZt3.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('231', '/media/9_e0PyyUN.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('232', '/media/10_w27K7NE.jpg', '20', '60');
INSERT INTO `goods_goodsdetailsitem` VALUES ('233', '/static/images/B5_03.png', '21', '61');
INSERT INTO `goods_goodsdetailsitem` VALUES ('234', '/static/images/B5_06.png', '21', '62');
INSERT INTO `goods_goodsdetailsitem` VALUES ('235', '/media/1_lCofK1Q.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('236', '/media/2_fN7fXqT.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('237', '/media/3_sQci5N1.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('238', '/media/4_t8f1jLp.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('239', '/media/5_pnAqZij.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('240', '/media/6_Jyvt0gV.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('241', '/media/7_88GAaTo.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('242', '/media/8_dwmGQq1.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('243', '/media/9_IVxniTc.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('244', '/media/10_MBQOH1D.jpg', '21', '63');
INSERT INTO `goods_goodsdetailsitem` VALUES ('245', '/static/images/B5_03.png', '22', '64');
INSERT INTO `goods_goodsdetailsitem` VALUES ('246', '/static/images/B5_06.png', '22', '65');
INSERT INTO `goods_goodsdetailsitem` VALUES ('247', '/media/1.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('248', '/media/2.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('249', '/media/3.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('250', '/media/4.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('251', '/media/5.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('252', '/media/6.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('253', '/media/7.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('254', '/media/8.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('255', '/media/9.jpg', '22', '66');
INSERT INTO `goods_goodsdetailsitem` VALUES ('256', '/media/10.jpg', '22', '66');

-- ----------------------------
-- Table structure for goods_inventory
-- ----------------------------
DROP TABLE IF EXISTS `goods_inventory`;
CREATE TABLE `goods_inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(11) NOT NULL,
  `color_id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `size_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_inventory_color_id_51ea6193_fk_goods_color_id` (`color_id`),
  KEY `goods_inventory_goods_id_315bae0f_fk_goods_goods_id` (`goods_id`),
  KEY `goods_inventory_size_id_52bf3d50_fk_goods_size_id` (`size_id`),
  CONSTRAINT `goods_inventory_color_id_51ea6193_fk_goods_color_id` FOREIGN KEY (`color_id`) REFERENCES `goods_color` (`id`),
  CONSTRAINT `goods_inventory_goods_id_315bae0f_fk_goods_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `goods_goods` (`id`),
  CONSTRAINT `goods_inventory_size_id_52bf3d50_fk_goods_size_id` FOREIGN KEY (`size_id`) REFERENCES `goods_size` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_inventory
-- ----------------------------
INSERT INTO `goods_inventory` VALUES ('1', '100', '1', '1', '1');
INSERT INTO `goods_inventory` VALUES ('2', '100', '1', '1', '2');
INSERT INTO `goods_inventory` VALUES ('3', '100', '1', '1', '3');
INSERT INTO `goods_inventory` VALUES ('4', '100', '1', '1', '4');
INSERT INTO `goods_inventory` VALUES ('5', '100', '2', '1', '1');
INSERT INTO `goods_inventory` VALUES ('6', '100', '2', '1', '2');
INSERT INTO `goods_inventory` VALUES ('7', '100', '2', '1', '3');
INSERT INTO `goods_inventory` VALUES ('8', '100', '2', '1', '4');
INSERT INTO `goods_inventory` VALUES ('9', '100', '3', '1', '1');
INSERT INTO `goods_inventory` VALUES ('10', '100', '3', '1', '2');
INSERT INTO `goods_inventory` VALUES ('11', '100', '3', '1', '3');
INSERT INTO `goods_inventory` VALUES ('12', '100', '3', '1', '4');
INSERT INTO `goods_inventory` VALUES ('13', '100', '4', '1', '1');
INSERT INTO `goods_inventory` VALUES ('14', '100', '4', '1', '2');
INSERT INTO `goods_inventory` VALUES ('15', '100', '4', '1', '3');
INSERT INTO `goods_inventory` VALUES ('16', '100', '4', '1', '4');
INSERT INTO `goods_inventory` VALUES ('17', '100', '5', '2', '5');
INSERT INTO `goods_inventory` VALUES ('18', '100', '5', '2', '6');
INSERT INTO `goods_inventory` VALUES ('19', '100', '5', '2', '7');
INSERT INTO `goods_inventory` VALUES ('20', '100', '5', '2', '8');
INSERT INTO `goods_inventory` VALUES ('21', '100', '6', '2', '5');
INSERT INTO `goods_inventory` VALUES ('22', '100', '6', '2', '6');
INSERT INTO `goods_inventory` VALUES ('23', '100', '6', '2', '7');
INSERT INTO `goods_inventory` VALUES ('24', '100', '6', '2', '8');
INSERT INTO `goods_inventory` VALUES ('25', '100', '7', '3', '9');
INSERT INTO `goods_inventory` VALUES ('26', '100', '8', '3', '9');
INSERT INTO `goods_inventory` VALUES ('27', '100', '9', '3', '9');
INSERT INTO `goods_inventory` VALUES ('28', '100', '10', '4', '6');
INSERT INTO `goods_inventory` VALUES ('29', '100', '11', '5', '5');
INSERT INTO `goods_inventory` VALUES ('30', '100', '11', '5', '6');
INSERT INTO `goods_inventory` VALUES ('31', '100', '11', '5', '7');
INSERT INTO `goods_inventory` VALUES ('32', '100', '11', '5', '8');
INSERT INTO `goods_inventory` VALUES ('33', '100', '12', '6', '5');
INSERT INTO `goods_inventory` VALUES ('34', '100', '12', '6', '6');
INSERT INTO `goods_inventory` VALUES ('35', '100', '12', '6', '7');
INSERT INTO `goods_inventory` VALUES ('36', '100', '13', '7', '6');
INSERT INTO `goods_inventory` VALUES ('37', '100', '13', '7', '7');
INSERT INTO `goods_inventory` VALUES ('38', '100', '13', '7', '8');
INSERT INTO `goods_inventory` VALUES ('39', '100', '14', '8', '5');
INSERT INTO `goods_inventory` VALUES ('40', '100', '14', '8', '6');
INSERT INTO `goods_inventory` VALUES ('41', '100', '14', '8', '7');
INSERT INTO `goods_inventory` VALUES ('42', '100', '14', '8', '8');
INSERT INTO `goods_inventory` VALUES ('43', '100', '15', '8', '5');
INSERT INTO `goods_inventory` VALUES ('44', '100', '15', '8', '6');
INSERT INTO `goods_inventory` VALUES ('45', '100', '15', '8', '7');
INSERT INTO `goods_inventory` VALUES ('46', '100', '15', '8', '8');
INSERT INTO `goods_inventory` VALUES ('47', '100', '16', '8', '5');
INSERT INTO `goods_inventory` VALUES ('48', '100', '16', '8', '6');
INSERT INTO `goods_inventory` VALUES ('49', '100', '16', '8', '7');
INSERT INTO `goods_inventory` VALUES ('50', '100', '16', '8', '8');
INSERT INTO `goods_inventory` VALUES ('51', '100', '17', '9', '5');
INSERT INTO `goods_inventory` VALUES ('52', '100', '17', '9', '6');
INSERT INTO `goods_inventory` VALUES ('53', '100', '17', '9', '7');
INSERT INTO `goods_inventory` VALUES ('54', '100', '17', '9', '8');
INSERT INTO `goods_inventory` VALUES ('55', '100', '18', '9', '5');
INSERT INTO `goods_inventory` VALUES ('56', '100', '18', '9', '6');
INSERT INTO `goods_inventory` VALUES ('57', '100', '18', '9', '7');
INSERT INTO `goods_inventory` VALUES ('58', '100', '18', '9', '8');
INSERT INTO `goods_inventory` VALUES ('59', '100', '19', '9', '5');
INSERT INTO `goods_inventory` VALUES ('60', '100', '19', '9', '6');
INSERT INTO `goods_inventory` VALUES ('61', '100', '19', '9', '7');
INSERT INTO `goods_inventory` VALUES ('62', '100', '19', '9', '8');
INSERT INTO `goods_inventory` VALUES ('63', '100', '20', '9', '5');
INSERT INTO `goods_inventory` VALUES ('64', '100', '20', '9', '6');
INSERT INTO `goods_inventory` VALUES ('65', '100', '20', '9', '7');
INSERT INTO `goods_inventory` VALUES ('66', '100', '20', '9', '8');
INSERT INTO `goods_inventory` VALUES ('67', '100', '21', '10', '5');
INSERT INTO `goods_inventory` VALUES ('68', '100', '21', '10', '6');
INSERT INTO `goods_inventory` VALUES ('69', '100', '21', '10', '7');
INSERT INTO `goods_inventory` VALUES ('70', '100', '21', '10', '8');
INSERT INTO `goods_inventory` VALUES ('71', '100', '22', '11', '5');
INSERT INTO `goods_inventory` VALUES ('72', '100', '22', '11', '6');
INSERT INTO `goods_inventory` VALUES ('73', '100', '22', '11', '7');
INSERT INTO `goods_inventory` VALUES ('74', '100', '22', '11', '8');
INSERT INTO `goods_inventory` VALUES ('75', '100', '23', '11', '5');
INSERT INTO `goods_inventory` VALUES ('76', '100', '23', '11', '6');
INSERT INTO `goods_inventory` VALUES ('77', '100', '23', '11', '7');
INSERT INTO `goods_inventory` VALUES ('78', '100', '23', '11', '8');
INSERT INTO `goods_inventory` VALUES ('79', '100', '24', '11', '5');
INSERT INTO `goods_inventory` VALUES ('80', '100', '24', '11', '6');
INSERT INTO `goods_inventory` VALUES ('81', '100', '24', '11', '7');
INSERT INTO `goods_inventory` VALUES ('82', '100', '24', '11', '8');
INSERT INTO `goods_inventory` VALUES ('83', '100', '25', '12', '6');
INSERT INTO `goods_inventory` VALUES ('84', '100', '25', '12', '7');
INSERT INTO `goods_inventory` VALUES ('85', '100', '25', '12', '8');
INSERT INTO `goods_inventory` VALUES ('86', '100', '26', '12', '6');
INSERT INTO `goods_inventory` VALUES ('87', '100', '26', '12', '7');
INSERT INTO `goods_inventory` VALUES ('88', '100', '26', '12', '8');
INSERT INTO `goods_inventory` VALUES ('89', '100', '27', '13', '5');
INSERT INTO `goods_inventory` VALUES ('90', '100', '27', '13', '6');
INSERT INTO `goods_inventory` VALUES ('91', '100', '27', '13', '7');
INSERT INTO `goods_inventory` VALUES ('92', '100', '27', '13', '8');
INSERT INTO `goods_inventory` VALUES ('93', '100', '28', '13', '5');
INSERT INTO `goods_inventory` VALUES ('94', '100', '28', '13', '6');
INSERT INTO `goods_inventory` VALUES ('95', '100', '28', '13', '7');
INSERT INTO `goods_inventory` VALUES ('96', '100', '28', '13', '8');
INSERT INTO `goods_inventory` VALUES ('97', '100', '29', '14', '5');
INSERT INTO `goods_inventory` VALUES ('98', '100', '29', '14', '6');
INSERT INTO `goods_inventory` VALUES ('99', '100', '29', '14', '7');
INSERT INTO `goods_inventory` VALUES ('100', '100', '29', '14', '8');
INSERT INTO `goods_inventory` VALUES ('101', '100', '30', '14', '5');
INSERT INTO `goods_inventory` VALUES ('102', '100', '30', '14', '6');
INSERT INTO `goods_inventory` VALUES ('103', '100', '30', '14', '7');
INSERT INTO `goods_inventory` VALUES ('104', '100', '30', '14', '8');
INSERT INTO `goods_inventory` VALUES ('105', '100', '31', '15', '5');
INSERT INTO `goods_inventory` VALUES ('106', '100', '31', '15', '6');
INSERT INTO `goods_inventory` VALUES ('107', '100', '31', '15', '7');
INSERT INTO `goods_inventory` VALUES ('108', '100', '31', '15', '8');
INSERT INTO `goods_inventory` VALUES ('109', '100', '32', '15', '5');
INSERT INTO `goods_inventory` VALUES ('110', '100', '32', '15', '6');
INSERT INTO `goods_inventory` VALUES ('111', '100', '32', '15', '7');
INSERT INTO `goods_inventory` VALUES ('112', '100', '32', '15', '8');
INSERT INTO `goods_inventory` VALUES ('113', '100', '33', '15', '5');
INSERT INTO `goods_inventory` VALUES ('114', '100', '33', '15', '6');
INSERT INTO `goods_inventory` VALUES ('115', '100', '33', '15', '7');
INSERT INTO `goods_inventory` VALUES ('116', '100', '33', '15', '8');
INSERT INTO `goods_inventory` VALUES ('117', '100', '34', '16', '6');
INSERT INTO `goods_inventory` VALUES ('118', '100', '34', '16', '7');
INSERT INTO `goods_inventory` VALUES ('119', '100', '34', '16', '8');
INSERT INTO `goods_inventory` VALUES ('120', '100', '35', '17', '5');
INSERT INTO `goods_inventory` VALUES ('121', '100', '35', '17', '6');
INSERT INTO `goods_inventory` VALUES ('122', '100', '35', '17', '7');
INSERT INTO `goods_inventory` VALUES ('123', '100', '35', '17', '8');
INSERT INTO `goods_inventory` VALUES ('124', '100', '36', '17', '5');
INSERT INTO `goods_inventory` VALUES ('125', '100', '36', '17', '6');
INSERT INTO `goods_inventory` VALUES ('126', '100', '36', '17', '7');
INSERT INTO `goods_inventory` VALUES ('127', '100', '36', '17', '8');
INSERT INTO `goods_inventory` VALUES ('128', '100', '37', '17', '5');
INSERT INTO `goods_inventory` VALUES ('129', '100', '37', '17', '6');
INSERT INTO `goods_inventory` VALUES ('130', '100', '37', '17', '7');
INSERT INTO `goods_inventory` VALUES ('131', '100', '37', '17', '8');
INSERT INTO `goods_inventory` VALUES ('132', '100', '38', '18', '5');
INSERT INTO `goods_inventory` VALUES ('133', '100', '38', '18', '6');
INSERT INTO `goods_inventory` VALUES ('134', '100', '38', '18', '7');
INSERT INTO `goods_inventory` VALUES ('135', '100', '39', '19', '5');
INSERT INTO `goods_inventory` VALUES ('136', '100', '39', '19', '6');
INSERT INTO `goods_inventory` VALUES ('137', '100', '39', '19', '7');
INSERT INTO `goods_inventory` VALUES ('138', '100', '39', '19', '8');
INSERT INTO `goods_inventory` VALUES ('139', '100', '40', '20', '5');
INSERT INTO `goods_inventory` VALUES ('140', '100', '40', '20', '6');
INSERT INTO `goods_inventory` VALUES ('141', '100', '40', '20', '7');
INSERT INTO `goods_inventory` VALUES ('142', '100', '40', '20', '8');
INSERT INTO `goods_inventory` VALUES ('143', '100', '41', '21', '5');
INSERT INTO `goods_inventory` VALUES ('144', '100', '41', '21', '6');
INSERT INTO `goods_inventory` VALUES ('145', '100', '41', '21', '7');
INSERT INTO `goods_inventory` VALUES ('146', '100', '41', '21', '8');
INSERT INTO `goods_inventory` VALUES ('147', '100', '42', '21', '5');
INSERT INTO `goods_inventory` VALUES ('148', '100', '42', '21', '6');
INSERT INTO `goods_inventory` VALUES ('149', '100', '42', '21', '7');
INSERT INTO `goods_inventory` VALUES ('150', '100', '42', '21', '8');
INSERT INTO `goods_inventory` VALUES ('151', '100', '43', '22', '5');
INSERT INTO `goods_inventory` VALUES ('152', '100', '43', '22', '6');
INSERT INTO `goods_inventory` VALUES ('153', '100', '43', '22', '7');
INSERT INTO `goods_inventory` VALUES ('154', '100', '43', '22', '8');
INSERT INTO `goods_inventory` VALUES ('155', '100', '44', '22', '5');
INSERT INTO `goods_inventory` VALUES ('156', '100', '44', '22', '6');
INSERT INTO `goods_inventory` VALUES ('157', '100', '44', '22', '7');
INSERT INTO `goods_inventory` VALUES ('158', '100', '44', '22', '8');
INSERT INTO `goods_inventory` VALUES ('159', '100', '45', '22', '5');
INSERT INTO `goods_inventory` VALUES ('160', '100', '45', '22', '6');
INSERT INTO `goods_inventory` VALUES ('161', '100', '45', '22', '7');
INSERT INTO `goods_inventory` VALUES ('162', '100', '45', '22', '8');

-- ----------------------------
-- Table structure for goods_size
-- ----------------------------
DROP TABLE IF EXISTS `goods_size`;
CREATE TABLE `goods_size` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `value` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_size
-- ----------------------------
INSERT INTO `goods_size` VALUES ('1', '150', '150');
INSERT INTO `goods_size` VALUES ('2', '160', '160');
INSERT INTO `goods_size` VALUES ('3', '165', '165');
INSERT INTO `goods_size` VALUES ('4', '170', '170');
INSERT INTO `goods_size` VALUES ('5', 'S', 'S');
INSERT INTO `goods_size` VALUES ('6', 'M', 'M');
INSERT INTO `goods_size` VALUES ('7', 'L', 'L');
INSERT INTO `goods_size` VALUES ('8', 'XL', 'XL');
INSERT INTO `goods_size` VALUES ('9', '均码', '均码');

-- ----------------------------
-- Table structure for polls_choice
-- ----------------------------
DROP TABLE IF EXISTS `polls_choice`;
CREATE TABLE `polls_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choice_text` varchar(200) NOT NULL,
  `votes` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_choice_question_id_c5b4b260_fk_polls_question_id` (`question_id`),
  CONSTRAINT `polls_choice_question_id_c5b4b260_fk_polls_question_id` FOREIGN KEY (`question_id`) REFERENCES `polls_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of polls_choice
-- ----------------------------
INSERT INTO `polls_choice` VALUES ('1', '这是好东西', '3', '1');
INSERT INTO `polls_choice` VALUES ('2', 'I am you', '3', '2');
INSERT INTO `polls_choice` VALUES ('3', '哈哈哈', '3', '1');
INSERT INTO `polls_choice` VALUES ('4', '不知道', '0', '1');
INSERT INTO `polls_choice` VALUES ('5', 'i dont know', '1', '3');
INSERT INTO `polls_choice` VALUES ('6', 'hehehe', '0', '3');
INSERT INTO `polls_choice` VALUES ('7', '晴天', '0', '4');
INSERT INTO `polls_choice` VALUES ('8', '阴天', '0', '4');
INSERT INTO `polls_choice` VALUES ('9', '晴转多云', '1', '4');
INSERT INTO `polls_choice` VALUES ('10', '大雨', '1', '4');
INSERT INTO `polls_choice` VALUES ('11', '吃了', '0', '5');
INSERT INTO `polls_choice` VALUES ('12', '没吃', '1', '5');
INSERT INTO `polls_choice` VALUES ('13', '吃了没吃饱', '0', '5');

-- ----------------------------
-- Table structure for polls_question
-- ----------------------------
DROP TABLE IF EXISTS `polls_question`;
CREATE TABLE `polls_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_text` varchar(200) NOT NULL,
  `pub_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of polls_question
-- ----------------------------
INSERT INTO `polls_question` VALUES ('1', '这是什么', '2018-05-22 06:01:49');
INSERT INTO `polls_question` VALUES ('2', 'who are you', '2018-05-22 06:02:15');
INSERT INTO `polls_question` VALUES ('3', 'what is this', '2018-05-22 06:02:33');
INSERT INTO `polls_question` VALUES ('4', '今天天气怎么样', '2018-05-22 08:00:09');
INSERT INTO `polls_question` VALUES ('5', '吃了吗', '2018-05-22 08:00:18');

-- ----------------------------
-- Table structure for user_address
-- ----------------------------
DROP TABLE IF EXISTS `user_address`;
CREATE TABLE `user_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(20) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `isdefault` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `User_address_user_id_08596f52_fk_User_user_id` (`user_id`),
  CONSTRAINT `User_address_user_id_08596f52_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_address
-- ----------------------------
INSERT INTO `user_address` VALUES ('7', 'mlw', '18812345678', '北京市,市辖区,东城区,打算', '1', '3');
INSERT INTO `user_address` VALUES ('8', 'mlw', '18812345678', '北京市,市辖区,东城区,ada', '0', '3');
INSERT INTO `user_address` VALUES ('9', '', '', '北京市,市辖区,东城区,a', '0', '3');
INSERT INTO `user_address` VALUES ('10', 'mlw', '2123123323', '北京市,市辖区,东城区,asdqaw', '0', '3');

-- ----------------------------
-- Table structure for user_user
-- ----------------------------
DROP TABLE IF EXISTS `user_user`;
CREATE TABLE `user_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_user
-- ----------------------------
INSERT INTO `user_user` VALUES ('1', 'hello123@163.con', 'e10adc3949ba59abbe56e057f20f883e');
INSERT INTO `user_user` VALUES ('2', 'mlw123@163.com', 'e10adc3949ba59abbe56e057f20f883e');
INSERT INTO `user_user` VALUES ('3', 'nihao123@163.com', 'e10adc3949ba59abbe56e057f20f883e');
