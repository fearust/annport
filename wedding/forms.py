from django import forms
from wedding.models import Cast


class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = ['bride', 'groom', 'bride_phone', 'groom_phone',
                  'wedding_date', 'wedding_place', 'wedding_reception',
                  'officiator',
                  'email_addr', 'wish_mc', 'customer_memo']
        # staff_memo 및 create_date는 view에서 처리함
