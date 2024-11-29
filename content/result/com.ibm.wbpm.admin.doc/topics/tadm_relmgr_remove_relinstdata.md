<!-- image -->

# Using database tools to remove relationship instance data from
the repository

## Before you begin

## About this task

## Procedure

1. Locate the database. The database location depends
on the database platform.

Option
Description

Database platform
Location

Databases
The location is configured during installation and profile
creation of the server. For example, if you configured the server
automatically and selected the default database name, the name of
the database is WPRCSDB.
2 Delete the database artifacts making up a relationship: Using the tools for your database platform, perform the followingsteps to delete all database objects for a given relationship.
    1. Before removing any data from the database in the following
steps, make a backup of the database.
    2. Find the relationships tables. The following
tables are created at the time the relationships are installed.
Table
Format

1 table for relationship properties
\_<relname>\_P\_uniqueidentifier

1 table for role properties for each application-specific
role
\_<relname>\_<rolename>\_P\_uniqueidentifier

1 table for each application-specific role (for static relationships
1 table for the generic role is also created)
\_<relname>\_<rolename>\_RT\_uniqueidentifier

Restriction: Only the first four characters
of the relationship name are used. If the database holds tables for
multiple relationships, you should distinguish relationship names
within the first 4 characters.
    3. Find the stored procedures. Stored procedure
objects have the following format:\_<relname>\_RS\_uniqueidentifier or \_<relname>\_<rolename>\_RS\_uniqueidentifier
    4. Find the sequences. Sequence objects have
the following format:\_<relname>\_S\_uniqueidentifier
    5 Using the tools for your database platform, delete thefollowing:
        1. tables
        2. stored procedures
        3. sequences

## What to do next