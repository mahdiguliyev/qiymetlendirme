from django import forms
from .models import EvaluationOrder,Apartment,PrivateHouse,EnterpriseComplex,NonResidentialArea,NonResidentialBuilding,LandPlot,OtherRealState

class EvaluationOrderForm(forms.ModelForm):

    class Meta:
        model = EvaluationOrder
        fields = '__all__'

class Apartment(forms.ModelForm):

    class Meta:
        model = Apartment
        fields = '__all__'

class PrivateHouse(forms.ModelForm):

    class Meta:
        model = PrivateHouse
        fields = '__all__'

class EnterpriseComplex(forms.ModelForm):

    class Meta:
        model = EnterpriseComplex
        fields = '__all__'

class NonResidentialArea(forms.ModelForm):

    class Meta:
        model = NonResidentialArea
        fields = '__all__'

class NonResidentialBuilding(forms.ModelForm):

    class Meta:
        model = NonResidentialBuilding
        fields = '__all__'

class LandPlot(forms.ModelForm):

    class Meta:
        model = LandPlot
        fields = '__all__'

class OtherRealState(forms.ModelForm):

    class Meta:
        model = OtherRealState
        fields = '__all__'