from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from DropBox.models import Folder

admin.site.register(
    Folder,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    )
)