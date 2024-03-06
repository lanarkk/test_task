from django.contrib import admin

from onboarding.models import Record, RecordData, Template, TemplateField


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', )


@admin.register(TemplateField)
class TemplateFieldAdmin(admin.ModelAdmin):
    list_display = (
        'template',
        'title',
        'tag',
        'type',
        'tab',
        'required',
        )
    list_display_links = ('template', )
    list_editable = ('title', 'tag', 'required', )


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('template', 'dt', )
    list_display_links = ('template', )


@admin.register(RecordData)
class RecordDataAdmin(admin.ModelAdmin):
    list_display = ('record', 'field', 'value', )
    list_display_links = ('record', 'field', )
    list_editable = ('value', )
