<!-- image -->

# Module definition

An SCA module is not just another type of package. In IBM® Business Automation Workflow, an SCA service module is equivalent to a Java™ EE EAR file and several other Java EE submodules. Java EE elements,
such as a WAR file, can be packaged along with the SCA module.

Non-SCA artifacts (JSPs and others) can also be packaged together with an SCA service module.
These artifacts can then invoke SCA services through the SCA client programming model using a
special type of reference called a stand-alone reference.

```
<?xml version="1.0" encoding="UTF-8"?>
<scdl:module xmlns:scdl="http://www.ibm.com/xmlns/prod/websphere/scdl/8.5.0"
name="CreditApproval"/>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<scdl:module xmlns:mt="http://www.ibm.com/xmlns/prod/websphere/scdl/moduletype/8.5.0"    
  xmlns:scdl="http://www.ibm.com/xmlns/prod/websphere/scdl/8.5.0"name="StockQuote">   
  <mt:moduleType type="com.ibm.ws.sca.scdl.moduletype.mediation" version="1.0.0"/>
</scdl:module>
```