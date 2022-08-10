from marshmallow import Schema, fields


class UrlSchema(Schema):
    id = fields.Int(dump_only=True)
    short_id = fields.Str(required=True)
    source_url = fields.Str(required=True)


class UrlRedirectSchema(Schema):
    short_id = fields.Str(required=True)


class UrlShortenerSchema(Schema):
    url = fields.Str(required=True)


class ShortUrlSchema(Schema):
    short_url = fields.Str(required=True)