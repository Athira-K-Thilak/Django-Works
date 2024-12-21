from django import forms

class RegistrationForm(forms.Form):

    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control mb-2'}))

    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2'}))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2'}))
    

class VehicleForm(forms.Form):

    name=forms.CharField()

    running_type=forms.IntegerField()

    OWNER_CHOICES=[
        ("first","first"),
        ("second","second"),
        ("third","third")
    ]

    owner_type=forms.ChoiceField(choices=OWNER_CHOICES)

    price=forms.IntegerField()

    FUEL_CHOICES=[
        ("petrol","petrol"),
        ("diesel","diesel"),
        ("cng","cng"),
        ("Electric","Electric")
    ]

    fuel_type=forms.ChoiceField(choices=FUEL_CHOICES)

    ROLE_CHOICES=[
        ("admin","admin"),
        ("staff","staff")
    ]

    role=forms.ChoiceField(choices=ROLE_CHOICES,widget=forms.Select(attrs={'class':'form-control form-select'}))


class BmrForm(forms.Form):

    weight=forms.FloatField()
    height=forms.IntegerField()
    age=forms.IntegerField()
    GENDER_CHOICES=[
        ("Please Select","Please Select"),
        ("Female","Female"),
        ("Male","Male"),
        ("Other","Other")
    ]
    gender=forms.ChoiceField(choices=GENDER_CHOICES)
    ACTIVITY_CHOICE=[
        ("Please Select","Please Select"),
        ("active","active"),
        ("very active","very active"),
        ("moderatly active","moderatly active"),
        ("not active","not active")
    ]
    Activity_Level=forms.ChoiceField(choices=ACTIVITY_CHOICE)


class AppointmentForm(forms.Form):

    full_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    contact_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control mb-2'}))
    email_address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    street_address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    street_address_line2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    city=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    state=forms.CharField (widget=forms.TextInput(attrs={'class':'form-control mb-2'}))
    ZipCode=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control mb-2'}))
    date=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control mb-2'}))


#bmi
class BmiForm(forms.Form):
    weight=forms.IntegerField()
    height=forms.IntegerField()

#milage
# 
class MilageForm(forms.Form):
    distance=forms.IntegerField()
    consumption=forms.IntegerField()    

#calrie form
class CalorieForm(forms.Form):
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control mb-3'}))

    height=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control mb-3'}))

    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control mb-3'}))

    GENDER_CHOICES=(
        ('male','MALE'),
        ('female','FEMALE')
    )   

    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.Select(attrs={'class':'form-control form-select'}))

    ACTIVITY_CHOICES=(
        (1.2,'SEDENTARY'),
        (1.375,'LIGHTLY ACTIVE'),
        (1.55,'MODERATLY ACTIVE'),
        (1.725,'VERY ACTIVE'),
        (1.9,'EXTRA ACTIVE')
    )

    activity=forms.ChoiceField(choices=ACTIVITY_CHOICES,widget=forms.Select(attrs={'class':'form-control form-select'}))
















