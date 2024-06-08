from cerberus import Validator

resume_schema = {
    'resume_text': {'type': 'string', 'required': True}
}

analysis_schema = {
    'contact_info': {'type': 'dict'},
    'education': {'type': 'list', 'schema': {'type': 'string'}},
    'experience': {'type': 'list', 'schema': {'type': 'string'}},
    'skills': {'type': 'list', 'schema': {'type': 'string'}}
}

v = Validator()
