# PostgreSQL database
privileges

PostgreSQL
manages database access permissions by using roles. A role can consist of a database user or a group
of database users, depending on your role configuration.

When you create database schemas
using the typical installation or database scripts that are generated using the
BPMConfig command-line utility, your role ID must have the authority to create
tables. When the tables are created, you must have the authority to select, insert, update, and
delete information in the tables.

- Sufficient privilege to create relational tables and indexes.
- ALTER, DELETE, INSERT, REFERENCES, SELECT, UPDATE and CREATE OR REPLACE PROCEDURE privileges on
the created tables

- SELECT, INSERT, UPDATE, and DELETE privileges on the tables.
- EXECUTE ON PROCEDURE privilege on stored procedures.

| Component                                                                                | Installation and upgrade privileges                                                                                                                            | Runtime privileges                                                   |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Process ServerNote: Only the Process Server component applies to Workflow on containers. | CREATE TABLE, ALTER TABLE, CREATE SCHEMA, SELECT, INSERT, UPDATE TABLE, DROP TABLE, CREATE INDEX, CREATE UNIQUE INDEX, CREATE OR REPLACE PROCEDURE, REFERENCES | CREATE, SELECT, UPDATE, DELETE, INSERT, CREATE PROCEDURE, DROP TABLE |
| Performance Data Warehouse                                                               | CREATE TABLE, CREATE SCHEMA, ALTER TABLE, SELECT, INSERT, UPDATE TABLE, DROP TABLE, CREATE INDEX, CREATE UNIQUE INDEX, REFERENCES                              | CREATE, SELECT, UPDATE, DELETE, INSERT, DROP TABLE                   |
| Content                                                                                  | CREATE TABLE, CREATE INDEX, INSERT, CREATE SCHEMA, CREATE TABLESPACE, ALTER TABLE, SELECT, INSERT, UPDATE TABLE, DROP TABLE, TEMP, REFERENCES                  | CREATE, SELECT, UPDATE, DELETE, INSERT, DROP TABLE                   |
| BPM document store                                                                       |                                                                                                                                                                | CREATE, SELECT, UPDATE, DELETE, INSERT, DROP TABLE                   |