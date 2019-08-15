from flask_restful import fields

AuthInterface = {
    'username':   fields.String,
    'password':   fields.String,
    'uri':    fields.Url
}
