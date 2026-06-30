from app import create_app
from app.models.prenda import Prenda
from app.models.prenda_imagen import PrendaImagen
app = create_app()
with app.app_context():
    prendas = Prenda.query.all()
    print('PRNDA_ROWS')
    for p in prendas:
        print(p.idPrenda, getattr(p, 'image_urls', None))
    images = PrendaImagen.query.all()
    print('IMAGES_ROWS')
    for img in images:
        print(img.idImagen, img.idPrenda, img.filename, img.created_at)
