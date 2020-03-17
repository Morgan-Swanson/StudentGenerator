from pylatex.base_classes import CommandBase

class EducationEntry(CommandBase):
    _latex_name = 'EducationEntry'

class BoldHeading(CommandBase):
    _latex_name = 'BoldHeading'

class DatedEntry(CommandBase):
    _latex_name = "DatedEntry"

class FirstDatedEntry(CommandBase):
    _latex_name = "FirstDatedEntry"

class NameEntry(CommandBase):
    _latex_name = "NameEntry"

class PageSpacing(CommandBase):
    _latex_name = "PageSpacing"

class WorkEntry(CommandBase):
    _latex_name = "WorkEntry"

class WorkEntryTitle(CommandBase):
    _latex_name = "WorkEntryTitle"

class ItemEntry(CommandBase):
    _latex_name = "ItemEntry"

class EndSection(CommandBase):
    _latex_name = "EndSection" 