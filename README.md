# FileGO
FileGO is a Windows 10 system tray program that automatically moves files desirably.
<br>
<br>

<img src="Images/systrayshot.png" width=845 height=85>
<br>
<br>
<br>

## What is it?
Here is a quick video showing how to use it, further information down below:
<br>
<br>
[![DEMO](https://img.youtube.com/vi/NZZPcL75MHY/0.jpg)](https://www.youtube.com/watch?v=NZZPcL75MHY)

<br>
FileGO runs in the background and constantly checks for specific files in a specific folder, <br>
and then moves them to another folder you would like.
<br>
<br>

You can define:
* Suffixes: The suffixes of the files which FileGO should care about
* Track folder: The directory where FileGO checks for new files added to the folder, and if their suffixes matches the ones that are defined.
* Target folder: The directory where the files with the defined suffixes, within the dedicated folder, are transferred to.

<br>
<br>
<br>
<img src="Images/uishot.png" width=328 height=392>
<br>
<br>

In the above example, any new files added to "Desktop", that also have either one of the suffixes ".doc", ".pdf", or ".docx",
are automatically moved into the "School" folder.
<br>
<br>

<img src="Images/notification.png" width=214 height=69>
<br>
<br>

This is the notification received when a new file has been detected and transferred.
Keep in mind that FileGO can be kept running in the background as a system tray program.
<br>
<br>

## Usages of FileGO and Additional Information
FileGO can be use in many other efficient ways, including checking in the Downloads folder and moving specific files to specific locations.
I personally find it very useful to automatically detect mp4 files in Downloads and move them to a folder for videos, while keeping everything
else in the Downloads folder.
<br>
<br>

If you want, you may open multiple instances of FileGO at the same time for multiple tasks. However, be careful with it, since it is possible
that you would create an infinite loop of file transfer. In that case, shut the program down with Task Manager as soon as possible.
<br>
<br>

Also, the system tray icon might become irresponsive if too many files are detected at one instant.
<br>

This project is compelted by a highschooler, there may be some undiscovered bugs and unoptimized parts, so feedbacks are appreciated.
<br>
<br>

Enjoy file automation with FileGO!
