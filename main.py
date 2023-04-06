import logging

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

logger = logging.getLogger(__name__)

   
   
class CustomCommandsExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        
        
class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        for i in range(5):
            data = {'new_name': 'Item %s was clicked' % i}
            items.append(ExtensionResultItem(name='Item%s' %i,
                                             description='Item description %s' %i,
                                             on_enter=ExtensionCustomAction(data, keep_app_open=True)))    
            
        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        return RenderResultListAction([ExtensionResultItem(name=data['new_name'],
                                                           on_enter=HideWindowAction())])
    
if __name__ == '__main__':
    CustomCommandsExtension().run()