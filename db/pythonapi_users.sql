-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pythonapi
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `useremail` varchar(150) NOT NULL,
  `userpassword` varchar(255) NOT NULL,
  `created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ip` varchar(45) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `useremail` (`useremail`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Frank','franktest@gmail.com','admin123','2026-05-01 04:43:33','2026-05-01 04:43:33','192.168.1.1','USA','NeWyORK',NULL),(2,'Amit','amit1@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543210'),(3,'Rahul','rahul2@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543211'),(4,'Neha','neha3@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543212'),(5,'Priya','priya4@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543213'),(6,'Rohit','rohit5@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543214'),(7,'Karan','karan6@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543215'),(8,'Simran','simran7@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543216'),(9,'Ankit','ankit8@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543217'),(10,'Pooja','pooja9@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543218'),(11,'Vikas','vikas10@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543219'),(12,'Sneha','sneha11@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543220'),(13,'Deepak','deepak12@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543221'),(14,'Manish','manish13@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543222'),(15,'Ritu','ritu14@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543223'),(16,'Sanjay','sanjay15@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543224'),(17,'Alok','alok16@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543225'),(18,'Nisha','nisha17@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543226'),(19,'Tarun','tarun18@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543227'),(20,'Kavita','kavita19@gmail.com','admin123','2026-05-01 11:57:49','2026-05-01 11:57:49',NULL,NULL,NULL,'9876543228');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-01 22:17:03
