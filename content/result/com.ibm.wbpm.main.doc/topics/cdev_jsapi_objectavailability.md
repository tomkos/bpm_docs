# Variable availability

| Object       | Context Allowed   | Context Instantiated      | Context Denied   |
|--------------|-------------------|---------------------------|------------------|
| TWLogger     | All               | None                      | None             |
| TW           | Process           | Process                   | ScoreBoard       |
| TWScoreboard | ScoreBoard        | ScoreBoard                | Process, Service |
| Chart        | ScoreBoard        | Filter Layout, Datasource | None             |
| TWDate       | All               | None                      | None             |
| TWMap        | All               | None                      | None             |
| String       | All               | None                      | None             |
| XMLDocument  | All               | None                      | None             |
| XMLElement   | All               | None                      | None             |
| XMLNodelist  | All               | None                      | None             |
| listOf       | All               | None                      | None             |
| ic           | All               | None                      | None             |
| Alert        | All               | None                      | None             |
| Event        | All               | None                      | None             |