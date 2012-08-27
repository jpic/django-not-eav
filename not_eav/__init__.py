def autodiscover():
    from models import Attribute

    for attribute in Attribute.objects.all():
        attribute.contribute_to_class()
