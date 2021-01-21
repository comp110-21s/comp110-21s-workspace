# COMP110 Workspace - Spring 2021

Your work in the course will be completed in this workspace. Instructions for the two most common tasks you'll perform can be found below.

## Backup Your Work

"Push" your work up to GitHub for backup. By creating "commits", which you can think of as versioned checkpoints in your workspace, you are not at risk of losing your work. It's easy to revert back to an old version or to restore your entire workspace on a different computer.

1. Select the _View_ menu and then _SCM_ (Source Control Management)
   - Alternatively: Select the Activity Bar icon that's three circles with lines for Source Control
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word changes and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see these listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed.
5. Open the _View_ menu and select _Command Palette_, the shortcut for this menu is:
   - Windows: `Control+Shift+P`
   - Mac: `Command+Shift+P`
6. Begin typing in: `Git: Push to...` and press `Enter` once it is the first option.
7. Select the `backup` remote that is your personal workspace on GitHub. If you do not see `backup` listed, see the instructions below on _Setup Backup Course Material Repository_.
   - You may see a spinning "refresh" icon in your status bar at the bottom of VSCode. Unless an error backing up occurs, you will not see any confirmation.
   - If you want to see your backed up work on Github, navigate to the following URL but replace `USERNAME` with your GitHub username:
   - `https://github.com/comp110-21s/comp110-workspace-21s-USERNAME`

## Download New Course Material

"Pulling" course materials down from Upstream. As new lesson material or starter code for exercises and projects is added to our central course repository, these are the steps you'll take to download them into your own workspace repository.

1. Open the _View_ menu and select _Command Palette_ 
   - The shortcut for this menu is:
   - Windows: `Control+Shift+P`
   - Mac: `Command+Shift+P`
2. Begin typing in `Git: Pull From...` and press `Enter` once it is the first option. 
3. Begin typing in `origin` and press `Enter` once it is the first option.
   - If you do not see "upstream" as an option, follow the "Setup Upstream" instructions below.
4. Press enter with `origin/master` as the first option.
5. This downloads the latest course materials! It will succeed silently, so if nothing appears to happen it worked (and any new files will be available in the file explorer). If there was an error, you would see an error message pop up.

## Setup Backup Course Material Repository

When you are first setting up your personal workspace repository, you will need to follow these instructions to connect the repository on your computer with your personal "backup" course repository on GitHub. As we add new material through the course, you will then be able to easily back it up to your backup repo.

1. Navigate a web browser to <https://classroom.github.com/a/vjk6Jd9d>
2. Join the Classroom by selecting your ONYEN (Clicking "Skip to the next step" is also OK)
3. Click "Accept this Assignment"
4. When the workspace is getting setup you may need to refresh until it tells you you're ready to go!
5. Click the link to your personal backup repository that looks something like this `https://github.com/comp110-21s/comp110-workspace-21s-KrisJordan` (except instead of `KrisJordan` you will see your GitHub username).
6. Toward the top of the page it will say "Quick setup" and you will see two buttons: HTTPS and SSH. Click HTTPS and copy the text of the URL in the box to the right of the buttons (or click the clipboard icon)
7. With your workspace open in VSCode, type in _Git: Add Remote_ and press enter with the option selected.
10. In the blank text box that appears, paste in the URL to your backup repository that you just copied. Press enter.
11. When asked for "Remote name" type in: `backup`
12. Follow the steps in the section above on how to "Backup your work."
