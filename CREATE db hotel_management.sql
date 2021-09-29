CREATE DATABASE  IF NOT EXISTS `hotel_management` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hotel_management`;
-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hotel_management
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `bills`
--

DROP TABLE IF EXISTS `bills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills` (
  `Bill_id` char(5) DEFAULT NULL,
  `customer_name` char(50) NOT NULL,
  `Sr_No` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `discount` int DEFAULT NULL,
  `net_to_be_paid` int DEFAULT ((`amount` - `discount`)),
  `payment_method` enum('cash','credit card','debit card') DEFAULT NULL,
  UNIQUE KEY `Bill_id` (`Bill_id`),
  UNIQUE KEY `Bill_id_2` (`Bill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills`
--

LOCK TABLES `bills` WRITE;
/*!40000 ALTER TABLE `bills` DISABLE KEYS */;
INSERT INTO `bills` VALUES ('AA001','Pappu Lal',1,3000,300,2700,'credit card'),('AA002','Swapnil Garg',2,9000,900,8100,'debit card'),('AA003','Manas Pagrani',3,4000,400,3600,'credit card'),('AA004','Kartikeya Gangwar',4,13000,1300,11700,'cash'),('AA005','Lakshya Agarwal',5,18000,1800,16200,'cash'),('AA006','Ram Kumar',6,2000,200,1800,'debit card'),('AA007','Rajat Sharma',7,14000,1400,12600,'cash'),('AA008','Felix',9,6000,600,5400,'credit card');
/*!40000 ALTER TABLE `bills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `Sr_No` int NOT NULL AUTO_INCREMENT,
  `fName` char(100) NOT NULL,
  `Phone_Number` bigint DEFAULT NULL,
  `customer_id` char(100) NOT NULL,
  `id_number` char(50) NOT NULL,
  `doa` datetime DEFAULT CURRENT_TIMESTAMP,
  `doc` datetime DEFAULT NULL,
  `room_id` int NOT NULL,
  PRIMARY KEY (`Sr_No`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Pappu Lal',9123456789,'Aadhar','888844442222','2021-05-13 00:00:00','2021-05-15 00:00:00',1001),(2,'Swapnil Garg',8899221234,'PanCard','UXA1234567','2021-05-14 00:00:00','2021-05-18 00:00:00',1002),(3,'Manas Pagrani',8621696942,'Aadhar','642166221243','2021-05-18 00:00:00','2021-05-19 00:00:00',1003),(4,'Kartikeya Gangwar',4404207601,'PanCard','UXB1124789','2021-07-01 00:00:00','2021-07-08 00:00:00',1002),(5,'Lakshya Agarwal',8341213312,'Driving Licence','UP92334B','2021-07-02 00:00:00','2021-07-07 00:00:00',1003),(6,'Ram Kumar',3334356789,'PanCard','UXA92334333','2021-07-03 00:00:00','2021-07-04 00:00:00',1005),(7,'Rajat Sharma',8219983729,'Aadhar','862431229837','2021-09-05 00:00:00','2021-09-19 11:50:34',1001),(8,'Kushagra Singh',7060880220,'VoterID','UPAB99233','2021-09-08 00:00:00',NULL,1002),(9,'Felix',9988776655,'Aadhar','999988887777','2021-09-19 12:35:00','2021-09-21 22:51:45',1003),(10,'Sandeep Garg',9876543219,'Aadhar','109090901010','2021-09-19 15:15:20',NULL,1001),(11,'Raman Dubey',1234567823,'PanCard','UXZ1021332','2021-09-21 22:50:38',NULL,1010);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rooms` (
  `room_id` int DEFAULT NULL,
  `room_type` enum('basic','deluxe','luxury','suite') DEFAULT NULL,
  `room_floor` char(10) DEFAULT NULL,
  `Occupied_by_customer` int DEFAULT NULL,
  `cost_pernight` int DEFAULT (1000),
  `availabilty` enum('available','booked') DEFAULT NULL,
  UNIQUE KEY `room_id` (`room_id`),
  UNIQUE KEY `room_id_2` (`room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES (1001,'basic','Ground',10,1000,'booked'),(1002,'deluxe','Ground',8,1500,'booked'),(1003,'luxury','Ground',NULL,3000,'available'),(1004,'basic','First',NULL,1000,'available'),(1005,'deluxe','First',NULL,1500,'available'),(1006,'luxury','First',NULL,3000,'available'),(1007,'basic','Second',NULL,1000,'available'),(1008,'deluxe','Second',NULL,1500,'available'),(1009,'luxury','Second',NULL,3000,'available'),(1010,'suite','Third',11,9000,'booked');
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-29 17:35:59
