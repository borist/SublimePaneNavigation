import sublime
import sublime_plugin


class PaneNavigationCommand(sublime_plugin.TextCommand):
    """
    Cycle through to next/previous pane in a window with multiple panes,

    @param direction: 1 to navigate to next pane, -1 to navigate to
                        previous pane
    """
    def run(self, view, direction):
        window = self.view.window()
        num_panes = window.num_groups()
        active_pane = window.active_group()
        window.focus_group((active_pane + direction) % num_panes)


class NextViewInPaneCommand(sublime_plugin.TextCommand):
    """
    Switch to the next tab in the active pane, in the order that the
    tabs are open in the pane, cycling to the first tab if called on the
    last tab.
    """
    def run(self, view):
        change_tab(self, view, 1)


class PrevViewInPaneCommand(sublime_plugin.TextCommand):
    """
    Switch to the previous tab in the active pane, in the order that the
    tabs are open in the pane, cycling to the first tab if called on the
    last tab.
    """
    def run(self, view):
        change_tab(self, view, -1)


def change_tab(self, view, direction):
    """
    Cycle through to the next/previous tab in the active pane, in the
    order that the tabs are open in the pane.

    @param direction: 1 to navigate to next tab, -1 to navigate to
                        previous tab
    """
    window = self.view.window()
    group_index, view_index = window.get_view_index(window.active_view())
    views = window.views_in_group(group_index)
    window.focus_view(views[(view_index + direction) % len(views)])
