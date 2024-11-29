<!-- image -->

# Working with targets

A component can call a component in another module to minimize
the time and cost of building an application. Targets provide additional
flexibility: to allow your installed applications to benefit from
advances in processing or other changes, you can use the administrative
console to change the endpoint of a cross-module invocation, without
rewriting or redeploying the application.

To take advantage of the flexibility provided, you must understand
how the system names the targets. The link from the calling module
must connect to the correct target.

## Target names

```
folder/export/fullpath\_to\_target/target\_component\_name
```

```
folder/calling\_component\_name/
full\_path\_to\_target\_component/target\_component\_name
```

- Changing import targets

Changing the target of a reference provides applications with the flexibility of taking advantage of advances in components as they happen without recompiling and reinstalling the application.