from aenea.strict import (Grammar, AppContext, MappingRule,
                       Dictation, IntegerRef, Key)

from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.state.short import R

from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib import control


class CommandRule(MergeRule):
    pronunciation = "slack"

    mapping = {
        "open channel": R(Key("c-k"), rdescript="Slack: Open Channel"),
        "open all threads": R(Key("cs-t"), rdescript="Slack: Open All Threads"),
        #"next team": R(Key("cs-]"), rdescript="Slack: Open Team One"),
        "open team <n>": R(Key("c-%(n)d"), rdescript="Slack: open team"),

    }
    extras = [
        Dictation("text"),
        Dictation("mim"),
        IntegerRefST("n", 1, 1000),
    ]
    defaults = {"n": 1, "mim": ""}


# ---------------------------------------------------------------------------

context = AppContext(executable="slack")
grammar = Grammar("slack", context=context)
grammar.add_rule(CommandRule(name="slack"))
if settings.SETTINGS["apps"]["slack"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(CommandRule())
    else:
        grammar.load()