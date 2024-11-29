# Enabling Case Analyzer to
update completed cases

## Procedure

To enable Case Analyzer to process the updates:

1. Stop Content Platform Engine.
2 Run the following database commands on the Case Analyzer store database: UPDATE <CASCHEMA>.X\_CAProperties SET PropValue='true' WHERE PropName = analyzer.processEventsAfterCaseClosed'; UPDATE <CASCHEMA>.X\_CAProperties SET PropValue='BATCH' WHERE PropName ='analyzer.db.updateMode’;

```
UPDATE <CASCHEMA>.X\_CAProperties SET PropValue='true' WHERE PropName = analyzer.processEventsAfterCaseClosed';
```

```
UPDATE <CASCHEMA>.X\_CAProperties SET PropValue='BATCH' WHERE PropName ='analyzer.db.updateMode’;
```

    - For Db2, Oracle and PostgreSQL, the value of analyzer.db.updateMode property
is ‘BATCH’.
    - For Microsoft SQL server, you need to update the
value.
3. Restart Content Platform Engine.