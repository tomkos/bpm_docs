# Creating and configuring SQL Server databases before typical
installation

- Configuring XA transactions for SQL Server

You must configure XA transactions after the Microsoft SQL Server database is installed and before you start the server. The SQL Server JDBC driver provides support for Java Platform, Enterprise Edition/JDBC 2.0 optional distributed transactions. JDBC connections obtained from the SQLServerXADataSource class can participate in standard distributed transaction processing environments such as Java Platform, Enterprise Edition (Java EE) application servers.
- Creating SQL Server databases

You must create the required databases before you install IBM Business Automation Workflow. Usually you require the Process database, the Performance Data Warehouse database, the Common database, and the Content database. In the case of an AdvancedOnly deployment environment, you need only the Common database.
- Creating users and schemas for SQL Server databases

You must create the users and schemas after creating the SQL Server databases.