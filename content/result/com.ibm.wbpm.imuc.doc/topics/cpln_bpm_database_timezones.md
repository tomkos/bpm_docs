# Database time zone and character set considerations

## Time zone considerations

Timestamps that are stored in the database are based on the time zone that is configured for the
Business Automation Workflow server and database server. Because of
this dependency, you should not change the time zone configuration for the servers of an existing
setup if timers are already scheduled. If you change the time zone configuration of the servers, the
existing timers can trigger at an unexpected time.

If you
have a second database server for failover or disaster recovery reasons,
both database servers should be configured for the same time zone,
regardless of where they are physically located.

## Character set considerations for Oracle databases

- For the database character set (CHAR types), Business Automation Workflow requires AL32UTF8.
- For the national character set (NCHAR types), Business Automation Workflow requires UTF8 or
AL16UTF16. AL16UTF16 is recommended.

Note that the national character set required for Business Automation Workflow is different from the Oracle default value.

For a more detailed
description of the character set parameters, refer to the related
Oracle information.

## Related information

- Oracle Database Migration Assistant for Unicode