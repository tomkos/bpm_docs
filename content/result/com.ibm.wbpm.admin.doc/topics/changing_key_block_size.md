# Changing the block size allocation for primary keys

## About this task

The <pri-key-block-size> setting
is used for all database tables where Business Automation Workflow creates
the primary key. If a cluster contains multiple Business Automation Workflow servers,
all servers access the same database. If each server created primary
keys independently, there would often be conflicts because two or
more servers would create the same primary key. To avoid these conflicts,
each server uses the database table LSW\_PRI\_KEY to assign new primary
keys. It would be too resource-intensive to update this table for
each new key. Instead, each server allocates a range of values for
the new keys by updating the LSW\_PRI\_KEY table (which retains the
high key value for each entity type). After the server has used all
the values from the range, it allocates a new range through access
to the database. The default value for this range is 50,
but the value can be modified using the <pri-key-block-size> configuration
setting.

## Procedure

To change the block size allocation for a primary key:

1. In the appropriate 100Custom.xml files
(see the topic Location of 100Custom configuration files for
their location), specify the block size allocation for the primary
key by using the following format: <properties>
   <server>
      <pri-key-block-size merge="replace">200</pri-key-block-size>
   </server>
</properties>
2. Restart the server.