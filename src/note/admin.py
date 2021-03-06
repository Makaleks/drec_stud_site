from django.contrib import admin
from utils.custom_admins import CustomBaseAdmin
from reversion.admin import VersionAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import Note, Question

import logging
logger = logging.getLogger('site_events')

# Register your models here.

class NoteAdmin(CustomBaseAdmin, SortableAdminMixin, VersionAdmin):
    history_latest_first = True
    list_display = ('name', 'id_link', 'edited')
    def save_model(self, request, obj, form, change):
        if change:
            fields = [{field: str(getattr(obj, field))} for field in form.changed_data]
            logger.info('{0} \'{1}\' was {2}'.format(self.model.__name__, str(obj), 'edited in {0}'.format(str(fields)) if fields else 'just saved'), extra={'user': request.user.get_full_name()})
        else:
            fields = [{f.name: str(getattr(obj, f.name))} for f in obj._meta.fields]
            logger.info('{0} \'{1}\' was created as {2}'.format(self.model.__name__, str(obj), str(fields)), extra={'user': request.user.get_full_name()})
        return super(NoteAdmin, self).save_model(request, obj, form, change)
    def delete_model(self, request, obj):
        logger.info('{0} \'{1}\' was deleted'.format(self.model.__name__, str(obj)), extra={'user': request.user.get_full_name()})
        return super(NoteAdmin, self).delete_model(request, obj)
admin.site.register(Note, NoteAdmin)


class QuestionAdmin(CustomBaseAdmin, VersionAdmin):
    history_latest_first = True
    list_display = ('author', 'title', 'id_link', 'is_approved', 'is_answered', 'edited', 'created')
    def is_answered(self, obj):
        return obj.is_staff_answered()
    is_answered.short_description = 'Ответ студсовета'
    is_answered.boolean = True
    def save_model(self, request, obj, form, change):
        if change:
            fields = [{field: str(getattr(obj, field))} for field in form.changed_data]
            logger.info('{0} \'{1}\' was {2}'.format(self.model.__name__, str(obj), 'edited in {0}'.format(str(fields)) if fields else 'just saved'), extra={'user': request.user.get_full_name()})
        else:
            fields = [{f.name: str(getattr(obj, f.name))} for f in obj._meta.fields]
            logger.info('{0} \'{1}\' was created as {2}'.format(self.model.__name__, str(obj), str(fields)), extra={'user': request.user.get_full_name()})
        return super(QuestionAdmin, self).save_model(request, obj, form, change)
    def delete_model(self, request, obj):
        logger.info('{0} \'{1}\' was deleted'.format(self.model.title, str(obj)), extra={'user': request.user.get_full_name()})
        return super(QuestionAdmin, self).delete_model(request, obj)
    # Questions are accessable for every is_staff
    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    def has_module_permission(self, request, obj=None):
        return True
admin.site.register(Question, QuestionAdmin)
