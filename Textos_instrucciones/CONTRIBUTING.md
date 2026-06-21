# 👥 Guía de Contribución

## 🔄 Flujo de Trabajo

### Opción 1: Git Simple (Recomendado para equipos pequeños)

1. **Actualizar rama main**
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Crear rama de feature**
   ```bash
   git checkout -b feature/nombre-descriptivo
   ```

3. **Hacer cambios y commits**
   ```bash
   git add .
   git commit -m "type: descripción"
   ```

4. **Tipos de commits permitidos:**
   - `feat`: Nueva funcionalidad
   - `fix`: Corrección de errores
   - `docs`: Cambios en documentación
   - `refactor`: Refactorización de código
   - `test`: Agregar o actualizar tests

5. **Hacer push**
   ```bash
   git push origin feature/nombre-descriptivo
   ```

6. **Crear Pull Request**
   - Describir qué se cambió
   - Mencionar si hay breaking changes
   - Esperar revisión del equipo

---

### Opción 2: Git Flow (Recomendado para equipos grandes - 3+ desarrolladores)

Para un flujo de trabajo más robusto con ramas de feature, release y hotfix:

→ **[Ver GITFLOW.md](GITFLOW.md)** para instrucciones completas

Git Flow es ideal cuando:
- Tienes 3+ desarrolladores trabajando simultáneamente
- Necesitas versiones y releases planificadas
- Quieres hotfixes separados de features normales
- Trabajas con CI/CD y testing automated

## 📋 Convenciones de Código

### Nombres de archivos y carpetas
- Usar `snake_case`: `usuarios_bp.py`, `config_settings.py`
- Archivos de blueprints: `entidad_bp.py`
- Modelos: `entidad.py`

### Nombres de variables y funciones
- Usar `snake_case`: `get_usuarios()`, `user_data`
- Nombres descriptivos: `fecha_creacion` no `fc`

### Estructura de blueprints
```python
from flask import Blueprint, request
from app.database.database import db
from app.models.ejemplo import Ejemplo
from app.utils.response import response_success, response_error

ejemplo_bp = Blueprint('ejemplo', __name__, url_prefix='/api/ejemplo')

# GET
@ejemplo_bp.route('', methods=['GET'])
def get_ejemplos():
    try:
        # lógica
        return response_success(data, "mensaje")
    except Exception as e:
        return response_error(str(e), 500)

# POST
@ejemplo_bp.route('', methods=['POST'])
def create_ejemplo():
    try:
        data = request.get_json()
        if not data:
            return response_error("El body debe ser un JSON válido", 400)
        # validar y crear
        return response_success(data, "mensaje", 201)
    except Exception as e:
        return response_error(str(e), 500)
```

## ✅ Antes de hacer Push

- [ ] El código funciona sin errores
- [ ] No hay archivos innecesarios (logs, __pycache__, etc.)
- [ ] Se respetan las convenciones de código
- [ ] Se actualizó README.md si es necesario
- [ ] Se hizo commit descriptivo

## 🔄 Resolver Conflictos

```bash
# Si hay conflictos al hacer pull
git pull origin main

# Resolver conflictos en los archivos
# Luego:
git add .
git commit -m "resolve: merge conflicts"
git push origin feature/nombre
```

## 📚 Recursos

- [Documentación Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/)
- [Git Basics](https://git-scm.com/book/en/v2)

---

**Gracias por contribuir a RentStyle! 🎉**
