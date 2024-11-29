<!-- image -->

# Application Response Measurement statistics for the Service Component Architecture

The Application Response Measurement (ARM) statistics shown in the following tables are - in a
simplified manner - time and count measurements of caller invocations to the Service Component
Architecture (SCA) layer, and the results returned from a service. There are, in fact, a number of
service invocation patterns that vary between synchronous and asynchronous implementations of
deferred responses, results retrievals, callbacks, and one-way invocations. All patterns, however,
are between the caller invocation and a service, the response from the service, or, in some cases, a
data source, with the SCA layer interposed in between.

- Arm40.ArmMetricFactory - the full Java
class name of your ARM implementation providers metrics factory.
- Arm40.ArmTranReportFactory - the full Java class name of your ARM implementation providers transaction report factory.
- Arm40.ArmTransactionFactory - the full Java class name of your ARM implementation providers transaction factory.

| Event type             | Element                                             |
|------------------------|-----------------------------------------------------|
| Business process       | Process                                             |
| Human task             | Task                                                |
| Business rule          | Operation                                           |
| Business state machine | Transition Guard Action EntryAction ExitAction      |
| Selector               | Operation                                           |
| Map                    | Map Transformation                                  |
| Mediation              | OperationBinding ParameterMediation                 |
| Resource adapter       | InboundEventRetrieval InboundEventDelivery Outbound |

| Statistic name       | Type    | Description                                                                                                                                                                                                                                                                                     |
|----------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GoodRequests         | Counter | Number of server invocations not raising exceptions.                                                                                                                                                                                                                                            |
| BadRequests          | Counter | Number of server invocations raising exceptions.                                                                                                                                                                                                                                                |
| ResponseTime         | Timer   | Duration measured on the server side between the reception of a request and computing the result.                                                                                                                                                                                               |
| TotalResponseTime    | Timer   | Duration measured on the caller side, from the time a caller requests a service to the time when the result is available for the caller. Does not include the processing of the result by the caller.                                                                                           |
| RequestDeliveryTime  | Timer   | Duration measured on the caller side, from the time a caller requests a service to the time when the request is handed over to the implementation on the server side. In a distributed environment, the quality of this measurement depends on the quality of synchronization of system clocks. |
| ResponseDeliveryTime | Timer   | The time required to make the result available to the client. For a deferred response, this time does not include the result retrieve time. In a distributed environment, the quality of this measurement depends on the quality of synchronization of system clocks.                           |

| Statistic name             | Type    | Description                                                                                                                                                             |
|----------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GoodRefRequests            | Counter | Number of caller invocations to the SCA layer that do not raise exceptions.                                                                                             |
| BadRefRequests             | Counter | Number of caller invocations to the SCA layer that do raise exceptions.                                                                                                 |
| RefResponseTime            | Timer   | Duration measured on the caller side, from the time the caller makes a request to the SCA layer and the time when the results of that call are returned to the caller.  |
| BadRetrieveResult          | Counter | Number of caller invocations to a data source that do raise exceptions.                                                                                                 |
| GoodRetrieveResult         | Counter | Number of caller invocations to a data source that do not raise exceptions.                                                                                             |
| RetrieveResultResponseTime | Timer   | Duration measured on the caller side, from the time the caller makes a request to the data source and the time when the data source response is returned to the caller. |
| RetrieveResultWaitTime     | Timer   | Duration measured on the caller side if a timeout occurs.                                                                                                               |

| Statistic name   | Type    | Description                                                                                                                                                      |
|------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GoodTargetSubmit | Counter | Number of SCA invocations to the service that do not raise exceptions.                                                                                           |
| BadTargetSubmit  | Counter | Number of SCA invocations to the service that do raise exceptions.                                                                                               |
| TargetSubmitTime | Timer   | Duration measured on the server side, from the time the SCA makes a request to the service and the time when the results of that call are returned to the SCA.   |
| GoodResultSubmit | Counter | Number of service invocations to the data source that do not raise exceptions.                                                                                   |
| BadResultSubmit  | Counter | Number of service invocations to the data source that do raise exceptions.                                                                                       |
| ResultSubmitTime | Timer   | Duration measured on the server side, from the time the service makes a request to the data source and the time when the results of are returned to the service. |

| Statistic name   | Type    | Description                                                                                                                                     |
|------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| GoodCB           | Counter | Number of SCA invocations to the callback that do not raise exceptions.                                                                         |
| BadCB            | Counter | Number of SCA invocations to the callback that do raise exceptions.                                                                             |
| CBTime           | Timer   | Duration from the time the SCA makes a request to the callback, and the time when the results from the callback are returned to the SCA.        |
| GoodCBSubmit     | Counter | Number of invocations from the service to the SCA handling the callback that do not raise exceptions.                                           |
| BadCBSubmit      | Counter | Number of invocations from the service to the SCA handling the callback that do raise exceptions.                                               |
| CBSubmitTime     | Timer   | Duration from the time the service makes a request to the SCA handling the callback, and the time when the results from the SCA to the service. |

- Synchronous invocations

You can obtain Application Response Measurement (ARM) performance statistics from a simple Service Component Architecture (SCA) call to a service and the response from the service.
- Deferred response with synchronous implementation

You can obtain Application Response Measurement (ARM) statistics with a synchronous invocation of the request. The returned result is sent as output to a data store for a synchronous implementation.
- Deferred response with asynchronous implementation

You can obtain Application Response Measurement (ARM) statistics from an asynchronous implementation. The call to the service and the return result are invoked but the resulting output is sent to a data store from the service target.
- Deferred response with asynchronous result retrieve

The ResultRetrieve Application Response Measurement (ARM) statistic can be correlated to some original request using the ARM transactions only if XPARENT-1 and XPARENT-2 have a common ancestor transaction. The invocation of request, and result retrieve occur on different threads
- Asynchronous callback with synchronous implementation

You can obtain Application Response Measurement (ARM) statistics when callback requests and callback executions use different threads on a synchronous implementation.
- Asynchronous callback with asynchronous implementation

Application Response Measurement (ARM) statistics are available for callback requests and callback executions using different threads with an asynchronous implementation.
- Asynchronous one way with synchronous implementation

These Application Response Measurement (ARM) statistics can be obtained when a call is submitted (fire and forget) with a synchronous implementation.
- Asynchronous one way with asynchronous implementation

Application Response Measurement (ARM) statistics when a call is submitted (fire and forget) with an asynchronous implementation.