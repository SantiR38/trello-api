"""Mixins for models."""

class NamesListingModelMixin:
    """Names listing model mixin.
    ---
    Enables the classmethod `get_names_list()`
    """
    @classmethod
    def get_names_list(cls):
        """Get names list.
        ---
        Shows a list with the names of all the instances.
        """
        qs = cls.objects.all()
        if qs.exists():
            qs = list(map(lambda x: x.name, qs))
            return qs
        return []