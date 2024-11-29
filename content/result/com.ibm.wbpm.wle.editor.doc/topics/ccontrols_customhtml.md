# Custom HTML

- CoachView
- ContentBox

The custom HTML item supports the use of JavaScript variables for
simple types. When the server generates the HTML page for the client,
it replaces the variable name with its value. However, after the server
generates the page, it does not update the HTML if there is a change
in the value. The server updates the variable only when it regenerates
the entire HTML page. If the server cannot resolve the variable, users
see the variable name instead of its value.

```
<div>Hello, {{tw.local.user.name}}.</div>
```

```
{{tw.businessData.address.street}}
```