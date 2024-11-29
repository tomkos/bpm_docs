<!-- image -->

# Export definition

Export components include a name and a target attribute, which names the service component that
is to be exported. Like import components, exports have a binding attribute that indicates how the
service is bound externally.

```
<?xml version="1.0" encoding="UTF-8"?>
<scdl:export xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  	
     xmlns:\_="http://Resources/StockQuoteService/Binding" xmlns:ns1="http://Resources/StockQuoteService"  	
     xmlns:scdl="http://www.ibm.com/xmlns/prod/websphere/scdl/8.5.0"  	
     xmlns:webservice="http://www.ibm.com/xmlns/prod/websphere/scdl/webservice/8.5.0"  	
     Xmlns:wsdl="http://www.ibm.com/xmlns/prod/websphere/scdl/wsdl/8.5.0"  	
     displayName="StockQuoteService" name="StockQuoteService" target="StockQuote\_MediationFlow">
<interfaces>
  <interface xsi:type="wsdl:WSDLPortType" portType="ns1:StockQuoteService">       
    <method name="getQuote"/>     
  </interface>   
</interfaces>
```