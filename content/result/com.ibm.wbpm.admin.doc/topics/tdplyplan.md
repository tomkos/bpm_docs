<!-- image -->

# Planning to deploy your applications that have adapters

## About this task

Each adapter has distinct planning requirements but share the following common
considerations.

- User authentication

An adapter provides a user name and a password in one of two ways. Understanding the features and limitations of each method can help you decide which option is best for your circumstance.
- Module deployment with the adapter or separately

Before you deploy your application, you must consider the deployment options: you can embed your adapter with the module or you can deploy the adapter as a stand-alone RAR file.
- Deployment that uses several versions of the adapter

When you deploy several versions of the adapter, whether as an embedded or stand-alone deployment, errors often occur.
- More deployment factors

Several more factors affect deploying applications with an adapter.
- Connection properties specified on a server or at design time

An application that uses an adapter binding needs connection properties. If you use a stand-alone adapter, a system administrator can specify connection properties. If you use an embedded adapter, connection properties are set up when the application is designed and developed.