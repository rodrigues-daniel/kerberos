import django_python3_ldap.utils.clean_user_data

def clean_user_data(model_fields):
    """
    Transforms the user data loaded from
    LDAP into a form suitable for creating a user.
    """
    # Call the default handler.
    model_fields = django_python3_ldap.utils.clean_user_data(model_fields)
    # Add our own data in.
    model_fields["is_staff"] = True
    model_fields["is_superuser"] = False 
return model_fields
