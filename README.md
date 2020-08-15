# COMP110 Workspace - Fall 2020

Your work in the course will be completed in this workspace. Instructions for the two most common tasks you'll perform can be found below.

## Backup Your Work

"Push" your work up to GitHub for backup. By creating "commits", which you can think of as versioned checkpoints in your workspace, you are not at risk of losing your work. It's easy to revert back to an old version or to restore your entire workspace on a different computer.

1. Select the _View_ menu and then _SCM_ (Source Control Management)
   - Alternatively: Select the Activity Bar icon that's three circles with lines for Source Control
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word changes and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see these listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...) and select "Push" to send this backed up version to your workspace repository space on GitHub.

## Download New Course Material

"Pulling" course materials down from Upstream. As new lesson material or starter code for exercises and projects is added to our central course repository, these are the steps you'll take to download them into your own workspace repository.

1. Open the _View_ menu and select _Command Palette_ 
   - The shortcut for this menu is:
   - Windows: `Control+Shift+P`
   - Mac: `Command+Shift+P`
2. Begin typing in `Git: Pull From...` and press `Enter` once it is the first option. 
3. Begin typing in `upstream` and press `Enter` once it is the first option.
   - If you do not see "upstream" as an option, follow the "Setup Upstream" instructions below.
4. Press enter with `upstream/master` as the first option.
5. This downloads the latest course materials!

## Setup Upstream Course Material Repository

When you are first setting up your personal workspace repository, you will need to follow these instructions to connect your repository with the "upstream" course material repository. As we add new material through the course you will then be able to easily download it into your personal course workspace repository.

1. Open the _View_ menu and select _Command Palette_
2. Type in _Git: Add Remote_ and press enter with the option selected.
3. Copy and paste the URL below into the text box that says "Provide repository URL" and press enter: 
   - https://github.com/comp110-20f/course-material.git
4. When asked for "Remote name" type in:
   - upstream
5. Press enter.
6. Open the _View_ menu and select _Command Palette_ once more
7. Type in _Git: Fetch From All Remotes_ and press enter
8. The _upstream_ connection is setup! For instructions on how to download new course material from upstream, refer to the section above.
