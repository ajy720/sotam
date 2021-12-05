-- MySQL dump 10.13  Distrib 8.0.24, for macos11 (x86_64)
--
-- Host: localhost    Database: sotam
-- ------------------------------------------------------
-- Server version	5.7.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `sotam`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `sotam` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `sotam`;

--
-- Table structure for table `Main_building`
--

DROP TABLE IF EXISTS `Main_building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Main_building` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `open_time` varchar(5) NOT NULL,
  `close_time` varchar(5) NOT NULL,
  `major` varchar(30) NOT NULL,
  `location` varchar(45) NOT NULL,
  `spell` varchar(2) NOT NULL,
  `name` varchar(20) NOT NULL,
  `tel` varchar(13) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Main_building`
--

LOCK TABLES `Main_building` WRITE;
/*!40000 ALTER TABLE `Main_building` DISABLE KEYS */;
INSERT INTO `Main_building` VALUES (1,'10:00','22:00','','서울 마포구 서강대길 17','A','본관',''),(2,'','','경제학과','서울특별시 마포구 신수동 백범로 35','GN','게페르트 남덕우 경제관',''),(3,'','','커뮤니케이션학부, 지식융합미디어학부','서울 마포구 백범로 23','GA','삼성 가브리엘관',''),(4,'','22:00','경영학과','서울 마포구 서강대길 17','MA','마태오관',''),(5,'','','','서울 마포구 백범로 35','M','메리홀','02-705-8743'),(6,'','','','서울 마포구 백범로 35','I','성이냐시오관','02-705-8161'),(7,'','','','서울 마포구 백범로 35','M','엠마오관',''),(8,'08:00','20:00','','서울 마포구 백범로 35','L','로욜라 도서관',''),(9,'','','','서울 마포구 백범로 35','CY','최양업관',''),(10,'','','글로벌한국학, 아트앤테크놀로지','서울 마포구 백범로 35','X','하비에르관',''),(11,'','','사회과학부','서울 마포구 백범로 35','D','다산관',''),(12,'','','','서울 마포구 백범로 35','GH','곤자가국제학사',''),(13,'','','','서울 마포구 백범로 35','GP','곤자가 플라자',''),(14,'','','','서울 마포구 백범로 35','TE','떼이야르관',''),(15,'','','국제인문학부','서울 마포구 고산16길 58','J','정하상관',''),(16,'','','자연과학부','서울 마포구 백범로 35','RA','리치별관',''),(17,'','','공학부','서울 마포구 백범로 35','AS','아담샬관',''),(18,'','','자연과학부, 공학부','서울 마포구 백범로 35','R','리치과학관',''),(19,'','','경제학과','서울 마포구 서강대길 17','K','김대건관',''),(20,'','','','서울 마포구 서강대길 18','BD','벨라르미노 학사',''),(21,'','','','서울 마포구 백범로 35','AR','아루페관',''),(22,'','','','서울 마포구 백범로 35','G','체육관',''),(23,'','','','서울 마포구 백범로 35','BW','베르크만스 우정원',''),(24,'','','','서울 마포구 고산16길 58','F','포스코 프란치스코관',''),(25,'','','','서울 마포구 백범로 35','AT','알바트로스 탑',''),(26,'','','경영학과','서울 마포구 백범로 23','PA','금호아시아나 바오로 경영관',''),(27,'','','','서울 마포구 백범로 23','T','토마스 모어관',''),(28,'','','','서울 마포구 고산16길 58','BP','대운동장',''),(29,'','','','서울 마포구 백범로 35','YF','청년광장','');
/*!40000 ALTER TABLE `Main_building` ENABLE KEYS */;
UNLOCK TABLES;
