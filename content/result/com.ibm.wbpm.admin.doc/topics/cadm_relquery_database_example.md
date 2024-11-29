<!-- image -->

# Example: Querying relationship data using database views

The data is correlated using the IBM® Business Automation Workflow relationship
service. Each application contains similar customer information, with
an identity relationship to correlate the information between each
application.

The following three tables show the data as it is stored within
each database:

| Given Name   | Last Name   | Home Phone    | ID        |
|--------------|-------------|---------------|-----------|
| Jessica      | Reed        | 111 111 11111 | clarify\_1 |
| Tara         | McLean      | 333 333 33333 | clarify\_2 |

| Given Name   | Last Name   | Home Phone    | ID     |
|--------------|-------------|---------------|--------|
| Jessica      | Reed        | 111 111 11111 | sap\_10 |
| Tara         | McLean      | 333 333 33333 | sap\_8  |

| Full Name    | Home Phone    | ID       |
|--------------|---------------|----------|
| Jessica Reed | 111 111 11111 | siebel\_6 |
| Tara McLean  | 333 333 33333 | siebel\_8 |

The customer business object definition names and elements (created
in Integration Designer for
each database) are shown in the following table:

| ClarifyCustomer   | ClarifyCustomer   | SapCustomer   | SapCustomer   | SiebelCustomer   | SiebelCustomer   |
|-------------------|-------------------|---------------|---------------|------------------|------------------|
| Element           | Type              | Element       | Type          | Element          | Type             |
| givenName         | string            | firstName     | string        | fullName         | string           |
| lastName          | string            | lastName      | string        |                  |                  |
| homePhone         | string            | homePhone     | string        | homePhone        | string           |
| clarifyId         | string            | sapId         | string        | siebelId         | string           |

| Relationship name   | Role name       | Business object name   | Key       |
|---------------------|-----------------|------------------------|-----------|
| ID                  | GenCustomer     | GenCustomer            | genId     |
| ID                  | ClarifyCustomer | ClarifyCustomer        | clarifyId |
| ID                  | SapCustomer     | SapCustomer            | sapId     |
| ID                  | SiebelCustomer  | SiebelCustomer         | siebelId  |

- http://CustomerModule/ClarifyCustomer
- http://CustomerModule/SapCustomer
- http://CustomerModule/SiebelCustomer

| VIEW\_NAME                   | RELATIONSHIP\_NAME              | ROLE\_NAME                             |
|-----------------------------|--------------------------------|---------------------------------------|
| V\_ID\_CLARIFYCUSTOMER\_098    | http://CustomerModule/ID       | http://CustomerModule/ClarifyCustomer |
| V\_ID\_SAPCUSTOMER\_515        | http://CustomerModule/ID       | http://CustomerModule/SapCustomer     |
| V\_ID\_SIEBELCUSTOMER\_411     | http://CustomerModule/ID       | http://CustomerModule/SiebelCustomer  |
| V\_USASTATE\_ABBREVIATION\_DE8 | http://CustomerModule/USASTATE | http://CustomerModule/Abbreviation    |
| V\_USASTATE\_CODE\_B32         | http://CustomerModule/USASTATE | http://CustomerModule/Code            |
| V\_USASTATE\_NAME\_933         | http://CustomerModule/USASTATE | http://CustomerModule/FullName        |

| Column Name        | Data Type                         | Value    | Description                                                                                                                                                                                                                                                                                                                                             |
|--------------------|-----------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KEY\_ATTRIBUTE\_NAME | depends on the key attribute type | Not null | This is where the role instance data is stored. For identity relationships, the column is named by the name of the key attribute. For example, SAPCUSTOMER\_SAPID will use sapid as the key attribute name and sapcustomer as the business object name. One column is defined for each key attribute. For static relationships, the column is named DATA |

| Clarify role view         | SAP role view           | Siebel role view        |
|---------------------------|-------------------------|-------------------------|
| INSTANCEID                | INSTANCEID              | INSTANCEID              |
| CLARIFYCUSTOMER\_CLARIFYID | SAPCUSTOMER\_SAPID       | SIEBELCUSTOMER\_SIEBELID |
| STATUS                    | STATUS                  | STATUS                  |
| LOGICAL\_STATE             | LOGICAL\_STATE           | LOGICAL\_STATE           |
| LOGICAL\_STATE\_TIMESTAMP   | LOGICAL\_STATE\_TIMESTAMP | LOGICAL\_STATE\_TIMESTAMP |
| CREATE\_TIMESTAMP          | CREATE\_TIMESTAMP        | CREATE\_TIMESTAMP        |
| UPDATE\_TIMESTAMP          | UPDATE\_TIMESTAMP        | UPDATE\_TIMESTAMP        |
| ROLEID                    | ROLEID                  | ROLEID                  |

```
//Create a table to store ID values from all three applications for each customer, 
//and associate a unique instance ID with each customer. Use this table as a base 
//source table to populate relationship tables.
CREATE TABLE joint\_t (instanceid INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
clarify\_id VARCHAR(10) NOT NULL,
sap\_id VARCHAR(10) NOT NULL,
siebel\_id VARCHAR(10) NOT NULL)

//Compare the name and home phone number across the three application tables. 
//If a match is found, insert that person's ID value from each application table 
//into the joint\_t table. Associate the three ID values to a unique ID; this 
//ID will be used later as the relationship instance ID. 
INSERT INTO joint\_t (clarify\_id,sap\_id,siebel\_id)
SELECT A.ID, B.ID, C.ID
FROM clarifycustomer A,sapcustomer B, siebelcustomer C
WHERE A.homephone=B.homephone AND
B.homephone=C.homephone, AND
B.givenname=C.firstname AND
B.lastname=C.lastname AND 
A.fullname=C.firstname CONCAT ' ' CONCAT C.lastname

//Create a sequence for each application; this sequence will be 
//used later as a role ID in each role table.
CREATE SEQUENCE clarify\_roleid MINVALUE 1 ORDER CACHE 100
CREATE SEQUENCE sap\_roleid MINVALUE 1 ORDER CACHE 100
CREATE SEQUENCE siebel\_roleid MINVALUE 1 ORDER CACHE 100

//Populate the role instance table for the CLARIFY role.
INSERT INTO V\_ID\_CLARIFYCUSTOMER\_098 (instanceid, roleid,
  clarifycustomer\_clarifyid, status, logical\_state, logical\_state\_timestamp,
  create\_timestamp, update\_timestamp)
FROM joint\_t

//Populate the role instance table for the SAP role.
INSERT INTO V\_ID\_SAPCUSTOMER\_515 (instanceid, roleid, sapcustomer\_sapid,
  status, logical\_state, logical\_state\_timestamp, create\_timestamp,
  update\_timestamp)
SELECT instanceid NEXTVAL FOR sap\_roleid, sap\_id, 0, 0, current
  timestamp, current timestamp, current timestamp
FROM joint\_t

//Populate the role instance table for the SIEBEL role.
INSERT INTO V\_ID\_SIEBELCUSTOMER\_AFC (instanceid, roleid, siebelcustomer\_siebelid,
  status, logical\_state, logical\_state\_timestamp, create\_timestamp, update\_timestamp)
SELECT instanceid, NEXTVAL FOR siebel\_roleid, sap\_id, 0, 0, current timestamp,
  current timestamp, current timestamp
FROM joint\_t
```