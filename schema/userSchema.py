from ../model import user

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'firstName')

