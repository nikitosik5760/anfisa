from django.contrib import admin

from .models import IceCream, Comment, Image


class CommentItemInLine(admin.TabularInline):
    model = Comment
    raw_id_fields = ['ice_cream']


class ImageItemInLine(admin.TabularInline):
    model = Image
    fields = ('product', 'image_tag', 'image', 'is_main')
    readonly_fields = ('image_tag',)
    extra = 1


class IceCreamAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'price', 'quantity']
    list_display = ['name', 'price', 'quantity']
    inlines = [CommentItemInLine, ImageItemInLine]


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'content', 'email', 'ice_cream__name']
    list_display = ['name', 'created_at', 'email', 'content', 'ice_cream']
    list_filter = ['name', 'created_at', 'email', 'ice_cream']


admin.site.register(IceCream)
admin.site.register(Comment, CommentAdmin)
