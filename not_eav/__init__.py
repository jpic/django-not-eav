def autodiscover():
    from models import BaseFieldModel

    for field in BaseFieldModel.objects.select_subclasses():
        field.contribute_to_class()
