from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from aenea.strict import (Grammar, AppContext, Dictation, Key)
from aenea import AeneaContext, ProxyAppContext


class JetbrainsRule(MergeRule):
    pronunciation = "jet brains"

    mapping = {
        "quickfix":                 R(Key("a-enter"), rdescript="JetBrains: Quick Fix"),
        "duplicate":                R(Key("c-d"), rdescript="JetBrains: Duplicate"),
        "auto complete":            R(Key("cs-a"), rdescript="JetBrains: Auto Complete"),
        "format code":              R(Key("ca-l"), rdescript="JetBrains: Format Code"),
        "show doc":                 R(Key("c-q"), rdescript="JetBrains: Show Documentation"),
        "show param":               R(Key("c-p"), rdescript="JetBrains: Show Parameters"),
        "Jen method":               R(Key("a-insert"), rdescript="JetBrains: Generated Method"),
        "jump to source":           R(Key("f4"), rdescript="JetBrains: Jump To Source"),
        "delete line":              R(Key("c-y"), rdescript="JetBrains: Delete Line"),
        "search symbol":            R(Key("cas-n"), rdescript="JetBrains: Search Symbol"),
        "build":                    R(Key("c-f9"), rdescript="JetBrains: Build"),
        "build and run":            R(Key("s-f10"), rdescript="JetBrains: Build And Run"),
        "next tab":                 R(Key("a-right"), rdescript="JetBrains: Next Tab"),
        "prior tab":                R(Key("a-left"), rdescript="JetBrains: Previous Tab"),
        
        "comment line":             R(Key("c-slash"), rdescript="JetBrains: Comment Line"), 
        "uncomment line":           R(Key("cs-slash"), rdescript="JetBrains: Uncomment Line"), 
        "select ex":                R(Key("c-w"), rdescript="JetBrains: untitled command"), 
        "select ex down":           R(Key("cs-w"), rdescript="JetBrains: entitled command"),
        "search everywhere":        R(Key("c-dot"), rdescript="JetBrains: Search Everywhere"),
        "find in current":          R(Key("cs-f"), rdescript="JetBrains: Find In Current"),
        "go to line":               R(Key("c-g"), rdescript="JetBrains: Go To Line"),

        "go to definition":         R(Key("f12"), rdescript="JetBrains: Go To Definition"),
        "close tab":                R(Key("c-f4"), rdescript="JetBrains: Close Tab"),
        "last tab":                 R(Key("c-tab"), rdescript="JetBrains: Last Tab"),
        "open file":                R(Key("cs-n"), rdescript="JetBrains: open file"),
        "find in files":            R(Key("cs-f"), rdescript="JetBrains: Find In Files"),
        "Klink":                    R(Key("ctrl:down, tab"), rdescript="jet brains: show switcher"),
        "clank":                    R(Key("ctrl:up"), rdescript="jet brains: end switcher"),
        "focus code":               R(Key("escape"), rdescript="JetBrains: ffocus on code"),
        "focus find":               R(Key("ctrl:down, tab/15, 3, ctrl:up"), rdescript="JetBrains: ffocus on find"),
        "focus project":            R(Key("ctrl:down, tab/15, 1, ctrl:up"), rdescript="JetBrains: ffocus on project"),
        "hide find":                R(Key("ctrl:down, tab/15, 3, ctrl:up, s-escape"), rdescript="JetBrains: hide find panel"),
        "hide project":             R(Key("ctrl:down, tab/15, 1, ctrl:up, s-escape"), rdescript="JetBrains: hhide project panel"),
        "show project":             R(Key("a-1/15, escape"), rdescript="JetBrains: show project panel"),
        "show find":                R(Key("a-3/15, escape"), rdescript="JetBrains: show find panel"),
        "rename":                   R(Key("s-f6"), rdescript="JetBrains:  rename"),
        }

    extras = [
              Dictation("text"),
              Dictation("mim"),
              IntegerRefST("n", 1, 1000),
              
             ]
    defaults = {"n": 1, "mim":""}

#---------------------------------------------------------------------------

local_context = AppContext(executable="idea", title="IntelliJ") \
          | AppContext(executable="idea64", title="IntelliJ") \
          | AppContext(executable="studio64") \
          | AppContext(executable="pycharm")
context = AeneaContext(
    ProxyAppContext(cls='jetbrains-pycharm-ce'),
    local_context
    )
grammar = Grammar("IntelliJ + Android Studio + PyCharm", context=context)

if settings.SETTINGS["apps"]["jetbrains"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(JetbrainsRule())
    else:
        rule = JetbrainsRule(name="jet brains")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()