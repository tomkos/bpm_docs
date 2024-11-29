# Configuring your databases

- Updating IBM Business Automation Workflow data sources

If you need to modify one or more properties for an IBM Business Automation Workflow data source, or you find that your initial configuration is incorrect for an Oracle data source, you must use the BPMConfig command to make the required updates. You cannot make the updates using the administrative console.
- Configuring JDBC drivers

IBM Business Automation Workflow includes Java database connectivity (JDBC) drivers for DB2 databases. The versions of the DB2 JDBC drivers that are included are determined by the levels of the corresponding database products that were supported by the particular release of Business Automation Workflow. You should update the JDBC drivers whenever another level of a database product is released, to avoid unexpected errors from failures that originate from the drivers. If you are using Oracle or SQL Server databases, you must configure your own JDBC drivers.
- Configuring Oracle Real Application Cluster (RAC) for use with IBM Business Automation Workflow

Oracle Real Application Clusters (RAC) is an option of an Oracle database that brings together two or more computers to form a clustered database that behaves as a single system. In a RAC database, Oracle processes that run in separate nodes access the same data from a shared disk storage.