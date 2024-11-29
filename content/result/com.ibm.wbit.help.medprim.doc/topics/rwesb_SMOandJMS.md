# Accessing
JMS information in the SMO

## Introduction

If you invoke a mediation module
by sending a JMS message to an export with a JMS binding, you can
access and update the JMS message using mediation primitives. Most
mediation primitives let you navigate messages using XPath expressions.
If you implement your own custom mediation primitive, you can access
message information from Java™ code.

## XPath examples

```
/body
```

```
/headers/JMSHeader/JMSMessageID
```

```
/headers/properties[name='JMSXGroupID']
```

```
/headers/properties[name='MyProperty']
```