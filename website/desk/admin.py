from django.contrib import admin

# Register your models here.
from .models import Course, Coin, Document

class CourseAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","user_name","subject","timestamp"]
	list_filter = ["timestamp"]
	search_fields = ["course_name", "user_name","subject"]
	class Meta:
		model = Course


class CoinAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","coin"]
	search_fields = ["user_name"]
	class Meta:
		model = Coin



class DocumentAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","course_id"]
	search_fields = ["course_id","title"]
	class Meta:
		model = Document


admin.site.register(Course, CourseAdmin)
admin.site.register(Coin, CoinAdmin)
admin.site.register(Document, DocumentAdmin)