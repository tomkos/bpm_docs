# Disaster recovery

Business continuity is an overall plan to keep all aspects of a business functioning in the midst
of disruptive events. Disaster recovery is a subset of business continuity, focusing on the
technology systems that support business continuity.

Disaster recovery consists of well-defined strategies to back up the primary data center and
restore its data to a secondary data center.

- During normal operations, organizations use a live system. The backup programs run in the
background to save environmental information and application data.
- When the live system goes down, the backup system is restored from the backed-up data.

The topics in the following section provide information about the supported scenarios and
configuration for disaster recovery in a production environment that includes IBM® Business Automation
Workflow.

- Disaster recovery concepts

When you are planning for disaster recovery, consider the topology of the production environment, the types of data, the scope of the recovery, and the plans for data consistency.
- Backing up data

A backup system for disaster recovery is a copy of the production environment. The goal of any disaster recovery system is to create a mirror image of the data from the primary data center in a secondary data center. There are several ways to manage a backup system. Each method imposes some constraints on the production environment, and each presents some advantages and disadvantages.
- Runtime logs in a database: Overview

Store transaction and compensation logs in a relational database to improve high availability support and disaster recovery processes.
- Disaster recovery strategies

Disaster recovery consists of well-defined strategies to back up the primary data center and restore its data to a secondary data center.
- Disaster recovery strategies with an external Content Platform Engine

Consider the characteristics in disaster recovery strategies with an external Content Platform Engine.