-- create a database called iot
-- create a table, use any table name
-- this example uses a table called: rand_one
CREATE TABLE `rand_one` (
  `rand_id` int(11) NOT NULL AUTO_INCREMENT,
  `deviceValue` int(11) DEFAULT NULL,
  `deviceParameter` varchar(45) DEFAULT NULL,
  `deviceId` varchar(45) DEFAULT NULL,
  `event_dateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`rand_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
