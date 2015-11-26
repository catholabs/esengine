from es_engine.fields import StringField
from es_engine.bases.field import BaseField


class ModelMetaclass(type):

    def __new__(mcls, name, bases, attrs):  # noqa
        attrs['_fields'] = {}
        for base in bases:
            if hasattr(base, '__autoid__'):
                if base.__autoid__ and not 'id' in attrs:
                    attrs['id'] = StringField()
                break
        for key, value in attrs.iteritems():
            if isinstance(value, BaseField):
                attrs['_fields'][key] = value
        cls = type.__new__(mcls, name, bases, attrs)
        if any(x.__name__ == 'EmbeddedDocument' for x in bases):
            cls.__type__ = cls
        return cls
