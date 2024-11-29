# Installing, configuring, and administering IBM Business Automation
Machine Learning Server

Intelligent Task Prioritization uses
historic runtime data to provide a prioritized task list for the user, improving workforce
efficiency and maximizing throughput. Tasks are assigned to a user based on their task expertise and
the predicted value from processing time predictions. Task experts are determined by using a
self-supervised classification neural network that predicts the likelihood of whether a worker will
complete a task faster than the workforce average. Processing time is determined by using a
regressive neural network that predicts how long it takes a worker to complete a task in seconds.
These models are hosted in Machine Learning Server.

- Installing IBM Business Automation Machine Learning Server

Machine Learning Server runs only on Linux.
- Configuring Business Automation Workflow to use IBM Business Automation Machine Learning Server

Before you can use Machine Learning Server services, you must configure Business Automation Workflow to be able to use Machine Learning Server.
- Changing the IBM Business Automation Machine Learning Server configuration

You can change the environment variables used in the docker-compose.yml file by updating the values of the corresponding variables in the .env file.
- Regenerating certificates for IBM Business Automation Machine Learning Server

You might need to regenerate the certificates used by the Machine Learning Server. The certificates for the services are in the ba-ml-server\_install\_dir/certs directory.
- Using custom certificates for IBM Business Automation Machine Learning Server

To use your custom certificates, keystores, or truststores for all Machine Learning Server secured components, stop the services, replace the certificates, and restart the services.
- Administering IBM Business Automation Machine Learning Server

Commands are available for administering Machine Learning Server.
- Uninstalling IBM Business Automation Machine Learning Server

To uninstall Machine Learning Server, remove the installation directory and the Docker images.
- Troubleshooting the IBM Business Automation Machine Learning Server

Use the information to identify and resolve problems that can occur while you are using the Machine Learning Server.