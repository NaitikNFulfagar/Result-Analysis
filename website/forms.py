from django import forms
from .models import templates_obj
from .models import PDFUpload

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['pdf_file', 'temp' ,'year', 'sem','new_pdf']
    created_by = forms.CharField(widget=forms.HiddenInput(),required=False)
    pdf_file = forms.FileField(widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    #new_pdf= forms.CheckboxInput(attrs={'class': 'form-check-input'})
    
class AddtemplatesForm(forms.ModelForm):
    
    class Meta:
        model     =  templates_obj
        fields = ['Year','Branch', 'key_value_pairs']
    key_value_pairs = forms.CharField(widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Year'].required = True
        self.fields['Branch'].required = True
        self.fields['key_value_pairs'].required = True
        self.fields['Year'].empty_label = "Select Year"  # Optional: Set a custom label for the empty option
        self.fields['Branch'].empty_label = "Select Branch"  # Optional: Set a custom label for the empty option
        
    def clean(self):
        cleaned_data = super().clean()
        Year = cleaned_data.get("Year")
        Branch = cleaned_data.get("Branch")

        if templates_obj.objects.filter(Year=Year, Branch=Branch).exists():
            raise forms.ValidationError(f"A template for Year '{Year}' and Branch '{Branch}' already exists.")

        return cleaned_data
    
    def clean(self):
        cleaned_data = super().clean()
        Year = cleaned_data.get("Year")
        Branch = cleaned_data.get("Branch")

        # Get the instance being updated, if any
        instance = self.instance

        # Check if there are other instances with the same Year and Branch
        if templates_obj.objects.filter(Year=Year, Branch=Branch).exclude(id=instance.id).exists():
            raise forms.ValidationError(f"A template for Year '{Year}' and Branch '{Branch}' already exists.")
        
        if Year=="FE" and not(Branch=="ALL"):
            raise forms.ValidationError("Please select FE with ALL only")

        return cleaned_data



      
    


# class SignUpForm(UserCreationForm):
# 	email 		= forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
# 	first_name 	= forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
# 	last_name 	= forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


# 	def __init__(self, *args, **kwargs):
# 		super(SignUpForm, self).__init__(*args, **kwargs)

# 		self.fields['username'].widget.attrs['class'] = 'form-control'
# 		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
# 		self.fields['username'].label = ''
# 		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

# 		self.fields['password1'].widget.attrs['class'] = 'form-control'
# 		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
# 		self.fields['password1'].label = ''
# 		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

# 		self.fields['password2'].widget.attrs['class'] = 'form-control'
# 		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
# 		self.fields['password2'].label = ''
# 		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Record Form
# class AddtemplatesForm(forms.ModelForm):
# 	first_name   =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
# 	last_name    =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
# 	email        =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"type":"email" ,"placeholder":"Email", "class":"form-control"}), label="")
# 	phone        =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
# 	address      =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
# 	city         =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
# 	state        =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
# 	zipcode      =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

# 	class Meta:
# 		model     =  Record
# 		exclude   =  ("user",)