from collections import defaultdict

from . import status_codes as sc


class APIException(Exception):
    def __init__(self, status_code, message=None, errors=None,
                 error_code=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.errors = errors
        self.error_code = error_code

    def to_dict(self):
        error = {
            "error": {
                "message": self.message
                if self.message
                else sc.STATUS_CODES[self.status_code]["message"],
                "type": sc.STATUS_CODES[self.status_code]["type"],
                "code": self.status_code,
                "errors": self.errors if self.errors else [],
                "error_code": self.error_code,
            }
        }
        return error


class CerberusException(APIException):
    def __init__(self, validator):
        errors_codes = defaultdict(dict)
        informational_errors_found = False
        for error in validator._errors:
            if not isinstance(error.code, int) and len(str(error.code)) > 1:
                code = int(str(error.code)[:1])
            else:
                code = error.code
            if code < 5:
                errors_codes["syntax"][error.document_path[0]] = validator.\
                    errors[
                        error.document_path[0]
                    ]
                informational_errors_found = True
            elif (
                code == 97
                and error.is_normalization_error
                and not informational_errors_found
            ):
                # Se ignoran los error de normalizacion ya que
                # van aparecer en la validacion del esquema
                errors_codes["coerce"][error.document_path[0]] = \
                    validator.errors[
                        error.document_path[0]
                    ]
            else:
                errors_codes["semantic"][error.document_path[0]] = \
                    validator.errors[
                    error.document_path[0]
                ]
                informational_errors_found = True

        if "syntax" in errors_codes:
            self.status_code = 400
            APIException.__init__(self, self.status_code,
                                  errors=errors_codes["syntax"])
        elif "semantic" in errors_codes:
            self.status_code = 422
            APIException.__init__(
                self, self.status_code, errors=errors_codes["semantic"]
            )
        else:
            self.status_code = 422
            APIException.__init__(self, self.status_code,
                                  errors=errors_codes["coerce"])


class ResourceNotFoundException(APIException):
    def __init__(self, message=None, errors=None):
        self.status_code = 404
        APIException.__init__(self, self.status_code, message, errors)
