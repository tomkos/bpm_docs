# Creating and configuring SQL Server databases

- Configuring XA transactions

You must configure XA transactions after the Microsoft SQL Server database is installed and before you start the server. The SQL Server JDBC driver provides support for Java Platform, Enterprise Edition/JDBC 2.0 optional distributed transactions. JDBC connections obtained from the SQLServerXADataSource class can participate in standard distributed transaction processing environments such as Java Platform, Enterprise Edition (Java EE) application servers.
- Creating SQL Server databases

You can create the required databases for IBM Business Automation Workflow either before or after you run the BPMConfig command with the -create -de parameters to create profiles and configure your deployment environment.
- Creating users and schemas for SQL Server databases

You must create the users and schemas after creating the SQL Server databases.