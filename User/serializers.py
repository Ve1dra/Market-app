from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "fullname", "phone", "role", "dob", "address", "bvn", ]

        read_only_fields = ["id", "email"]

        def validate(self, attrs):
            '''attrs is the parameter that holds the all key - value in the field's variable'''
            phone = attrs.get("phone")
            if phone:
                if not phone.startswith('+234'):
                    raise serializers.ValidationError("Phone number must start with +234")
                if len(phone) != 14:
                    raise serializers.ValidationError("Phone number must be exactly 14 characters long")
                try:
                    int(phone[1:])
                except Exception:
                    raise serializers.ValidationError("Phone number must be numbers only")
    
            bvn = attrs.get("bvn")
            if bvn:
                if len(bvn) != 11:
                    raise serializers.ValidationError("BVN number must be exactly 11 characters long")
                try:
                    int(bvn)
                except Exception:
                    raise serializers.ValidationError("BVN number must be numbers only")
            return attrs