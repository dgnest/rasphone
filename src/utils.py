from wtforms import validators


class NumericValidator(object):

    error_message1 = 'Must be %d digits long.'
    error_message2 = 'Must be a number'

    @classmethod
    def fixed_digits(self, digits):

        def _fixed_digits(form, field):
            if len(str(field.data)) != digits:
                raise validators.ValidationError(
                    self.error_message1 % digits
                )
            if isinstance(field.data, (str, unicode)):
                raise validators.ValidationError(self.error_message2)
        return _fixed_digits

    @classmethod
    def numeric(self):

        def _numeric(form, field):
            if isinstance(field.data, (str, unicode)):
                raise validators.ValidationError(self.error_message2)
        return _numeric
