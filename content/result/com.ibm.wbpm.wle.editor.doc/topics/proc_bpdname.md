# Instance names in BPDs and processes

For example, when an instance flows from a parent BPD to a child linked BPD, the instance name
changes to reflect its child status. However, when the instance flows back to the parent BPD, the
instance name changes again to reflect the parent BPD:

```
Instance Name Test [BPD] (Parent):n
Instance Name Test [BPD] (Child):n
Instance Name Test [BPD] (Parent):n
```

By comparison, when an instance flows from a parent process to a child process, the instance name
remains the same when the instance flows to the child process and then returns to the parent
process:

```
Instance Name Test [Process] (Parent):n
Instance Name Test [Process] (Parent):n
Instance Name Test [Process] (Parent):n
```