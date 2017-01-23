"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'code.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'code.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard
from admin_tools.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for code.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick actions'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('Create Missions'), '/admin/gm/mission/'],
                [_('Complete Stages'), '/admin/gm/stage/'],
                [_('Team Management'), '/admin/gm/team/'],
            ]
        ))

        self.children.append(modules.DashboardModule(
            title="HI",
            children=['Welcome to the admin. Here you can chose quick actions from the above, or you can dive into the CMS in the "Applications" menu. To add GMs, hit the Administration menu.'],
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 10))
