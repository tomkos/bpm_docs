# Adding a custom logo to Process Portal

## About this task

## Procedure

1. Create a toolkit for the customization files. You
can create a toolkit by using either Workflow Center or
the desktop Process Designer.
In this example, the toolkit is called SDBToolkit and
the acronym is SDBTK.
2. Create the header and graphic files. The
example uses the following header file:<html xmlns="http://www.w3.org/1999/xhtml>
<head>
<style>
   .customLogo {
       background-color: #325c80;
       height:55px;
   }
</style>
       <script type="text/javascript">
           var customLogoURL = com\_ibm\_bpm\_coach.getManagedAssetUrl("speedDemonBikes.png", com\_ibm\_bpm\_coach.assetType\_WEB, "SDBTK");
           window.onload = function() {
              document.getElementById("customLogoImg").src = customLogoURL;
              console.log("!!");
           };
       </script>
</head>
       <div class="customLogo" role="main">
           <div>
               <img id="customLogoImg" src="" alt="" />
       </div>
</html>The URL in the header file is used to retrieve
the logo from the toolkit.
3 Add the files to the toolkit:
    1. Open the new toolkit in Process Designer.
    2. In the library, click the + sign
next to Files, then select Web File,
and add the header and graphic files.
    3. In Workflow Center, create
a snapshot of the new toolkit.
4 Add a dependency to Process Portal forthe new toolkit.

1. In Process Designer, open
the Process Portal process
application.
2. In the library, click the + sign
next to Toolkits, then select the new toolkit.
5 Add the logo to the appropriate Process Portal client-sidehuman service. In this example, the company logo is added to the user profile, which is a view in theRESPONSIVE\_PORTAL client-side human service.

In this example, the company logo is added to the user profile, which is a view in the
RESPONSIVE\_PORTAL client-side human service.

1. On the Overview tab for the Process Portal process
application, click the RESPONSIVE\_PORTAL client-side
human service.
2. On the Coaches tab, click Portal
to display the views, and then double-click anywhere in the views pane.
3. From the Advanced section of the palette, add a Custom
HTML view to the views pane, over the User Profile view.

Tip: To ensure that the logo appears on the view and not next to it, drop the
Custom HTML view onto the User Profile view and not outside it.
4 Configure the Custom HTML control to refer to the headerfile:
    1. Select the control, and in the Properties section HTML tab, select Managed
File.
    2. From the list of files, select the header file that contains the
link to the graphic file.
6. Save your changes.

## Results