<!-- image -->

# Example of an XML output file

The output file you will see after
running your script is shown below.

```
<?xml version="1.0" encoding="UTF-8"?>
<resource name="OrderTest">
   <testsuite end="1213022103171" name="OrderFVT" start="1213022101062"
   	totalTests="7">
   	<testcase end="1213022101750" name="test\_checkAvailability"
     result="fail" start="1213022101093">
         <variation end="1213022101703" name="Passed" start="1213022101093">
            <severity>pass</severity>
            <description>Passed pass</description>
            <resource>OrderTest</resource>
         </variation>
         <variation end="1213022101750" name="Failed"
            start="1213022101703">
            <severity>fail</severity>
            <description>
               junit.framework.AssertionFailedError:
               Variation:[Failed] Variable:[quantity] FAIL(
               Input:[39] Not\_EQ Expected:[29] )&#13; 
               at junit.framework.Assert.fail(Assert.java:47)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.datatable.AbstractOutputDataEntry.fail(Unknown Source)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.datatable.AbstractOutputDataEntry.processAssertEvent(Unknown Source)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.datatable.AbstractOutputDataEntry.assertValue(Unknown Source)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.datatable.AbstractOutputDataEntry.setVariableValueAndAssert(Unknown Source)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.datatable.DataSet.setOutputVariableValueAndAssert(Unknown Source)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.junit.TestCaseDelegate.setOutputVariableValueAndAssert(Unknown Source)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.junit.DataDrivenTestCase.setOutputVariableValueAndAssert(Unknown Source)&#13; 
               at test.OrderFVT.test\_checkAvailability(OrderFVT.java:74)&#13;
               at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)&#13; 
               at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:79)&#13;
               at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)&#13;
               at java.lang.reflect.Method.invoke(Method.java:618)&#13;
               at com.ibm.ccl.soa.test.ct.runtime.junit.TestCaseDelegate.runTest(Unknown Source)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.junit.TestCaseDelegate.runBare(Unknown Source)&#13; 
               at com.ibm.ccl.soa.test.ct.runtime.junit.DataDrivenTestCase.runBare(Unknown Source)&#13; 
               at junit.framework.TestResult$1.protect(TestResult.java:106)&#13;
               at junit.framework.TestResult.runProtected(TestResult.java:124)&#13;
               at junit.framework.TestResult.run(TestResult.java:109)&#13;
               at junit.framework.TestCase.run(TestCase.java:118)&#13;
               at com.ibm.wbit.comptest.ct.runtime.runner.CTJUnitRunner.test(Unknown Source)&#13; 
               at com.ibm.wbit.comptest.ct.servlet.TestServlet.invokeTestBean(Unknown Source)&#13; 
               at com.ibm.wbit.comptest.ct.servlet.TestServlet.doPost(Unknown Source)&#13; 
               at com.ibm.wbit.comptest.ct.servlet.TestServlet.doGet(Unknown Source)&#13; 
               at javax.servlet.http.HttpServlet.service(HttpServlet.java:743)&#13;
               at javax.servlet.http.HttpServlet.service(HttpServlet.java:856)&#13;
               at com.ibm.ws.webcontainer.servlet.ServletWrapper.service(ServletWrapper.java:1081)&#13;
               at com.ibm.ws.webcontainer.servlet.ServletWrapper.handleRequest(ServletWrapper.java:550)&#13;
               at com.ibm.ws.wswebcontainer.servlet.ServletWrapper.handleRequest(ServletWrapper.java:478)&#13;
               at com.ibm.ws.webcontainer.webapp.WebApp.handleRequest(WebApp.java:3391)&#13;
               at com.ibm.ws.webcontainer.webapp.WebGroup.handleRequest(WebGroup.java:267)&#13;
               at com.ibm.ws.webcontainer.WebContainer.handleRequest(WebContainer.java:811)&#13;
               at com.ibm.ws.wswebcontainer.WebContainer.handleRequest(WebContainer.java:1455)&#13;
               at com.ibm.ws.webcontainer.channel.WCChannelLink.ready(WCChannelLink.java:115)&#13;
               at com.ibm.ws.http.channel.inbound.impl.HttpInboundLink.handleDiscrimination(HttpInboundLink.java:458)&#13;
               at com.ibm.ws.http.channel.inbound.impl.HttpInboundLink.handleNewInformation(HttpInboundLink.java:387)&#13;
               at com.ibm.ws.http.channel.inbound.impl.HttpInboundLink.ready(HttpInboundLink.java:267)&#13;
               at com.ibm.ws.tcp.channel.impl.NewConnectionInitialReadCallback.sendToDiscriminators(NewConnectionInitialReadCallback.java:214)&#13;
               at com.ibm.ws.tcp.channel.impl.NewConnectionInitialReadCallback.complete(NewConnectionInitialReadCallback.java:113)&#13;
               at com.ibm.ws.tcp.channel.impl.AioReadCompletionListener.futureCompleted(AioReadCompletionListener.java:165)&#13;
               at com.ibm.io.async.AbstractAsyncFuture.invokeCallback(AbstractAsyncFuture.java:217)&#13;
               at com.ibm.io.async.AsyncChannelFuture.fireCompletionActions(AsyncChannelFuture.java:161)&#13;
               at com.ibm.io.async.AsyncFuture.completed(AsyncFuture.java:136)&#13;
               at com.ibm.io.async.ResultHandler.complete(ResultHandler.java:195)&#13;
               at com.ibm.io.async.ResultHandler.runEventProcessingLoop(ResultHandler.java:743)&#13;
               at com.ibm.io.async.ResultHandler$2.run(ResultHandler.java:873)&#13;
               at com.ibm.ws.util.ThreadPool$Worker.run(ThreadPool.java:1473)&#13;
            </description>
            <resource>OrderTest</resource>
         </variation>
      </testcase>
      <testcase end="1213022101828" name="test\_checkPurchaseOrder"
         result="fail" start="1213022101750">
         <variation end="1213022101781" name="Passed"
            start="1213022101750">
            <severity>pass</severity>
            <description>Passed pass</description>
            <resource>OrderTest</resource>
         </variation>
         <variation end="1213022101828" name="Failed"
            start="1213022101781">
            <severity>fail</severity>
            <description>
               junit.framework.AssertionFailedError:
               Variation:[Failed] Variable:[valid] FAIL(
               Input:[true] Not\_NEQ Expected:[true] )&#13; 
               ...
            </description>
            <resource>OrderTest</resource>
         </variation>
      </testcase>
      <testcase end="1213022102281" name="test\_takeOrder"
         result="fail" start="1213022101828">
         <variation end="1213022102140" name="Passed"
            start="1213022101828">
            <severity>pass</severity>
            <description>Passed pass</description>
            <resource>OrderTest</resource>
         </variation>
         <variation end="1213022102281" name="Failed"
            start="1213022102140">
            <severity>fail</severity>
            <description>
               junit.framework.AssertionFailedError:
               Variation:[Failed] Variable:[Item\_2] Path:[id] FAIL(
               Input:[rpc3453] Not\_EQ Expected:[bpc3453] )&#13; 
               ...
            </description>
            <resource>OrderTest</resource>
         </variation>
      </testcase>
      <testcase end="1213022102734" name="test\_components"
         result="pass" start="1213022102281">
         <variation end="1213022102500" name="Passed"
            start="1213022102281">
            <severity>pass</severity>
            <description>Passed pass</description>
            <resource>OrderTest</resource>
         </variation>
         <variation end="1213022102734" name="Failed"
            start="1213022102500">
            <severity>pass</severity>
            <description>Failed pass</description>
            <resource>OrderTest</resource>
         </variation>
      </testcase>
      <testcase end="1213022103000" name="test\_flowData"
         result="error" start="1213022102734">
         <variation end="1213022103000" name="Passes"
            start="1213022102734">
            <severity>fail</severity>
            <description>
               com.ibm.wbit.comptest.ct.service.CTRuntimeException:
               com.ibm.websphere.sca.ServiceRuntimeException: Fail
               to invoke [sca.component.java.impl.CheckAvailabilityImpl.public java.math.BigInteger 
               sca.component.java.impl.CheckAvailabilityImpl.checkAvailability(commonj.sdo.DataObject)
               throws com.ibm.websphere.sca.ServiceBusinessException] for
               component [{OrderEntry}CheckAvailability]: caused by: java.lang.NullPointerException&#13; 
               at com.ibm.wbit.comptest.ct.runtime.service.CTServiceProxy.doInvoke(Unknown Source)&#13; 
               ....
            </description>
            <resource>OrderTest</resource>
         </variation>
      </testcase>
      <testcase end="1213022103093" name="test\_async" result="fail"
         start="1213022103000">
         <variation end="1213022103046" name="Passed"
            start="1213022103000">
            <severity>pass</severity>
            <description>Passed pass</description>
            <resource>OrderTest</resource>
         </variation>
         <variation end="1213022103093" name="Failed"
            start="1213022103046">
            <severity>fail</severity>
            <description>
               junit.framework.AssertionFailedError:
               Variation:[Failed] Variable:[quantity] FAIL(
               Input:[29] Not\_GT Expected:[29] )&#13; 
               ...
            </description>
            <resource>OrderTest</resource>
         </variation>
      </testcase>
      <testcase end="1213022103171" name="test\_error" result="pass"
         start="1213022103093">
         <variation end="1213022103171" name="Default"
            start="1213022103093">
            <severity>pass</severity>
            <description>Default pass</description>
            <resource>OrderTest</resource>
         </variation>
      </testcase>
   </testsuite>
</resource>
```