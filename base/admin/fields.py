def get_admin_fields(admin_class):
    fields = []
    admin_fields = admin_class.fields
    if type(admin_fields) is tuple:
        for field_set in admin_fields:
            if type(field_set) is tuple:
                for f in field_set:
                    fields.append(f)
            else:
                fields.append(field_set)
    return fields
