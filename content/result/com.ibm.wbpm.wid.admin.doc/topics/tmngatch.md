<!-- image -->

# Managing test configuration module attachments

## About this task

- Attaching the integration test client to test configuration modules

If you want to use the integration test client to test modules and their components but you do not want to use the invocation mechanism of the test client to perform your testing, you can attach the integration test client to the modules using a test configuration and then use a different invocation mechanism for testing your operations, such as JMS messages, web services, or JSPs.
- Synchronizing Attach events with test configurations

If you have attached the integration test client to a test configuration module and you later add another module to the test configuration, you will need to synchronize the Attach event with the test configuration to enable the integration test client to attach to the added test configuration module.
- Detaching the integration test client from test configuration modules

If you have attached the integration test client to a module, you can detach it from the module when you have finished your testing.