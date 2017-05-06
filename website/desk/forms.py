from django import forms

from .models import Course, Document


class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
			"course_name",
			"subject",
			"description"

		]