from django import forms

class CreateNewTask(forms.Form):
	title = forms.CharField(label='Título de tarea', 
		max_length=200,
		widget=forms.TextInput(attrs={'class': 'input'})
	)
	description = forms.CharField(label='Descripción de la tarea', 
		widget=forms.Textarea(attrs={'class': 'input'})
	)

class CreateNewProject(forms.Form):
	name = forms.CharField(label='Nombre del projecto',
		max_length=200,
		widget=forms.TextInput(attrs={'class': 'input'})
	)