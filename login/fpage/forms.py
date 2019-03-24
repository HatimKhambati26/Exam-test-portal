from django import forms
from .models import Detail

# from django.contrib.auth.models import User
FILTER_COURSES = (
    ('IOT', 'IOT'),
    ('Ethical Hacking', 'Ethical Hacking'),
    ('Augmented Reality', 'Augmented Reality'),
    ('Machine Learning', 'Machine Learning'),
)


class DetailsForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    course = forms.ChoiceField(choices=FILTER_COURSES)

    def clean_name(self):
        user_name = self.cleaned_data['name']
        return user_name

    def clean_email(self):
        user_email = self.cleaned_data['email']
        return user_email

    def clean_phone(self):
        user_phone = self.cleaned_data['phone']
        return user_phone

    def clean_course(self):
        user_course = self.cleaned_data['course']
        return user_course

    def clean_score(self):
        user_score = self.cleaned_data['score']
        return user_score

    class Meta:
        model = Detail
        fields = ('name', 'email', 'phone', 'course', 'score',)


class IOTForm(forms.ModelForm):

    CHOICES=[('1','Option 1'),
            ('2','Option 2'),
            ('3','Option 3'),
            ('4','Option 4')]

    q1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q4 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q5 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q7 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def clean_q1(self):
        user_q1 = self.cleaned_data['q1']
        return user_q1
    def clean_q2(self):
        user_q2 = self.cleaned_data['q2']
        return user_q2
    def clean_q3(self):
        user_q3 = self.cleaned_data['q3']
        return user_q3
    def clean_q4(self):
        user_q4 = self.cleaned_data['q4']
        return user_q4
    def clean_q5(self):
        user_q5 = self.cleaned_data['q5']
        return user_q5
    def clean_q6(self):
        user_q6 = self.cleaned_data['q6']
        return user_q6
    def clean_q7(self):
        user_q7 = self.cleaned_data['q7']
        return user_q7
    def clean_q8(self):
        user_q8 = self.cleaned_data['q8']
        return user_q8
    def clean_q9(self):
        user_q9 = self.cleaned_data['q9']
        return user_q9
    def clean_q10(self):
        user_q10 = self.cleaned_data['q10']
        return user_q10

    class Meta:
        model = Detail
        fields = ('score',)


class EHForm(forms.ModelForm):

    CHOICES=[('1','Option 1'),
            ('2','Option 2'),
            ('3','Option 3'),
            ('4','Option 4')]

    q1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q4 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q5 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q7 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def clean_q1(self):
        user_q1 = self.cleaned_data['q1']
        return user_q1
    def clean_q2(self):
        user_q2 = self.cleaned_data['q2']
        return user_q2
    def clean_q3(self):
        user_q3 = self.cleaned_data['q3']
        return user_q3
    def clean_q4(self):
        user_q4 = self.cleaned_data['q4']
        return user_q4
    def clean_q5(self):
        user_q5 = self.cleaned_data['q5']
        return user_q5
    def clean_q6(self):
        user_q6 = self.cleaned_data['q6']
        return user_q6
    def clean_q7(self):
        user_q7 = self.cleaned_data['q7']
        return user_q7
    def clean_q8(self):
        user_q8 = self.cleaned_data['q8']
        return user_q8
    def clean_q9(self):
        user_q9 = self.cleaned_data['q9']
        return user_q9
    def clean_q10(self):
        user_q10 = self.cleaned_data['q10']
        return user_q10

    class Meta:
        model = Detail
        fields = ('score',)


class ARForm(forms.ModelForm):

    CHOICES=[('1','Option 1'),
            ('2','Option 2'),
            ('3','Option 3'),
            ('4','Option 4')]

    q1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q4 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q5 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q7 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def clean_q1(self):
        user_q1 = self.cleaned_data['q1']
        return user_q1
    def clean_q2(self):
        user_q2 = self.cleaned_data['q2']
        return user_q2
    def clean_q3(self):
        user_q3 = self.cleaned_data['q3']
        return user_q3
    def clean_q4(self):
        user_q4 = self.cleaned_data['q4']
        return user_q4
    def clean_q5(self):
        user_q5 = self.cleaned_data['q5']
        return user_q5
    def clean_q6(self):
        user_q6 = self.cleaned_data['q6']
        return user_q6
    def clean_q7(self):
        user_q7 = self.cleaned_data['q7']
        return user_q7
    def clean_q8(self):
        user_q8 = self.cleaned_data['q8']
        return user_q8
    def clean_q9(self):
        user_q9 = self.cleaned_data['q9']
        return user_q9
    def clean_q10(self):
        user_q10 = self.cleaned_data['q10']
        return user_q10

    class Meta:
        model = Detail
        fields = ('score',)


class MLForm(forms.ModelForm):

    CHOICES=[('1','Option 1'),
            ('2','Option 2'),
            ('3','Option 3'),
            ('4','Option 4')]

    q1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q4 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q5 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q7 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def clean_q1(self):
        user_q1 = self.cleaned_data['q1']
        return user_q1
    def clean_q2(self):
        user_q2 = self.cleaned_data['q2']
        return user_q2
    def clean_q3(self):
        user_q3 = self.cleaned_data['q3']
        return user_q3
    def clean_q4(self):
        user_q4 = self.cleaned_data['q4']
        return user_q4
    def clean_q5(self):
        user_q5 = self.cleaned_data['q5']
        return user_q5
    def clean_q6(self):
        user_q6 = self.cleaned_data['q6']
        return user_q6
    def clean_q7(self):
        user_q7 = self.cleaned_data['q7']
        return user_q7
    def clean_q8(self):
        user_q8 = self.cleaned_data['q8']
        return user_q8
    def clean_q9(self):
        user_q9 = self.cleaned_data['q9']
        return user_q9
    def clean_q10(self):
        user_q10 = self.cleaned_data['q10']
        return user_q10

    class Meta:
        model = Detail
        fields = ('score',)
