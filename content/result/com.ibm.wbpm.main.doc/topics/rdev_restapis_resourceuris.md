# Resource URIs for BPD and BPEL   resources

```
http://{host}:{port}/rest/{component}/v1/{resource}?{query}
```

| REST API                                         | Context root                             |
|--------------------------------------------------|------------------------------------------|
| BPD-related REST APIs                            | /bpm/wle/                                |
| BPEL-related REST APIs                           | /bpm/bfm/  /bpm/htm/                     |
| IBM® Process Federation Server REST APIs         | /bpm/federated/                          |
| Repository REST APIs                             | /bpm/repo/                               |
| Federated Business Automation Workflow REST APIs | /bpm/federated/bfm/  /bpm/federated/htm/ |
| Business calendar REST APIs                      | /bpm/businesscalendar/                   |

- Support for new MIME types or resource representations.
- The addition of new properties to existing JSON objects that are
returned to a client. These properties are ignored by clients that
are not at the latest level.