# Customizing the login page for Process Portal

## About this task

## Procedure

1 Export the Process Portal application:
    1. Start the administrative console and go to Applications > Application Types > WebSphere enterprise applications.
    2. Select the Process Portal application
(IBM BPM Responsive Portal), click Export,
and save the EAR file to an empty directory.
2 Update the login page files in the Process Portal EARfile with your logo information:

1. In your file explorer, go to the directory that contains
the exported EAR file and extract the files. The
extracted files include the responsivePortal.war file,
which includes the login.jsp file and the logo
graphic file.
2. Extract the files in the responsivePortal.war file
to a new directory.
3. In the new directory, open the login.jsp file
in a text editor, and change the src attribute to
point to your company logo: <img class="ibm-logo" src="img/ibm-logo.png" alt="" />
For example, if the mycorp.png file
is the graphic file for your logo, the code looks as follows:<img class="ibm-logo" src="img/mycorp.png" alt="" />
4. Add your graphic file to the img directory.
5. Compress the files in the responsivePortal.war directory.
6. Replace the responsivePortal.war file
in the exported Process Portal EAR
file with your updated file.
3 Replace the deployed Process Portal applicationwith your updated version:

1. In the administrative console, go to Applications > Application Types > WebSphere enterprise applications.
2. Select the Process Portal application
and click Update.
3. From the update options, select Replace the
entire application, and enter the fully qualified path
of the updated EAR file.
4. Click Next and follow the steps
to update the Process Portal application.

## Results