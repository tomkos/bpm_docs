<!-- image -->

# Test environment

As an IBM Integration
Designer developer,
how you set up a remote environment depends on your target deployment
environment.

## Workflow Server

In
an IBM Integration
Designer unit
test environment, the server can be installed locally or on a remote
machine. When Workflow Server is
installed locally, IBM Integration
Designer finds
it and displays it in the Servers view.

By default, the Workflow Server name
in the Servers view contains the version of the server. If you update
the server, the name in the Servers view will not be updated. However,
you can edit the server name and either change or remove the version.

When Workflow Server is
installed remotely, you can target it from IBM Integration
Designer by
creating a new server.

1. In the Servers view, right-click and select New > Server.
2. Select IBM > Workflow Server.
3. Specify the remote server host name and click Next.
4. Specify the profile name, connection, and security information, and click
Finish.

## Workflow Server via Workflow Center

1. In the Workflow Center,
select Window > Preferences.
2. Select Business Integration > Workflow Center.
3. Specify the Workflow Center URI,
user name, and password.
4. Click Test Connection. If everything is
correct, click OK.

Learn about the Workflow Center by reading The Workflow Center repository. If you experience communication problems with the remote server, such
as problems in publishing to the remote server or obtaining the status of the server, see Resolving communication problems with remote servers.

## Installing to a unique package group

1. Start Installation Manager.
2. Click File > Preferences, and then click Repositories.
3 In the Repositories window, use the AddRepository button to specify the following repositorylocations for IBM IntegrationDesigner andfor Installation Manager : where image\_directory is the root directoryof the DVD or the extracted installation image, and os\_bit denotesyour operating system and bit version (for example, win64 ). Click OK eachtime to add the repository and close the Add Repository window.
    - image\_directory\disk1\diskTag.inf
    - image\_directory\disk1\IM\_os\_bit\repository.config

where image\_directory is the root directory
of the DVD or the extracted installation image, and os\_bit denotes
your operating system and bit version (for example, win64).

Click OK each
time to add the repository and close the Add Repository window.

4. Click OK to close the Preferences window.
5. From the Installation Manager window,
click Install and then follow the installation
prompts.Note: When you get to the Location page, Installation Manager displays
the choice of whether to install into a new package group or into
the existing supported Rational Application
Developer package
group. A package group is a directory that contains resources that
packages share with other packages in the same group. To install IBM Integration
Designer into
the directory that contains the existing Rational Application
Developer installation,
choose Use the existing package group. The Installation
Directory field identifies where Rational Application
Developer is installed.