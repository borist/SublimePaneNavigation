SublimePaneNavigation
=====================

"SublimePaneNavigation" is a plugin for the Sublime Text 2 editor that provides increased keyboard navigation between tabs and panes (when using multiple panes). This plugin primarly does 2 things:

1. **Tab Navigation:** Changes the `ctrl+tab` and `ctrl+shift+tab` key bindings to cycle through the tabs in the **active pane** (i.e. current group) in the order that they appear in the pane (as opposed to in order of recency, as is the default).
2. **Split Pane Navigation:** Adds key bindings for `ctrl+]` and `ctrl+[` to cycle through the multiple panes open in a window (if there are multiple panes).

Installation
------------
SublimePaneNavigation is available for installed through [Package Control](http://wbond.net/sublime_packages/package_control/installation) for Sublime Text 2. The advantage of using this method is that Package Control will automatically keep SublimeLinter up to date with the latest version. To install it with Package Control:

* Make sure you have Package Control installed, instructions available at http://wbond.net/sublime_packages/package_control/installation
* Once you install Package Control, restart Sublime Text 2 and bring up the Command Palette with `cmd+shift+P` (on Mac OS X) or `ctrl+shift+P` (on Windows or Linux).
* Select "Package Control: Install Package" and  wait while Package Control fetches the latest package list.
* Then, start typing "SublimePaneNavigation" and select it from the list when it appears (restarting Sublime Text 2 is not necessary).

Usage
-----
There are four key bindings associated with this plugin (note that in the descriptions, "next" and "previous" refer to the order in which the tabs/panes appear in the window, not based on recency as is the default in Sublime Text 2):

* `ctrl+tab`: cycle to the next tab in the active pane
* `ctrl+shift+tab`: cycle to the previous tab in the active pane
* `ctrl+]`: cycle to the next pane in the active window
* `ctrl+[`: cycle to the previous pane in the active window

Configuring
-----------
If you would like part of the available functionality (for example, if you only want the split pane navigation), simply comment out the key bindings for the unwanted functionality. Additionally, if you would like to change the key bindings, simply edit the "Key Bindings" file available in the preferences menu: `Preferences->Package Settings->SublimePaneNavigation->Key Bindings - Default`.
