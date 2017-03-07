"""
__author__ = 'Zone22'
Command-module for Atom
Official Site "https://atom.io/"
"""
from aenea.strict import (Grammar, AppContext, MappingRule,
                       Dictation, IntegerRef,
                       Key, Text, Repeat, Pause)
from dragonfly.actions.action_mimic import Mimic

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


# How long to wait for the Atom palette to load before hitting the enter key
atom_palette_wait = "30"
if settings.SETTINGS["miscellaneous"]["atom_palette_wait"]:
    atom_palette_wait = settings.SETTINGS["miscellaneous"]["atom_palette_wait"]


class AtomRule(MergeRule):
    pronunciation = "atom"

    mapping = {

# Spoken commands that are commented out do not have assigned default shortcut keys or are incompatible.
# The '#extra' subsection of commands that fit within the category but are not displayed by the menu or UI
# Legend: '#' for not assigned, '##' for shortcut or functional duplicate.
# ----------Spoken Command/Action------------------> Shortcut keys----------> #Displayed Text

    #Basic Cursor Navigation
            "up [<n>]":                                R(Key("up"), rdescript="Atom: Move Cursor Up #") * Repeat(extra="n"),
            "down [<n>]":                              R(Key("down"), rdescript="Atom: Move Cursor Down #") * Repeat(extra="n"),
            "right [<n>]":                             R(Key("right"), rdescript="Atom: Move Cursor Right #") * Repeat(extra="n"),
            "left [<n>]":                              R(Key("left"), rdescript="Atom: Move Cursor Left #") * Repeat(extra="n"),
    #Basic White Text Manipulation
            "tab|indent [<n>]":                        R(Key("tab"), rdescript="Atom: Press Tab Key #") * Repeat(extra="n"),
            "space [<n>]":                             R(Key("space"), rdescript="Atom: Press Tab Key #") * Repeat(extra="n"),
# Menu UI-------------------------------------------------------------------------------------------
    #File Menu
            "[open] new window":                       R(Key("cs-n"), rdescript="Atom: New Window"),
            "new file":                                R(Key("c-n"), rdescript="Atom: New File"),
            "open file":                               R(Key("c-o"), rdescript="Atom: Open File"),
            "open folder":                             R(Key("cs-o"), rdescript="Atom: Open Folder"),
            "add project folder":                      R(Key("ac-o"), rdescript="Atom: Add Project Folder"),
            "open settings":                           R(Key("c-comma"), rdescript="Atom: Open Settings"),
            "[open] last tab":                         R(Key("cs-t"), rdescript="Atom: Reopen Last File or Tab"),
            "reopen closed item":                      R(Key("cs-p") + Text("Reopen Closed Item") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Reopen Last File or Tab"),
            "open [your] config":                      R(Key("cs-p") + Text("Open Your Config") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open Your Config"),
            "open [your] int script":                  R(Key("cs-p") + Text("Open Your Int Script") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open Your Int Script"),
            "open [your] key map":                     R(Key("cs-p") + Text("Open Your Key Map") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open Your Key Map"),
            "open [your] snippet":                     R(Key("cs-p") + Text("Open Your Snippet") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open Your Snippet"),
            "open [your] stylesheet":                  R(Key("cs-p") + Text("Open your Stylesheet") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open Your Stylesheet"),
            "save":                                    R(Key("c-s"), rdescript="Atom: Save"),
            "save as":                                 R(Key("cs-s"), rdescript="Atom: Save As"),
            "save all":                                R(Key("cs-p") + Text("Save All") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Save All"),
            "close pane":                              R(Key("cs-p") + Text("Pane Close") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Close Pane"),
            "close pane others":                       R(Key("cs-p") + Text("Pane Close Other Items") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Close Pane"),
            "close window":                            R(Key("cs-w"), rdescript="Atom: Close Window"),
        #Extra
    #Edit Menu
            "cut":                                     R(Key("s-delete"), rdescript="Atom: Cut"),
            "copy ":                                   R(Key("c-insert"), rdescript="Atom: Copy"),
            "paste [<n>]":                             R(Key("s-insert"), rdescript="Atom: Paste") * Repeat(extra="n"),
            "copy path":                               R(Key("cs-c"), rdescript="Atom: Copy Path"),
            "select all":                              R(Key("c-a"), rdescript="Atom: Select All"),
            "[toggle] comments":                       R(Key("c-slash"), rdescript="Atom: Toggle Comments"),
            "reflow section":                          R(Key("ac-q"), rdescript="Atom: Reflow Section"),
            "select encoding":                         R(Key("cs-u"), rdescript="Atom: Select Encoding"),
            "[go to] line <n>":                        R(Key("c-g") + Pause("10") + Text("%(n)s") + Key("enter"), rdescript="Atom: Go to Line #"),
            "select grammar":                          R(Key("cs-l"), rdescript="Atom: Select Grammar"),
        #Lines Submenu
            ##"indent":                                  R(Key("c-lbrace"), rdescript="Atom: Indent"), # Rework Dragonfly Keymapping
            "outdent":                                 R(Key("c-rightbrace"), rdescript="Atom: Outdent"),
            "auto indent editor":                      R(Key("cs-p") + Text("Editor Auto Indent") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Auto Indent"),
            "auto indent windows":                     R(Key("cs-p") + Text("Window Auto Indent") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Auto Indent"),
            "[move] line up [<n>]":                    R(Key("c-up"), rdescript="Atom: Move Line Up #") * Repeat(extra="n"),
            "[move] line down [<n>]":                  R(Key("c-down"), rdescript="Atom: Move Line Down #") * Repeat(extra="n"),
            "duplicate line [<n>]":                    R(Key("cs-d"), rdescript="Atom: Duplicate Line") * Repeat(extra="n"), #Unless remapped the command triggers Dragon NaturallySpeaking dictation box
            "delete line [<n>]":                       R(Key("cs-k"), rdescript="Atom: Delete Line or # Lines Below") * Repeat(extra="n"),
            "join line":                               R(Key("c-j"), rdescript="Atom: Join Line"),
        #Text Submenu
            "uppercase":                               R(Key("cs-p") + Text("Editor Upper Case") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Convert Uppercase"),
            "lowercase":                               R(Key("cs-p") + Text("Editor Lower Case") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Convert lowercase"),
            "delete [to] end of word [<n>]":           R(Key("c-delete"), rdescript="Atom: Delete to End oF Word") * Repeat(extra="n"),
            "delete sub word [<n>]":                   R(Key("a-backspace"), rdescript="Atom: Delete to End of Subword") * Repeat(extra="n"),
            "delete [to] previous word [<n>]":         R(Key("cs-p") + Text("Delete to Previous Word boundary") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Delete to previous word boundary") * Repeat(extra="n"),
            "delete [to] next word [<n>]":             R(Key("cs-p") + Text("Delete to Next Word Boundary") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Delete to next word boundary") * Repeat(extra="n"),
            ##"delete line":                           R(Key("cs-k"), rdescript="Atom: Delete Line"),
            "transpose":                               R(Key("cs-p") + Text("Transpose") +  Key("enter"), rdescript="Atom: Transpose"),
        #Folding Submenu
            "make fold":                               R(Key("acw-f"), rdescript="Atom: Make Fold"),
            "fold":                                    R(Key("ac-lbrace"), rdescript="Atom: Fold"),
            "unfold":                                  R(Key("ac-rightbrace"), rdescript="Atom: Unfold"),
            "unfold all":                              R(Key("acs-rightbrace"), rdescript="Atom: Unfold All"),
            "fold [level] [<n2>]":                     R(Key("c-%(n)s"), rdescript="Atom: Fold Level 1-9"),
        #Bookmarks Submenu
            "view all":                                R(Key("c-f2"), rdescript="Atom: Reflow Section"),
            "bookmark | book":                         R(Key("ca-f2"), rdescript="Atom: Toggle Bookmark"),
            "next bookmark | next book":               R(Key("f2"), rdescript="Atom: Jump to Next Bookmark"),
            "previous bookmark | previous book":       R(Key("s-f2"), rdescript="Atom: Jump to Previous Bookwork"),
    #View Menu
            "reload file":                             R(Key("ac-r"), rdescript="Atom: Reload File"),
            "fullscreen":                              R(Key("f11"), rdescript="Atom: Toggle Fullscreen"),
            "toggle menubar":                          R(Key("cs-p") + Text("Toggle Menu Bar") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Toggle Menubar"),
            "increase font [size] [<n>]":              R(Key("cs-equals"), rdescript="Atom: Increase Font Size") * Repeat(extra="n"),
            "decrease font [size] [<n>]":              R(Key("cs-minus"), rdescript="Atom: Decrease Font size") * Repeat(extra="n"),
            "reset font [size]":                       R(Key("c-0"), rdescript="Atom: Reset Font Size"),
            "toggle soft wrap":                        R(Key("cs-p") + Text("Toggle Soft Wrap") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Toggle Soft Wrap"),
            ##"toggle command palette":                  R(Key(""), rdescript="Atom: Toggle Command Palette"),
            "[toggle] treeview":                       R(Key("c-backslash"), rdescript="Atom: Toggle Treeview"),
        #Panes Submenu
            "split above":                             R(Key("cs-p") + Text("Pane: Split Up") + Pause(atom_palette_wait) + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Split Up"),
            "split below":                             R(Key("cs-p") + Text("Pane: Split Down") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Split Down"),
            "split left":                              R(Key("cs-p") + Text("Pane: Split Left") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Split Left"),
            "split right":                             R(Key("cs-p") + Text("Pane: Split Right") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Split Right"),
            "focus [on] next [pane]":                  R(Key("cs-p") + Text("Window: Focus Next Pane") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Focus Next Pane"),
            "focus [on] previous [pane]":              R(Key("cs-p") + Text("Window: Focus Previous Pane") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Focus Previous Pane"),
            "focus [pane] [on] above":                 R(Key("cs-p") + Text("Window: Focus Pane Above") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Focused Pane Above"),
            "focus [pane] [on] below":                 R(Key("cs-p") + Text("Window: Focus Pane Below") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Focus Pane Below"),
            "focus [pane] [on] left":                  R(Key("cs-p") + Text("Window: Focus Pane on Left") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Focus On left"),
            "focus [pane] [on] right":                 R(Key("cs-p") + Text("Window: Focus Pane on Right") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Focus Pane on Right"),
            ##"close pane":                              R(Key("cs-p") + Text("Window: pane close") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Close Pane"),
        #extras
            "[go to] pane [<n2>]":                     R(Key("a-%(n)s"), rdescript="Atom: Go to Pane 1-9"),
            "focus previous":                          R(Key("cs-p") + Text("Core: Focus Previous") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Focus Previous"),
            "next pane":                               R(Key("cs-p") + Text("Window: Focus Previous Pane") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Next Pane"),
            "previous pane":                           R(Key("cs-p") + Text("Window: Focus Next Pane") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Previous Pane"),
        #Developer Submenu
            #"open in development mode":                R(Key(""), rdescript="Open in Development Mode"),
            "run atom [specs]":                        R(Key("ac-s"), rdescript="Atom: Run Atoms Specs"),
            "run package [specs]":                     R(Key("ac-p"), rdescript="Atom: Run Package Specs "),
            "[toggle] developer tools":                R(Key("ac-i"), rdescript="Atom: Toggle Developer Tools"),
    #Selection Menu
            "[add] selection above [<n>]":             R(Key("ac-up"), rdescript="Atom: Add Selection Above #") * Repeat(extra="n"),
            "[add] selection below [<n>]":             R(Key("ac-down"), rdescript="Atom: Add Selection Below #") * Repeat(extra="n"),
            "split into lines":                        R(Key("cs-p") + Text("Split Into Lines") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Split Into lines"),
            "single Section":                          R(Key("escape"), rdescript="Atom: Single Section"),
            "select [to] top":                         R(Key("cs-home"), rdescript="Atom: Select to Top"),
            "select [to] bottom":                      R(Key("cs-end"), rdescript="Atom: Select to Bottom"),
            "select line":                             R(Key("c-l"), rdescript="Atom: Select Line"),
            "select word [<n>]":                       R(Key("cs-p") + Text("Editor: Word") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Select Word") * Repeat(extra="n"),
            "[select] [to] beginning [of] word [<n>]": R(Key("cs-left"), rdescript="Atom: Select to Beginning of Word #") * Repeat(extra="n"),
            "[select] [to] end of word [<n>]":         R(Key("cs-right"), rdescript="Atom: Select to End of Word #") * Repeat(extra="n"),
            "[select] [to] beginning [of] line":       R(Key("cs-p") + Text("Editor: Select to Beginning of Line") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Select to Beginning of line"),
            "[select] [to] first character of line":   R(Key("s-home"), rdescript="Atom: Select to First Character of Line"),
            "[select] [to] end of line":               R(Key("s-end"), rdescript="Atom: Select to End of line"),
            "[select] inside brackets":                R(Key("ac-m"), rdescript="Atom: Select Inside Brackets"),
    #Find Menu
            "find in buffer":                          R(Key("c-f"), rdescript="Atom: Find in Buffer"),
            "replacing in buffer":                     R(Key("ac-f"), rdescript="Atom: Replacing in Buffer"),
            "select next":                             R(Key("c-d"), rdescript="Atom: Select Next"),
            "find select all":                         R(Key("a-f3"), rdescript="Atom: Select All"),
            "find replace next":                       R(Key("cs-p") + Text("Find and Replace: Replace Next") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Replace Next"),
            "find replace all":                        R(Key("cs-p") + Text("Find and Replace: Replace All") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Replace All"),
            "find buffer":                             R(Key("c-b"), rdescript="Atom: Find Buffer"),
            "find file":                               R(Key("c-p"), rdescript="Atom: Find File"),
            "find modified file":                      R(Key("cs-b"), rdescript="Atom: Find Modified File"),
    #Packages Menu
        #Bracket Matcher Submenu
            "bracket [go to] match":                   R(Key("c-m"), rdescript="Atom: Go To Matching Bracket"),
            ##"select inside bracket":                 R(Key("ac-m"), rdescript="Atom: Select inside bracket"),
            "bracket remove [from] selection":         R(Key("c-lbrace"), rdescript="Atom: Remove Bracket from Selection"),
            "close [current] tag":                     R(Key("cs-p") + Text("Bracket Matcher: Close Tag") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Close current tag"),
            "bracket remove matching":                 R(Key("ac-backspace"), rdescript="Atom: Remove matching brackets"),
        #Command Palette Submenu
            "[toggle] [command] palette":              R(Key("cs-p"), rdescript="Atom: Toggle Command Palette"),
        #Dev Live Reload Submenu
            "reload [all] styles":                     R(Key("acs-r"), rdescript="Atom: Reload All Styles"),
        #Git Diff Submenu
            "move to next diff [different]":           R(Key("cs-p") + Text("Move to Next Diff") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Move to Next Diff"),
            "move to previous diff [different]":       R(Key("cs-p") + Text("Move to Previous Diff") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Move to Previous Different"),
            "[toggle] diff List":                      R(Key("cs-p") + Text("Toggle Diff List") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Toggle Diff List"),
        #Keybinding Resolver Submenu
            "toggle key [binding] resolver":           R(Key("cs-p") + Text("Key Binding Resolver: Toggle") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Toggle Keybinding Resolver"),
        #Markdown Preview Submenu
            "markdown preview":                        R(Key("cs-m"), rdescript="Atom: Markdown Toggle Preview"),
        #Extras
            "markdown copy html":                      R(Key("cs-p") + Text("Markdown Preview: Copy HTML") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Markdown Preview: Copy HTML"),
            "markdown toggle break on newline":        R(Key("cs-p") + Text("Markdown Preview: Toggle Break On Single Newline") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Markdown Preview: Toggle Break On Single Newline"),
        #Package Generator Submenu
            "make|generate package":                   R(Key("cs-p") + Text("Package Generator: Generate Package") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Generate Atom Package"),
            "make|generate syntax theme":              R(Key("cs-p") + Text("Package Generator: Generate Syntax Theme") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Generate Atom Syntax Theme"),
        #Settings View Submenu
            ##"open setting":                             R(Key("c-comma"), rdescript="Atom: Open Setting"),
            "show key bindings":                       R(Key("cs-p") + Text("Settings View: Show Key Bindings") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Show Keybindings"),
            "installed themes":                        R(Key("cs-p") + Text("Settings View: Installed Themes") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Install Themes"),
            "uninstalled themes":                      R(Key("cs-p") + Text("Settings View: Uninstall Themes") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Uninstall Themes"),
            "installed packages":                      R(Key("cs-p") + Text("Settings View: Installed Packages") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Install Packages"),
            "uninstalled packages":                    R(Key("cs-p") + Text("Settings View: Uninstalled Packages") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Uninstall packages/themes"),
            "search packages|themes":                  R(Key("cs-p") + Text("Settings View: Install Packages and Themes") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Install Packages/Themes"),
            "update packages":                         R(Key("cs-p") + Text("Settings View: Check for Package Update") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Check for Packages"),
        #Snippets Submenu
            "expand snippets":                         R(Key("cs-p") + Text("Snippets: Expand") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Expand Snippets"),
            "next snippet":                            R(Key("tab"), rdescript="Atom: Next Stop|Snippet"),
            "previous snippet":                        R(Key("a-tab"), rdescript="Atom: Previous Stop|Snippet"),
            "available snippet":                       R(Key("as-tab"), rdescript="Atom: Available Snippets"),
        #Styleguide Submenu
            "show style [guide]":                      R(Key("cs-g"), rdescript="Atom: Show Styleguide"),
            #Symbol
            "find symbol":                             R(Key("c-r"), rdescript="Atom: Find Symbol"),
            "project symbol":                          R(Key("cs-r"), rdescript="Atom: Project Symbol"),
        #Timecop Submenu
            "timecop":                                 R(Key("cs-p") + Text("Timecop: View") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Show Timecop"),
        #Tree View Submenu
            "tree focus":                              R(Key("c-0"), rdescript="Atom: Toggle Focus on TreeView"),
            "tree [View] [toggle] view":               R(Key("c-backslash"), rdescript="Atom: Toggle"),
            "tree [View] [reveal] active file":        R(Key("cs-backslash"), rdescript="Atom: Reveal Active File"),
            "tree [View] [toggle] side":               R(Key("cs-p") + Text("Tree View: show") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Toggle Tree Side"),
        #Extras
            "tree show":                               R(Key("cs-p") + Text("Tree View: Show") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Tree View: Show"),
            "tree rename":                             R(Key("cs-p") + Text("Tree View: Rename") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Tree View: Rename"),
            "tree remove":                             R(Key("cs-p") + Text("Tree View: Remove") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Tree View: Remove"),
            "tree add file":                           R(Key("cs-p") + Text("Tree View: Add File") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Tree View: Add File"),
            "tree duplicate":                          R(Key("cs-p") + Text("Tree View: Duplicate") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Tree View: Duplicate"),
            "tree add folder":                         R(Key("cs-p") + Text("Tree View: Add Folder") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Tree View: Add Folder"),
        #Whitespaces Submenu
            "remove trailing [white] spaces":          R(Key("cs-p") + Text("Whitespace: Remove Trailing Whitespace") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Remove Trailing White Spaces"),
            "convert tabs [to] spaces":                R(Key("cs-p") + Text("Whitespace: Convert Tabs to Spaces") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Convert Tabs to Spaces"),
            "convert spaces [to] tabs":                R(Key("cs-p") + Text("Whitespace: Convert Spaces to Tabs") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Convert Spaces to Tabs"),
        #Merge Conflicts Submenu
            "git [detect] [merge] conflicts":          R(Key("cs-p") + Text("Merge Conflicts Detect") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Detect"),

# ----Atom Optional Third-Party Packages and Dependencies-----------------------------------------------------------------------------
 #Install through command prompt, Atom install manager or a .bat file at http://tinyurl.com/Atom-Dependencies
    # pip install --upgrade autopep8T
    # apm install project-sidebar
    # apm install project-manager
    # apm install git-plus
    # apm install script
    # apm install atom-beautify
    # apm install goto-last-edit
    # apm install tab-numbers
    # apm install menu-manager
    # apm install string-looper
    # apm install toggle-quotes
    # apm install delete-Plus
    # apm install expand-selection-to-quotes
    # apm install highlight-selected
    # apm install sublime-style-column-selection

#Atom Third-Party Package Commands-------------------------------------------------------------------------------------------------
        #Atom Beautify
            "beautify editor":                         R(Key("cs-p") + Text("Atom Beautify: Beautify Editor") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom : Beautify Editor"),
            "beautify migrate settings":               R(Key("cs-p") + Text("Atom Beautify: Migrate Settings") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Beautify: Migrate Settings"),
            "beautify debug editor":                   R(Key("cs-p") + Text("Atom Beautify: Help Debug Editor") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Beautify: Debug Editor"),
        #Toggle Quotes
            "toggle quotes":                           R(Key("cs-apostrophe"), rdescript="Atom: Toggle Quotes: Single or Double"),
        #Script
            "script run":                              R(Key("cs-p") + Text("Script: Run") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Script: run"),
            "script [run] options":                    R(Key("cs-p") + Text("Script: Run Options") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Script: Run Options or Configure"),
            "script [run] profile":                    R(Key("cs-p") + Text("Script: Run With Profile") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Script: Run With Profile"),
            "script run [by] line":                    R(Key("cs-p") + Text("Script: Run By Line Number") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Script: Run Script by Line"),
            "script kill [process]":                   R(Key("cs-p") + Text("Script: Kill Process") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Script: Kill Process"),
            "script close view":                       R(Key("cs-p") + Text("Script: Close View") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Script: Close View"),
            "script copy [run] [results]":             R(Key("cs-p") + Text("Script: Copy Run Results") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Script: Copy Run Results"),
            #"script close window and stop script":     R(Key("cs-p") + Text("Script: Close Window and Stop Script") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Script: Close Window and Stop Script"),
        #Delete Plus
            "delete words":                            R(Key("cs-p") + Text("Delete Plus: Delete") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Delete Plus"),
        #Last Edit
            "back edit":                               R(Key("c-i"), rdescript="Atom: Previous Edit"),
            "next edit":                               R(Key("ca-i"), rdescript="Atom: Next Last Edit"),
        #Looper
            #"cursor loud|capitalize [<n3>]":           R(Key("a-down"), rdescript="Atom: Looper Capitalize") * Repeat(extra="n"), # Not fully implemented
            #"cursor camel [<n4>]":                     R(Key("a-down"), rdescript="Atom: Looper Camelcase") * Repeat(extra="n"), # Not fully implemented
            #"cursor lowercase [<n5>]":                 R(Key("a-down"), rdescript="Atom: Looper Lowercase") * Repeat(extra="n"), # Not fully implemented
            "looping down cursor":                     R(Key("a-down"), rdescript="Atom: Looping Down at Cursor"),
            "looping up cursor":                       R(Key("a-up"), rdescript="Atom: Looping Up at Cursor"),
            "looping up":                              R(Key("wa-up"), rdescript="Atom: Looping Up"),
            "looping down":                            R(Key("wa-down"), rdescript="Atom: Looping Down"),
    #Open on GitHub
            "github [open] blame":                     R(Key("cs-p") + Text("Open on GitHub: Blame") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open On Github @ Blame"),
            "github [open] [branch] compare":          R(Key("cs-p") + Text("Open on GitHub: Branch Compare") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open On Github @ Branch Compare"),
            "github [open] [copy] URL":                R(Key("cs-p") + Text("Open on GitHub: Copy URL") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open On Github @ Copy URL"),
            "github [open] file":                      R(Key("cs-p") + Text("Open on GitHub: File") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open On Github @ File"),
            "github [open] history":                   R(Key("cs-p") + Text("Open on GitHub: History") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open On Github @ History"),
            "github [open] issues":                    R(Key("cs-p") + Text("Open on GitHub: Issues") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open On Github @ Issues"),
            "github [open] repository":                R(Key("cs-p") + Text("Open on GitHub: Repository") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Open On Github @ Repository"),
    #Git Plus
            "git custom|run":                          R(Key("cs-p") + Text("Git Plus: Run") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Run"),
            "git log":                                 R(Key("cs-p") + Text("Git Plus: Log") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Log"),
            "git log current [file]":                  R(Key("cs-p") + Text("Git Plus: Log Current File") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Current File"),
            "git status":                              R(Key("cs-p") + Text("Git Plus: Status") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Status"),
            "git show":                                R(Key("cs-p") + Text("Git Plus: Show") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Show"),
            "git tags":                                R(Key("cs-p") + Text("Git Plus: Tags") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Tags"),
            "git open changed files":                  R(Key("cs-p") + Text("Git Plus: Git Open Changed Files") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Open Changed Files"),
            "git checkout [branch|tag]":               R(Key("cs-p") + Text("Git Plus: Checkout") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Checkout Branch|Tag"),
            "git menu":                                R(Key("cs-p") + Text("Git Plus: Menu") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Menu"),
            "git pull":                                R(Key("cs-p") + Text("Git Plus: Pull") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Pull"),
            "git pull [using] rebase":                 R(Key("cs-p") + Text("Git Plus: Pull Using Rebase") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Pull Using Rebase"),
            "git push":                                R(Key("cs-p") + Text("Git Plus: Push") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Push"),
            "git commit":                              R(Key("cs-p") + Text("Git Plus: Commit") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Commit"),
            "git commit amend":                        R(Key("cs-p") + Text("Git Plus: Commit Amend") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Commit Amend"),
            "git merge":                               R(Key("cs-p") + Text("Git Plus: Merge") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Merge"),
            "git merge remote":                        R(Key("cs-p") + Text("Git Plus: Merge Remote") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Merge Remote"),
            "git diff":                                R(Key("cs-p") + Text("Git Plus: Diff") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Diff"),
            "git diff all":                            R(Key("cs-p") + Text("Git Plus: Diff All") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Diff All"),
            "git add":                                 R(Key("cs-p") + Text("Git Plus: Add") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Add"),
            "git add all":                             R(Key("cs-p") + Text("Git plus: Add All") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Add All"),
            "git add [and] commit":                    R(Key("cs-p") + Text("Git Plus: Add And Commit") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Add And Commit"),
            "git add all [and] commit":                R(Key("cs-p") + Text("Git Plus: Add All and Commit") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Add All and Commit"),
            "git add all commit [and] push":           R(Key("cs-p") + Text("Git Plus: Add All Commit And Push") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Add All Commit Push"),
            "git new branch":                          R(Key("cs-p") + Text("Git Plus: New Branch") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git New Branch"),
            "git rm|remove":                           R(Key("cs-p") + Text("Git Plus: Remove") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Git Remove"),
    #Project Manager
            "project manager [list]":                  R(Key("cs-p") + Text("Project Manager:List") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Project Manager: Toggle"),
            "project manager save":                    R(Key("cs-p") + Text("Project Manager:Save Project") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Project Manager: Save Project"),
            "project manager edit":                    R(Key("cs-p") + Text("Project Manager:Edit Project") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Project Manager: Edit Project"),
    #Menu Sidebar
            "[project manager] sidebar":               R(Key("cs-p") + Text("Project Sidebar: Toggle") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: Project Sidebar: Toggle"),
    #Expand Selection to Quotes
            "expand|fill quotes":                      R(Key("c-apostrophe"), rdescript="Atom: Expand Selection to Quotes"),
    #Auto Complete
            "auto [complete]":                         R(Key("c-space"), rdescript="Atom: Show Auto Complete Menu"),
    #Highlight Selected---- #Placeholder
    #Sublime Style Column Selection---- #Placeholder

#Atom | Dragonfly Development--------------------------------------------------------------------------------------------------------------------------------------------------------
    # Template to create more commands. Documentation: https://dragonfly.readthedocs.org/en/latest/actions.html and http://caster.readthedocs.io/en/latest/caster/doc/Intro/
        # Used for basic key shortcuts
            #"text for voice command":               R(Key("modifier-key"), rdescript="program name: command name/description"),
            #"":                                     R(Key(""), rdescript="Atom: "),
        # Used for command that utilizes the "command palette" shortcut in the absence of assigned keyboard shortcut.
            #"text for voice command":               R(Key("cs-p") + Text("text as described in command palette") + Pause(atom_palette_wait) + Key("enter"), rdescript="command name/description"),
            #"":                                     R(Key("cs-p") + Text("") + Pause(atom_palette_wait) + Key("enter"),
    #Atom Shortcut Snippets
            "dev keys [input] [<n>]":                R(Text('       #"":                                     R(Key("-"), rdescript="Atom: "),') + Key("enter"), rdescript="Macro: Dev Keys #") * Repeat(extra="n"),
            "dev [command] palette [<n>]":           R(Text('       #"":                                     R(Key("cs-p") + Text("") + Pause(atom_palette_wait) + Key("enter"), rdescript="Atom: "),') + Key("enter"), rdescript="Macro: Dev Command Palette #") * Repeat(extra="n"),
            "dev convert":                           Text('R(Key("cs-p") + Text("") + Pause(atom_palette_wait) + Key("enter"),') + Key("delete"),
        #Repeatable Snippets
            "dev numb keys [input] [<n>]":           R(Text('#" [<n>]":                                R(Key("-"), rdescript="Atom: ") * Repeat(extra="n"),') + Key("enter"), rdescript="Macro: Numb Dev Keys #") * Repeat(extra="n"),
            "dev numb [command] palette [<n>]":      R(Text('#" [<n>]":                                R(Key("cs-p") + Text("") + Pause(atom_palette_wait) + Key("enter") + Pause(atom_palette_wait), rdescript="Atom: ") * Repeat(extra="n"),') + Key("enter"), rdescript="Macro: Dev Numb Command Palette #") * Repeat(extra="n"),
    #Basic Dragonfly Snippets
            "dev key [<n>]":                         R(Text('"":                                Key(""),'), rdescript="Dragonfly: Print Dev Key #") * Repeat(extra="n"),
            "dev text [<n>]":                        R(Text('"":                                Text(""),'), rdescript="Dragonfly: Print Dev Text #") * Repeat(extra="n"),
            }
    extras = [
            Dictation("text"),
            Dictation("mim"),
            IntegerRefST("n", 1, 10000),
            IntegerRefST("n2", 1, 9),

             ]
    defaults = {"n": 1, "mim":""}

#---------------------------------------------------------------------------

context = AppContext(executable="atom", title="Atom")
grammar = Grammar("Atom", context=context)
if settings.SETTINGS["apps"]["atom"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(AtomRule())
    else:
        rule = AtomRule()
        gfilter.run_on(rule)
        grammar.add_rule(AtomRule(name="atom"))
        grammar.load()
