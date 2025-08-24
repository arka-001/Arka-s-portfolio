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
-- Table structure for table `portfolio_project`
--

DROP TABLE IF EXISTS `portfolio_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `portfolio_project` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `short_description` varchar(300) NOT NULL,
  `project_type` varchar(20) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `github_url` varchar(200) NOT NULL,
  `live_url` varchar(200) NOT NULL,
  `demo_url` varchar(200) NOT NULL,
  `featured` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `order` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_project`
--

LOCK TABLES `portfolio_project` WRITE;
/*!40000 ALTER TABLE `portfolio_project` DISABLE KEYS */;
INSERT INTO `portfolio_project` VALUES (1,'E-Commerce Platform','A full-featured e-commerce platform built with Django and React.','Modern e-commerce platform with Django backend and React frontend','web','projects/bd58b8d1-df49-4f04-8c54-81510ba29d46.png','https://github.com/arkamaitra/ecommerce-platform','https://ecommerce-demo.arkamaitra.com','',1,1,0,'2025-08-23 16:13:52.483693','2025-08-23 23:25:15.128888'),(2,'Task Management App','A collaborative task management application with real-time updates.','Collaborative task management with real-time updates','web','projects/4e09085e-e9a1-433f-bbce-eba86805eaaf.png','https://github.com/arkamaitra/task-manager','https://task-manager.arkamaitra.com','',1,1,0,'2025-08-23 16:13:52.487031','2025-08-24 12:35:14.755430');
/*!40000 ALTER TABLE `portfolio_project` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-25  0:21:22
