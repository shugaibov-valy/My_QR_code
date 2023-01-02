from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound
from config import DevConfig as config


app = Sanic("qr_codes-api")


# api info
@app.route("/")
async def info(request):
    return json(
        [
            {
                "title": "Моя машина",
                "description": "у меня очень красивая машина",
                "qrImgUrl": "https://qr_code.ru/my_car",
            },
            {
                "title": "Мой ребёнок",
                "description": "моему ребенку 15 лет",
                "qrImgUrl": "https://qr_code.ru/my_kid",
            },
            {
                "title": "Моя квартира",
                "description": "у меня квартира 40м2",
                "qrImgUrl": "https://qr_code.ru/my_home",
            },
            {
                "title": "Мой кошелёк",
                "description": "Небольшой полый или плоский предмет, чаще всего из кожи или ткани, предназначенный для ношения денег. Часто называлось также портмоне.",
                "qrImgUrl": "https://qr_code.ru/my_wallet",
            },
        ]
    )


@app.exception(NotFound)
def ignore_404s(request, exception):
    return json({"error": "not found"}, status=404)
