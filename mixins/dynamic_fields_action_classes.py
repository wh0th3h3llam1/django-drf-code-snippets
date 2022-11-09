
from typing import Dict, Iterator


class DynamicFieldsActionClassMixin:
    """
    A class which inhertis this mixin should have attribute
	`dynamic_fields_action_classes`.
    """
    # https://stackoverflow.com/questions/37061718/django-rest-framework-hide-specific-fields-in-list-display
    # https://github.com/gregschmit/drf-action-serializer/blob/master/action_serializer/serializers.py
    # https://gist.github.com/Alexx-G/f2983664fd6565a9bb8f
    dynamic_fields_action_classes: Dict[str, Iterator]
    
    def get_serializer(self, *args, **kwargs):
        try:
            fields = self.dynamic_fields_action_classes[self.action]["fields"] or []
            exclude = self.dynamic_fields_action_classes[self.action]["exclude"] or []
            read_only_fields = self.dynamic_fields_action_classes[self.action]["read_only_fields"] or []

            if fields:
                kwargs["fields"] = fields
            elif exclude:
                kwargs["exclude"] = exclude
            
            if read_only_fields:
                kwargs["read_only_fields"] = read_only_fields
        except (KeyError, AttributeError):
            pass
        finally:
            return super().get_serializer(*args, **kwargs)
