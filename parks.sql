--Employee
INSERT INTO Employee VALUES (Employee_num,Fname,Lname,Salary,Username,Password);
DELETE FROM Employee WHERE Employee_num=Empnum;
    --Modify Salary
UPDATE Employee
SET column1 = value1, column2 = value2, ...
WHERE condition;
--Camper
INSERT INTO Camper VALUES (CaPhone_num,CaFname,CaLname,Previous_stay_location,Prev_stay_length);
DELETE FROM Camper WHERE CaPhone_num=Cnum;
    --Modify CaPhone_num
--Park
INSERT INTO Park VALUES (Name,Location, Phone_num);
DELETE FROM Park WHERE Name=Pname;
    --No Modify Function needed
--Route
INSERT INTO Route VALUES (Attraction_name, Climb_condition, Type, Grade, Safety, Quality, Park_name);
DELETE FROM Route WHERE Attraction_name=routename;
    --Modify Climb_condition
--Trail
INSERT INTO Trail VALUES (Attraction_name, Length, Difficulty, Type, Trail_condition, Park_name);
DELETE FROM Trail WHERE Attraction_name=trailname;
    --Modify Trail_condition
--Campsite
INSERT INTO Campsite VALUES (Attraction_name,Camp_capacity, Camp_type, Camp_condition, Camp_current_count, Park_name, Popularity);
DELETE FROM Campsite WHERE Attraction_name=campname;
    --Modify Camp_condition
    --Modify Popularity
--Permits
INSERT INTO Permits VALUES (Attendee_num, Camper_num, Price);
DELETE FROM Permits WHERE Attendee_num=Empnum;
    --Modify Price
--Stays_At
INSERT INTO Stays_At VALUES (Camper_num, Park_name, Start_date, End_date);
DELETE FROM Stays_At WHERE Camper_num=Cnum;
    --No Modify Function needed
--Camp_Attendee 
INSERT INTO Camp_Attendee VALUES (Employee_num, Buddy);
DELETE FROM Camp_Attendee WHERE Employee_num=Empnum;
    --No Modify Function needed
--Maintenance 
INSERT INTO Maintenance VALUES (Employee_num, Park_name, Rank);
DELETE FROM Maintenance WHERE Employee_num=Empnum;
    --Modify Rank
--Repairs 
INSERT INTO Repairs VALUES (Employee_num, Park_name);
DELETE FROM Repairs WHERE Employee_num=Empnum;
    --Modify Park_name
--Works_At 
INSERT INTO Works_At VALUES (Employee_num, Park_name, Attraction_name);
DELETE FROM Works_At WHERE Employee_num=Empnum;
    --No Modify Function needed