from django.contrib import admin
from .models import Article, Category

# admin.site.disable_action('delete_selected') # from remove actions
# Change header
admin.site.site_header = "صفحه مدریت جنگو ( Django )"
# Register your models here.
def make_published(modeladmin, request,queryset):
    rows_update = queryset.update(status = 'p')
    if rows_update == 1:
        massage_bit = "منتشر شد"
    else:
        massage_bit = "منتشر شدند"
    modeladmin.message_user(request,"{} مقاله {}".format(rows_update,massage_bit))
make_published.short_description = 'انتشار مقالات انتخاب شده'

def make_draft(modeladmin, request,queryset):
    rows_update = queryset.update(status = 'd')
    if rows_update == 1:
        massage_bit = "پیش نویس شد"
    else:
        massage_bit = "پیش نویس شدند"
    modeladmin.message_user(request,"{} مقاله {}".format(rows_update,massage_bit))
make_draft.short_description = 'پیشنویش شدن مقالات انتخاب شده'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','parent','status') # Add information's for show in first look
    list_filter = (['status']) # Add filters
    search_fields = ('title', 'slug') # Add searchbar by args
    prepopulated_fields = {'slug' : ('title',)} # Auto add slug from title
    

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','jpublish','status','category_to_str') # Add information's for show in first look
    list_filter = ('publish','status') # Add filters
    search_fields = ('title', 'description') # Add searchbar by args
    prepopulated_fields = {'slug' : ('title',)} # Auto add slug from title
    ordering = ['status','publish'] # In jango in first order models by id by this we choice our own ordring
    actions = [make_published,make_draft]

    def category_to_str(self, obj):
        return ",".join([category.title for category in obj.active()])
    category_to_str.short_description = 'دسته بندی ها'

admin.site.register(Article, ArticleAdmin)
