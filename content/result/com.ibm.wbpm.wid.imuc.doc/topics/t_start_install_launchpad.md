# Installing from the product launchpad

## Before you begin

1. Complete the preinstallation tasks described in Preparing to install.
2. Make sure that you meet all the requirements in  Detailed system requirements for a specific product.

## Procedure

To install from the launchpad program, complete the following steps. You can run only
one launchpad at a time.

1. Run launchpad64.exe from the root directory of the extracted files. To install
or run IBM
Integration Designer,
you must elevate your Microsoft Windows user account privileges. Whether you are an administrative
user or a non-administrative user, right-click launchpad64.exe and select
Run as administrator.
2. Select the typical installation environment that you want to install. 
Then, click
Next to continue.

Based on your selection, your next screen is configured to emphasize the features that you
need.
3. Specify the location for the installation. The default installation path is
C:\IBM\IID\IID.
4. Select the features within IBM Integration
Designer that
you would like to install. For more information, see Available features.
5. Click Next.
6 Specify information about the server environment. The required entries vary based on the typeof IBM IntegrationDesigner environment beinginstalled. IBM IntegrationDesigner environment Instructions IBM IntegrationDesigner with Workflow Server IBM IntegrationDesigner only Go to step 7 .

| IBM Integration Designer environment          | Instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBM Integration Designer with Workflow Server | Specify information for the Workflow Server test environment: Host name: This field shows the name of your computer. Location: Click Browse to change the installation location. The Workflow Server test environment will be installed into the specified directory. The default installation path is C:\IBM\IID\WORKFLOW.  User name and Password: Specify the user credentials for the cell administrative account and for the deployment environment account. The cell administrator is the primary WebSphere® Application Server administrator. A user that is assigned to this role can assign other administrator roles, and is responsible for the administration of the cell and topology. A user that is assigned to this role is not responsible for the administration of the IBM Integration Designer components. This role provides access to all interfaces, enabling users to alter or delete all types of available library items and assets, including process applications and toolkits. This role also enables administration of Workflow Server, Performance Data Warehouses, and internal users and groups. You must be a user assigned to this role to deploy process applications on the Workflow Center server. The deployment environment administrator is the primary IBM Integration Designer administrator. A user that is assigned to this role has administrative access to the Workflow Center and Process Admin Console. This role provides access to all interfaces, enabling users to alter or delete all types of available library items and assets, including process applications and toolkits. This account also enables administration of Workflow Server, Performance Data Warehouses, and internal users and groups.     Click Next to continue. |
| IBM Integration Designer only                 | Go to step 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

7. Specify the user name and password for the Db2 database connectivity, and then click
Next..
8. On the Installation summary page, verify the installation options
and read the license agreements. If you agree to the terms of the license agreements, select
 I have read and accepted the license agreement and notices.
9 To change the choices that you made on previous pages, click Back andmake your changes. When you are satisfied with your installation choices, click InstallSoftware to install the package. On the Installation information page, the followinginformation is displayed: A progress indicator shows the percentage of the installation completed.

- The products and features that you chose to install, and their installation locations
- The user credentials that you specified; to ensure that the passwords are not shown in clear
text, clear the Show passwords check box
- The Db2 databases that you created before the installation

## Results

You have installed a fully functional IBM Integration
Designer with a Workflow Server test environment, if selected.

## What to do next

- Available features

You can customize your software product by selecting the features of IBM Integration Designer to install.