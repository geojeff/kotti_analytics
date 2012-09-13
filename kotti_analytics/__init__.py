from kotti.util import extract_from_settings
from kotti.views.slots import assign_slot

ANALYTICS_WIDGET_DEFAULTS = {
    'tracking_id': '',
    }

def render_analytics_widget(context, request, name=''):
    prefix = 'kotti_analytics.'
    if name:
        prefix += name + '.'
    variables = ANALYTICS_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return variables

def include_widget(config, where='right'): # pragma: no cover
    config.add_view(render_analytics_widget,
                    name='analytics',
                    renderer='templates/analytics_widget.pt')
    assign_slot('analytics', where)
