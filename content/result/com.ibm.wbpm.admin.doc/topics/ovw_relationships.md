<!-- image -->

# Managing relationships

- The relationship service

The relationship service maintains relationships and roles in the system. It manages relationship and role definitions and metadata and makes it possible to specify the definition of a relationship and manipulate the instances derived from the definition.
- The relationship manager

The relationship manager is a tool for manually controlling and manipulating relationship data to correct errors found in automated relationship management or provide more complete relationship information. In particular, it provides a facility for retrieving and modifying relationship instance data.
- Querying relationship data

If you want to query relationship data, you can use the relationship manager or views in a database.
- Managing relationship instances

Managing relationship instances can include tasks like viewing and editing instances, exporting and importing instances, creating and deleting instances, and rolling back instance data.
- Managing role instances

Managing role instances can include tasks like viewing instances, editing instance properties, and creating or deleting instances.
- Removing relationship instance data from the repository

An application that uses relationships has associated relationship schema and data in a repository. The repository is the database configured to hold the relationship instance data. When you uninstall such an application from a production server, the server does not remove the relationship schema and data from the repository. You must remove the existing relationship schema manually. When you uninstall such an application from a developing server, the schema and data are removed from the repository on every application stop or start process.
- Tutorial: Relationship manager administration

The relationship manager can be used to add, modify, and remove instances of relationships, which correlate identifiers from different environments for the same item of data. This tutorial demonstrates the basic functions of the relationship manager.