from rest_framework import serializers

from authentication.models import ACCOUNT_TYPES


class SignupSerializer(serializers.Serializer):

    '''Declear all the fields'''

    email = serializers.EmailField()
    fullname = serializers.CharField(max_length=255)
    phone = serializers.CharField()
    address = serializers.CharField()
    role = serializers.ChoiceField(choices=[x[0] for x in ACCOUNT_TYPES])
    bvn = serializers.CharField()
    password = serializers.CharField()
    dob = serializers.DateField()
    # class Meta:
    #     model = User
    #     fields = ["email", "fullname", "phone", "bvn"
    #               , "dob","is_staff","is_superuser"
    #               ]

    '''Validate all the fields
        Email is already being validated by EmailField
    
    '''
    
    def validate(self, attrs):
        '''attrs is the parameter that holds the all key - value in the field's variable'''
        phone = attrs["phone"]
        if not phone.startswith('+234'):
            raise serializers.ValidationError("Phone number must start with +234")
        if len(phone) != 14:
            raise serializers.ValidationError("Phone number must be exactly 14 characters long")
        try:
            int(phone[1:])
        except:  # noqa: BLE001
            raise serializers.ValidationError("Phone number must be numbers only")

        bvn = attrs["bvn"]
        if len(bvn) != 11:
            raise serializers.ValidationError("BVN number must be exactly 11 characters long")
        try:
            int(bvn[1:])
        except Exception:  # noqa: BLE001
            raise serializers.ValidationError("BVN number must be numbers only")

        password = attrs["password"]
        if len(password) < 8:
            raise serializers.ValidationError("Password must be exactly 8 characters long")

        return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    # def validated_data(self, attrs):
    #     email = attrs["email"]
    #     password = attrs["password"]