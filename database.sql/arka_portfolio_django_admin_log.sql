-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: arka_portfolio
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-08-23 20:46:20.046464','2','adv',1,'[{\"added\": {}}]',7,1),(2,'2025-08-23 20:52:29.583344','2','adv',3,'',7,1),(3,'2025-08-23 21:01:07.077574','1','Arka Maitra - abc',1,'[{\"added\": {}}]',9,1),(4,'2025-08-23 21:06:26.793399','1','E-Commerce Platform',2,'[{\"changed\": {\"fields\": [\"Technologies\"]}}]',14,1),(5,'2025-08-23 21:26:39.185105','1','Arka Maitra',1,'[{\"added\": {}}]',16,1),(6,'2025-08-23 21:35:24.477530','5','MySQL (Databases)',3,'',12,1),(7,'2025-08-23 21:35:44.783561','3','Django (Frameworks & Libraries)',3,'',12,1),(8,'2025-08-23 21:35:44.783612','2','JavaScript (Programming Languages)',3,'',12,1),(9,'2025-08-23 21:35:44.783644','1','Python (Programming Languages)',3,'',12,1),(10,'2025-08-23 21:35:44.783673','4','React (Frameworks & Libraries)',3,'',12,1),(11,'2025-08-23 21:47:17.495836','6','DRF (Frameworks & Libraries)',1,'[{\"added\": {}}]',12,1),(12,'2025-08-23 21:50:53.363016','1','E-Commerce Platform',2,'[{\"changed\": {\"fields\": [\"Technologies\"]}}]',14,1),(13,'2025-08-23 22:41:08.034098','7','React Js (Programming Languages)',1,'[{\"added\": {}}]',12,1),(14,'2025-08-23 22:42:13.959810','8','Java Script (Programming Languages)',1,'[{\"added\": {}}]',12,1),(15,'2025-08-23 23:19:52.268085','1','Bachelor of Technology in Computer Science and Engineering from Indian Institute of Technology',3,'',10,1),(16,'2025-08-23 23:21:47.898218','2','Diploma in computer science and technology from Nalhati government polytechnic',1,'[{\"added\": {}}]',10,1),(17,'2025-08-23 23:25:15.146690','1','E-Commerce Platform',2,'[{\"changed\": {\"fields\": [\"Image\", \"Technologies\"]}}]',14,1),(18,'2025-08-24 12:08:20.761979','5','Arka Maitra - bh',3,'',9,1),(19,'2025-08-24 12:08:20.762110','4','Arka Maitra - bh',3,'',9,1),(20,'2025-08-24 12:08:20.762121','3','Arka Maitra - bh',3,'',9,1),(21,'2025-08-24 12:08:20.762129','2','Arka Maitra - bh',3,'',9,1),(22,'2025-08-24 12:08:20.762136','1','Arka Maitra - abc',3,'',9,1),(23,'2025-08-24 12:09:11.967870','6','Arka Maitra - abc',2,'[{\"changed\": {\"fields\": [\"Is read\"]}}]',9,1),(24,'2025-08-24 12:17:23.877748','7','Arka Maitra - abc',3,'',9,1),(25,'2025-08-24 12:17:23.877845','6','Arka Maitra - abc',3,'',9,1),(26,'2025-08-24 12:28:52.901898','2','Diploma in computer science and technology from Nalhati government polytechnic',2,'[{\"changed\": {\"fields\": [\"Institution logo\"]}}]',10,1),(27,'2025-08-24 12:35:14.774667','2','Task Management App',2,'[{\"changed\": {\"fields\": [\"Image\", \"Technologies\"]}}]',14,1),(28,'2025-08-24 12:36:13.070903','1','Sarah Johnson - Project Manager at Tech Solutions Inc.',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',13,1),(29,'2025-08-24 12:42:23.638942','1','Arka Maitra',2,'[{\"changed\": {\"fields\": [\"Profile image\"]}}]',7,1),(30,'2025-08-24 12:43:08.736095','1','Arka Maitra',2,'[{\"changed\": {\"fields\": [\"Profile image\"]}}]',7,1),(31,'2025-08-24 12:47:59.204053','1','Arka Maitra',2,'[{\"changed\": {\"fields\": [\"Profile image\"]}}]',7,1),(32,'2025-08-24 12:48:23.325870','1','Arka Maitra',2,'[{\"changed\": {\"fields\": [\"Profile image\"]}}]',7,1),(33,'2025-08-24 12:49:16.808238','1','Arka Maitra',2,'[{\"changed\": {\"fields\": [\"Profile image\"]}}]',7,1),(34,'2025-08-24 12:54:10.077676','11','Arka Maitra - abc',3,'',9,1),(35,'2025-08-24 12:54:10.077860','10','Arka Maitra - abc',3,'',9,1),(36,'2025-08-24 12:54:10.077871','9','Arka Maitra - abc',3,'',9,1),(37,'2025-08-24 12:54:10.077879','8','Arka Maitra - abc',3,'',9,1),(38,'2025-08-24 13:42:07.444264','14','Arka Maitra - bh',3,'',9,1),(39,'2025-08-24 13:42:07.444984','13','Arka Maitra - bh',3,'',9,1),(40,'2025-08-24 13:42:07.445000','12','Arka Maitra - bh',3,'',9,1),(41,'2025-08-24 13:44:07.029223','18','dd - bh',3,'',9,1),(42,'2025-08-24 13:44:07.029434','17','Arka Maitra - bh',3,'',9,1),(43,'2025-08-24 13:44:07.029469','16','Arka Maitra - bh',3,'',9,1),(44,'2025-08-24 13:44:07.029478','15','Arka Maitra - bh',3,'',9,1),(45,'2025-08-24 13:44:40.395836','20','dd - bh',3,'',9,1),(46,'2025-08-24 13:44:40.395905','19','dd - bh',3,'',9,1),(47,'2025-08-24 14:03:20.671466','21','Arka Maitra - cc',2,'[{\"changed\": {\"fields\": [\"Is read\"]}}]',9,1),(48,'2025-08-24 15:02:19.427382','40','Arka Maitra - ss',3,'',9,1),(49,'2025-08-24 15:02:19.427441','39','Arka Maitra - ss',3,'',9,1),(50,'2025-08-24 15:02:19.427467','38','Arka Maitra - ss',3,'',9,1),(51,'2025-08-24 15:02:19.427486','37','Arka Maitra - ss',3,'',9,1),(52,'2025-08-24 15:02:19.427505','36','Arka Maitra - ss',3,'',9,1),(53,'2025-08-24 15:02:19.427532','35','Arka Maitra - ss',3,'',9,1),(54,'2025-08-24 15:02:19.427550','34','Arka Maitra - ss',3,'',9,1),(55,'2025-08-24 15:02:19.427567','33','Arka Maitra - ss',3,'',9,1),(56,'2025-08-24 15:02:19.427583','32','Arka Maitra - ss',3,'',9,1),(57,'2025-08-24 15:02:19.427599','31','Arka Maitra - ss',3,'',9,1),(58,'2025-08-24 15:02:19.427614','30','Arka Maitra - ss',3,'',9,1),(59,'2025-08-24 15:02:19.427631','29','Arka Maitra - ss',3,'',9,1),(60,'2025-08-24 15:02:19.427648','28','Arka Maitra - ss',3,'',9,1),(61,'2025-08-24 15:02:19.427664','27','Arka Maitra - ss',3,'',9,1),(62,'2025-08-24 15:02:19.427680','26','Arka Maitra - ss',3,'',9,1),(63,'2025-08-24 15:02:19.427698','25','Arka Maitra - ss',3,'',9,1),(64,'2025-08-24 15:02:19.427715','24','Arka Maitra - ss',3,'',9,1),(65,'2025-08-24 15:02:19.427731','23','Arka Maitra - ss',3,'',9,1),(66,'2025-08-24 15:02:19.427747','22','Arka Maitra - cc',3,'',9,1),(67,'2025-08-24 15:02:19.427765','21','Arka Maitra - cc',3,'',9,1),(68,'2025-08-24 15:38:43.521114','48','Arka Maitra - ss',3,'',9,1),(69,'2025-08-24 15:38:43.522156','47','Arka Maitra - ss',3,'',9,1),(70,'2025-08-24 15:38:43.522184','46','Arka Maitra - ss',3,'',9,1),(71,'2025-08-24 15:38:43.522205','45','Arka Maitra - zzzzzz',3,'',9,1),(72,'2025-08-24 15:38:43.522224','44','Arka Maitra - bh',3,'',9,1),(73,'2025-08-24 15:38:43.522242','43','Arka Maitra - bh',3,'',9,1),(74,'2025-08-24 15:38:43.522260','42','Arka Maitra - bh',3,'',9,1),(75,'2025-08-24 15:38:43.522276','41','Arka Maitra - bh',3,'',9,1),(76,'2025-08-24 15:42:13.341029','51','Arka Maitra - xxxx',3,'',9,1),(77,'2025-08-24 15:42:13.341252','50','Arka Maitra - xxxx',3,'',9,1),(78,'2025-08-24 15:42:13.341280','49','Arka Maitra - ss',3,'',9,1),(79,'2025-08-24 16:50:27.385126','1','Arka Maitra',2,'[{\"changed\": {\"fields\": [\"Phone\", \"Location\", \"Github\", \"Linkedin\", \"Resume\"]}}]',7,1),(80,'2025-08-24 16:51:11.864699','1','Arka Maitra',2,'[{\"changed\": {\"fields\": [\"Linkedin\"]}}]',7,1),(81,'2025-08-24 16:51:20.471927','1','Arka Maitra',2,'[]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-25  0:21:23
