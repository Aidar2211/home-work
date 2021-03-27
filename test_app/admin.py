from django.contrib import admin
from .models import Category, Product_Name, Comment


class CategoryAdmin(admin.ModelAdmin):
    search_fields = 'name'.split()

#
# class ReviewAdmin(admin.ModelAdmin):
#     fields = 'text product rating'.split()
#     search_fields = 'text rating product created '.split()
#     list_display = 'product rating text created updated'.split()


class ProductAdmin(admin.ModelAdmin):
    fields = 'title category description price created  '.split()
    readonly_fields = 'created '.split()
    list_display = 'title description price '.split()
    search_fields = 'title description'.split()


class CommentAdmin(admin.ModelAdmin):
    list_display = 'name product created '.split()
    search_fields = 'name body'.split()


admin.site.register(Category)
admin.site.register(Product_Name, ProductAdmin)
admin.site.register(Comment, CommentAdmin)


