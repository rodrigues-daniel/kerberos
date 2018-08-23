from django._python3_ldap import utils

def clean_user_data(model_fields):
    """
    Transforms the user data loaded from
    LDAP into a form suitable for creating a user.
    """
    # Call the default handler.
    model_fields = utils.clean_user_data(model_fields)
    # Add our own data in.
    model_fields["is_staff"] = True
    model_fields["is_superuser"] = False 
    return model_fields


def  menssagem():
        print("ola mundo")
