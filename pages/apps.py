from django.apps import AppConfig
from django.db import connection

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'


class StartupConfig(AppConfig):
    name = 'pages'
    verbose_name = 'pages'
    def ready(self):
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE Employee(
                Employee_num INT NOT NULL,
                Fname VARCHAR(20),
                Lname VARCHAR(20) NOT NULL,
                Salary DECIMAL(10,2) NOT NULL,
                Username VARCHAR(20),
                Password VARCHAR(20) NOT NULL,
                UNIQUE(Username),
                PRIMARY KEY (Employee_num)
            );
            CREATE TABLE Park(
                Name VARCHAR(20) NOT NULL,
                Location VARCHAR(20) NOT NULL,
                Phone_num INT NOT NULL,
                PRIMARY KEY (Name)
            );
            CREATE TABLE `Campsite` (
            `Attraction_name` varchar(20) NOT NULL,
            `Camp_capacity` int NOT NULL,
            `Camp_type` varchar(20) NOT NULL,
            `Camp_condition` varchar(20) NOT NULL,
            `Camp_current_count` int NOT NULL,
            Park_name VARCHAR(20) NOT NULL ,
            Popularity FLOAT NOT NULL,
            PRIMARY KEY(`Attraction_name`),
            FOREIGN KEY(Park_name) REFERENCES Park(Name)
            );
            CREATE TABLE Route(
                Attraction_name VARCHAR(20) NOT NULL,
                Climb_condition VARCHAR(20) NOT NULL,
                Type VARCHAR(20) NOT NULL,
                Grade VARCHAR(20) NOT NULL,
                Safety VARCHAR(20) NOT NULL,
                Quality VARCHAR(20) NOT NULL,
                Park_name VARCHAR(20) NOT NULL,
                PRIMARY KEY(Attraction_name),
                FOREIGN KEY(Park_name) REFERENCES Park(Name)
            );
            CREATE TABLE Trail(
                Attraction_name VARCHAR(20) NOT NULL,
                Length FLOAT NOT NULL,
                Difficulty VARCHAR(20) NOT NULL,
                Type VARCHAR(20) NOT NULL,
                Trail_condition VARCHAR(20) NOT NULL,
                Park_name VARCHAR(20) NOT NULL, 
                PRIMARY KEY(Attraction_name),
                FOREIGN KEY(Park_name) REFERENCES Park(Name)
            );
            CREATE TABLE Camper(
                CaPhone_num INT NOT NULL,
                CaFname VARCHAR(20) NOT NULL,
                CaLname VARCHAR(20) NOT NULL,
                `Previous_stay_location` varchar(20) NOT NULL,
                `Prev_stay_length` INT,
                PRIMARY KEY(CaPhone_num),
                FOREIGN KEY(Previous_stay_location) REFERENCES Campsite(Attraction_name)
            );
            CREATE TABLE `Permits` (
            `Atendee_num` int NOT NULL,
            `Camper_num` int NOT NULL,
            `Price` decimal NOT NULL,
            FOREIGN KEY(`Atendee_num`) REFERENCES Employee(Employee_num),
            FOREIGN KEY(`Camper_num`) REFERENCES Camper(CaPhone_num)
            );
            CREATE TABLE `Stays_At` (
            `Camper_num` int NOT NULL,
            Campsite_name varchar(20) NOT NULL,
            Start_date DATE NOT NULL,
            End_date DATE NOT NULL,
            FOREIGN KEY(`Camper_num`) REFERENCES Camper(CaPhone_num),
            FOREIGN KEY(Campsite_name) REFERENCES Campsite(Attraction_name)
            );
            CREATE TABLE Camp_Attendee (
            Employee_num int(11) NOT NULL,
            Buddy int(11) NOT NULL,
            FOREIGN KEY (Employee_num) REFERENCES Employee(Employee_num)
            );
            CREATE TABLE Maintenance (
            Employee_num int(11) NOT NULL,
            Park_name varchar(20) NOT NULL,
            Rank int(11) NOT NULL,
            FOREIGN KEY (Employee_num) REFERENCES Employee(Employee_num),
            FOREIGN KEY (Park_name) REFERENCES Park(Name)
            );
            CREATE TABLE Repairs (
            Employee_num int(11) NOT NULL,
            Park_name varchar(20) NOT NULL,
            FOREIGN KEY (Employee_num) REFERENCES Employee(Employee_num),
            FOREIGN KEY (Park_name) REFERENCES Park(Name)
            );
            CREATE TABLE Works_At (
            Employee_num int(11) NOT NULL,
            Park_name varchar(20) NOT NULL,
            Attraction_name varchar(20) NOT NULL,
            FOREIGN KEY (Employee_num) REFERENCES Employee(Employee_num),
            FOREIGN KEY (Park_name) REFERENCES Park(Name),
            FOREIGN KEY (Attraction_name) REFERENCES Campsite(Attraction_name)
            );
        ''')
