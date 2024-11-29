# Accessing WebSphere MQ header information in the SMO

## Introduction

You can access and update the content
in the WebSphere MQ
header structures using mediation primitives. Most mediation primitives let
you navigate messages using XPath expressions. If you do this, you must make
sure that the XPath identifies the particular header that the primitive is
interested in. If you implement your own custom mediation primitive, you can
access message information from Java™ code.

## XPath examples

```
/headers/MQHeader/header/rfh2/folder[name="usr"]/property[name="prop"]/value
```

```
/headers/MQHeader/header[format="MYHDR"]/value/mydata
```

```
/headers/MQHeader/header[2]/value/mydata
```