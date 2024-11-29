# Planning the number of databases

Databases are different from database schemas. Database schemas can share the same database.
Business Automation Workflow components such
as Messaging, BusinessSpace, and ProcessServer are assigned to database schemas. When no name
conflicts occur between database objects, components can share the same database. Components such as
Process Server and Performance Data Warehouse (PDW) do not have database schema support; therefore,
they cannot share the same database.

| Database                                        | Schema          | Components                                                                                                                                                                              |
|-------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMNDB (the common database)                     | SharedDB        | Messaging (Messaging Engine), FEM (Failed Event Manager), BusinessSpace (BSpace), Business Process Choreographer (BPC), and Event Sequencing                                            |
| CMNDB (the common database)                     | CellOnlyDB      | Application scheduler (AppSched), Mediations (Meds), Relationship manager (Rels), Enterprise Service Bus Logger Mediation (ESBLogMed), and Customization (Business Rules and Selectors) |
| BPMDB (the Process database)                    | ProcessServerDB | Workflow Server (ProcessServer) (and BPM content store (EmbeddedECM)                                                                                                                    |
| PDWDB (the Performance Data Warehouse database) | PerformanceDB   | Performance Data Warehouse                                                                                                                                                              |
| CPEDB (the Content database)                    | DosDb           | Design Object Store                                                                                                                                                                     |
| CPEDB (the Content database)                    | TosDb           | Target Object Store                                                                                                                                                                     |
| CPEDB (the Content database)                    | CaDb            | Case Analyzer Object Store                                                                                                                                                              |
| CPEDB (the Content database)                    | ChDb            | Case History Object Store                                                                                                                                                               |
| CPEDB (the Content database)                    | ICNDb           | IBM® Content Navigator                                                                                                                                                                  |

- The CellOnlyDB schema exists only in the Advanced and AdvancedOnly deployment environments, and
is part of the CMNDB database by default.
- If you configured an Express deployment environment, the default configuration uses two
databases, BPMDB and PDWDB.
- If you configured an AdvancedOnly deployment environment, the default configuration uses one
database, CMNDB, with the corresponding database schemas (CellOnlyDB and SharedDB) and assigned
components.
- For PostgreSQL, CMNDB
is not needed because there is no common database.