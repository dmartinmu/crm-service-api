STATUS_CODES = {
    200: {"type": "ok", "message": ""},
    400: {
        "type": "bad_request",
        "message": "Invalid syntax for this request was provided.",
    },
    401: {
        "type": "unauthorized",
        "message": "You are unauthorized to access the requested resource."
                   "Please log in.",
    },
    403: {
        "type": "forbidden",
        "message": "Your account is not authorized to access the requested"
                   " resource.",
    },
    404: {
        "type": "not_found",
        "message": "We could not find the resource you requested.",
    },
    405: {
        "type": "method_not_allowed",
        "message": "This method type is not currently supported.",
    },
    406: {
        "type": "not_acceptable",
        "message": "The server cannot produce a response matching"
                   " the list of acceptable values defined in the request's"
                   " proactive content negotiation headers. ",
    },
    409: {
        "type": "conflict",
        "message": "The request could not be completed due to a conflict "
                   "with the current state of the resource.",
    },
    422: {
        "type": "unprocessable_entity",
        "message": "The request was well-formed but was unable to be followed"
                   " due to semantic errors.",
    },
    500: {
        "type": "internal_server_error",
        "message": "Unexpected internal server error.",
    },
    501: {
        "type": "not_implemented",
        "message": "The requested resource is recognized but not implemented.",
    },
    502: {
        "type": "bad_gateway",
        "message": "Invalid response received when acting as a proxy"
                   " or gateway.",
    },
    503: {
        "type": "service_unavailable",
        "message": "The server is currently unavailable.",
    },
}
