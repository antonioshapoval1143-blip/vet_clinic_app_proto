-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 25.44.219.6    Database: vet_clinic
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  `adress` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `location` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `phone_number` int DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1000002 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'Шаповал','Антон','Олексійович','Адміністратор',NULL,NULL,NULL),(2,'Відʼємний','Іван','Ігорович','Адміністратор',NULL,'',NULL),(1000001,'super','man','-','Адміністратор','-','-',5554180);
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `appointment_date` date DEFAULT NULL,
  `appointment_time` time DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`),
  KEY `patient_id` (`patient_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (1,1,6,'2025-04-30','11:00:00','очікує'),(2,4,6,'2025-04-30','12:00:00','завершено'),(3,5,5,'2025-05-31','10:30:00','скасовано'),(4,1,5,'2025-07-31','09:00:00','скасовано'),(5,1,5,'2025-06-30','07:00:00','скасовано');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `adress` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  `animal_type` varchar(100) DEFAULT NULL,
  `work_format` varchar(100) DEFAULT NULL,
  `contact_info` text,
  `experience_years` int DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (4,'нана','нао','-','-','-','Терапевт загальної практики','-','Часткова зайнятість','5054758',1),(5,'Котов','Кирило','Вадимович','вул. Героїв','м. Київ','Терапевт загальної практики','Котові','Повна зайнятість','380982750919',3),(6,'Пила','Андрій','Степанович','Якийсь пров. буд. 1','м. Якесь','Хірург','Котові','Повна зайнятість','44413',4);
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctorschedule`
--

DROP TABLE IF EXISTS `doctorschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctorschedule` (
  `schedule_id` int NOT NULL,
  `doctor_id` int DEFAULT NULL,
  `weekday` enum('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday') DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  PRIMARY KEY (`schedule_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `doctorschedule_ibfk_1` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctorschedule`
--

LOCK TABLES `doctorschedule` WRITE;
/*!40000 ALTER TABLE `doctorschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `doctorschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `owners`
--

DROP TABLE IF EXISTS `owners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `owners` (
  `owner_id` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `address` text,
  `location` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `additional_contact` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owners`
--

LOCK TABLES `owners` WRITE;
/*!40000 ALTER TABLE `owners` DISABLE KEYS */;
INSERT INTO `owners` VALUES (1,'Іванов','Іван','Іванович','м. Дніпро',NULL,'380985246545','-','-'),(2,'yes','man','-','-','mojave','5553510','-','-'),(3,'Петров','Петро','Петрович','вул. Якась','м. Якесь','380560504784','-','-');
/*!40000 ALTER TABLE `owners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `species` varchar(50) DEFAULT NULL,
  `breed` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `weight_kg` decimal(5,2) DEFAULT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `patients_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `owners` (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,'Вергілій','Кіт','Сіамський',3,4.00,2),(2,'Мурчалко','Кіт','Ангорський',2,5.00,3),(3,'Пухнастик','Кіт','Манул',1,3.00,2),(4,'Дивак','Кіт','Плямисто-рудий',3,1.00,1),(5,'Злюка','Каракал','звичайний',3,16.00,1);
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reg_keys`
--

DROP TABLE IF EXISTS `reg_keys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reg_keys` (
  `key_id` int NOT NULL AUTO_INCREMENT,
  `keys` int NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`key_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reg_keys`
--

LOCK TABLES `reg_keys` WRITE;
/*!40000 ALTER TABLE `reg_keys` DISABLE KEYS */;
INSERT INTO `reg_keys` VALUES (1,1245,'apr'),(2,7928,'apr');
/*!40000 ALTER TABLE `reg_keys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treatments`
--

DROP TABLE IF EXISTS `treatments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treatments` (
  `treatment_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `diagnosis` text,
  `prescribed_treatment` text,
  `visit_date` date DEFAULT NULL,
  `service_cost` decimal(10,2) DEFAULT NULL,
  `payment_status` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`treatment_id`),
  KEY `patient_id` (`patient_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `treatments_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `treatments_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treatments`
--

LOCK TABLES `treatments` WRITE;
/*!40000 ALTER TABLE `treatments` DISABLE KEYS */;
INSERT INTO `treatments` VALUES (2,4,6,'Здоровий','Процедура УЗД','2025-04-30',550.00,'Paid');
/*!40000 ALTER TABLE `treatments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_actions_log`
--

DROP TABLE IF EXISTS `user_actions_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_actions_log` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `action_type` varchar(50) NOT NULL,
  `description` text,
  `action_date` date NOT NULL,
  `action_time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_actions_log_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users_login` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_actions_log`
--

LOCK TABLES `user_actions_log` WRITE;
/*!40000 ALTER TABLE `user_actions_log` DISABLE KEYS */;
INSERT INTO `user_actions_log` VALUES (1,1,'Авторизація','1 увійшов в аккаунт типу adm з id 1','2025-05-01','16:01:04'),(2,1,'Авторизація','1 увійшов в аккаунт типу adm з id 1','2025-05-01','17:00:21'),(3,1,'Авторизація','1 увійшов в аккаунт типу adm з id 1','2025-05-01','17:01:12');
/*!40000 ALTER TABLE `user_actions_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_login`
--

DROP TABLE IF EXISTS `users_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_login` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `phone_login` varchar(20) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `user_type` varchar(255) NOT NULL,
  `id_in_list` int NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `phone_login` (`phone_login`)
) ENGINE=InnoDB AUTO_INCREMENT=1000006 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_login`
--

LOCK TABLES `users_login` WRITE;
/*!40000 ALTER TABLE `users_login` DISABLE KEYS */;
INSERT INTO `users_login` VALUES (1,'45380','$argon2i$v=19$m=16,t=2,p=1$MTIzNDU2Nzg$Ruse7d9gunh/m5qHsF+cdw','adm',1),(2,'380985246545','$argon2i$v=19$m=16,t=2,p=1$MTIzNDU2Nzg$2cLeohOGHT0GxOC7vHSuuA','usr',1),(3,'5054758','$argon2i$v=19$m=16,t=2,p=1$MTIzNDU2Nzg$6G8Yl1oV6JT72xTzclLNpg','doc',4),(1000001,'5554180','$argon2i$v=19$m=16,t=2,p=1$MTIzNDU2Nzg$BaXdv/eRVAWsS647YKy3/w','adm',1000001),(1000002,'5553510','$argon2i$v=19$m=16,t=2,p=1$MTIzNDU2Nzg$6G8Yl1oV6JT72xTzclLNpg','usr',2),(1000003,'380560504784','$argon2i$v=19$m=16,t=2,p=1$MTIzNDU2Nzg$BaXdv/eRVAWsS647YKy3/w','usr',3),(1000004,'380982750919','$argon2i$v=19$m=16,t=2,p=1$MTIzNDU2Nzg$gNHXhP8Lm42GAHwn9C0tWg','doc',5),(1000005,'44413','$argon2i$v=19$m=16,t=2,p=1$MTIzNDU2Nzg$jiWh1sWVzvpUWLrAw/7p8Q','doc',6);
/*!40000 ALTER TABLE `users_login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-01 17:02:00
