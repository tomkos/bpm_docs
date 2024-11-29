<!-- image -->

# Installing applications associated with a stand-alone adapter

## Before you begin

1. Install the stand-alone adapter. Install the stand-alone adapter.
2. Create the necessary Java Naming and Directory Interface (JNDI) or Java Authentication and
Authorization Service (JAAS) resources.
3. Create an application EAR or snapshot to be used for deployment.

## About this task

A few more steps need to be taken when you deploy an application that includes references to a
stand-alone adapter.

## Procedure

1. Find the lib/ext folder of the installed deployment manager server in your
Advanced
deployment environment.
For example: install\_root/lib/ext
2. Copy the content from the adapter RAR file to the lib/ext folder.
For example, if your module uses a Flat Files adapter, open the CWYFF\_FlatFile folder
and copy the files.
3. Restart the deployment manager server to make the server class loader clear the cache and index
the added classes and schema from the lib/ext folder. For more information, see
Starting and stopping deployment managers.
4. Install the application to the target server or cluster. For more information, see
Deploying the module in the documentation for your adapter.
5. After you install the module to the target server or cluster, remove all the content that you
added to the lib/ext folder to avoid duplicate entry issues at run time; also,
removing this content avoids problems updating the adapter that might occur later.
6. Optional: 
Restart the deployment manager to clear the removed files from memory. For more information,
see Starting and stopping deployment managers.
7. Deploying the adapter binding involves tasks that occur on the deployment manager after the EAR
file is installed. Review the SystemOut.log file to confirm that no exceptions
are found.
8. Complete runtime customization that the deployed adapter configuration objects require. For
more information, see the Administering the adapter module section for your
specific adapter.

## Results

The application is deployed with the required adapter binding resources.