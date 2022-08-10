from flask import redirect
from flask.views import MethodView
from flask_smorest import abort, Blueprint


from app.context import url_service
from app.shcema.url import ShortUrlSchema, UrlSchema, UrlRedirectSchema, UrlShortenerSchema
from app.exc import NotFoundUrl

blp = Blueprint("url", __name__, description="Operations on url")


@blp.route('/')
class Url(MethodView):
    @blp.response(
        200, 
        UrlSchema(many=True), 
        example={
            "source_url": "https://naver.com",
            "id": 1,
            "short_id": "dddddL",
        }
        
    )
    def get(self):
        datas = url_service.get_all()
        return datas


@blp.route('/<string:short_id>')
class Redirect(MethodView):
    @blp.arguments(schema=UrlRedirectSchema, location="path", as_kwargs=True)
    @blp.response(301)
    def get(self, **path_parameter):
        """/short_id

        단축 Url의 원래 페이지로 이동
        ---
        """
        short_id = path_parameter['short_id']
        try:
            source_url = url_service.get_source_url(short_id)
        except NotFoundUrl:
            abort(400)
        return redirect(source_url)


@blp.route('/shorten/')
class Shortener(MethodView):
    @blp.arguments(UrlShortenerSchema, example={"url": "https://naver.com"})
    @blp.response(200, ShortUrlSchema, example={"url": "https://shortener.com/dddddL"})
    def post(sel, url_data):
        """/shorten/

        단축 url 생성
        ---
        """
        url = url_data["url"]
        short_url = url_service.shorten(url)
        return {"short_url": short_url}
