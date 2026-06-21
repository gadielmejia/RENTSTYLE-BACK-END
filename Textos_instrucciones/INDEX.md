# 📑 Índice de Documentación

Bienvenido al proyecto **RentStyle Backend API**. Aquí encontrarás toda la documentación necesaria.

## 🚀 Comenzar Rápidamente

**Si es tu primera vez en este proyecto:**

1. Abre [SETUP.md](SETUP.md) - Instrucciones paso a paso de configuración
2. Alterna entre [README.md](README.md) para ver los endpoints disponibles

**Atajo rápido (Windows):**
```bash
./setup.bat
```

**Atajo rápido (macOS/Linux):**
```bash
chmod +x setup.sh
./setup.sh
```

---

## 📚 Documentos Principales

| Documento | Propósito | Para quién |
|-----------|-----------|-----------|
| [README.md](README.md) | Documentación completa del API | Desarrolladores, QA |
| [SETUP.md](SETUP.md) | Instalación y configuración inicial | Nuevos miembros del equipo |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Convenciones de código y flujo Git | Desarrolladores |
| [ROADMAP.md](ROADMAP.md) | Plan de desarrollo y próximas fases | Project Manager, Desarrolladores |
| [TESTING.md](TESTING.md) | Guía de testing y QA | QA, Desarrolladores |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Convenciones de código | Desarrolladores |
| [GITFLOW.md](GITFLOW.md) | Git Flow avanzado para equipos | Líderes técnicos |
| [CHECKLIST.md](CHECKLIST.md) | Verificación antes de commits | Todos |

---

## 🏗️ Estructura del Proyecto

```
RENTSTYLE-BACK-END/
├── 📄 README.md                 # Documentación principal
├── 📄 SETUP.md                  # Guía de instalación
├── 📄 CONTRIBUTING.md           # Convenciones de código
├── 📄 ROADMAP.md                # Plan de desarrollo
├── 📄 TESTING.md                # Guía de testing
├── 📄 CHECKLIST.md              # Checklist final
├── 📄 INDEX.md                  # Este archivo
│
├── 🔧 Configuración
│   ├── .env.example             # Variables de entorno (plantilla)
│   ├── requirements.txt         # Dependencias Python
│   ├── setup.bat                # Instalación automática (Windows)
│   └── setup.sh                 # Instalación automática (Linux/Mac)
│
├── 📦 app/                      # Aplicación principal
│   ├── __init__.py              # Factory de la app
│   │
│   ├── 🗄️ config/
│   │   └── settings.py          # Configuración de DB
│   │
│   ├── 🗄️ database/
│   │   └── database.py          # Instancia de SQLAlchemy
│   │
│   ├── 🗄️ models/              # Modelos de datos
│   │   ├── roles.py
│   │   ├── usuarios.py
│   │   ├── categoria.py
│   │   ├── prenda.py
│   │   ├── inventario.py
│   │   ├── reserva.py
│   │   ├── detalle_reserva.py
│   │   ├── comprobante.py
│   │   ├── cita.py
│   │   └── __init__.py
│   │
│   ├── 🛣️ routes/              # Blueprints API
│   │   ├── home_bp.py
│   │   ├── roles_bp.py
│   │   ├── usuarios_bp.py
│   │   ├── categorias_bp.py
│   │   ├── prendas_bp.py
│   │   ├── inventario_bp.py
│   │   ├── reservas_bp.py
│   │   └── __init__.py
│   │
│   ├── 🔧 middlewares/          # Middlewares (futuro)
│   ├── 🔧 controllers/          # Controllers (futuro)
│   ├── 🔧 services/             # Services (futuro)
│   │
│   └── ⚙️ utils/
│       ├── response.py          # Funciones de respuesta JSON
│       └── __init__.py
│
├── 🧪 migrations/               # Migraciones de BD (autogenerado)
│
└── 🚀 run.py                    # Script para iniciar servidor
```

---

## 🔗 Navegación Rápida

### Para Comenzar
- [→ SETUP.md](SETUP.md) - Cómo instalar y configurar

### Para Desarrollar
- [→ README.md](README.md) - Endpoints y ejemplos de uso
- [→ CONTRIBUTING.md](CONTRIBUTING.md) - Cómo contribuir código

### Para Preparar Features
- [→ ROADMAP.md](ROADMAP.md) - Qué sigue en el roadmap

### Para Testing
- [→ TESTING.md](TESTING.md) - Cómo escribir y ejecutar tests

### Antes de Hacer Push
- [→ CHECKLIST.md](CHECKLIST.md) - Verificar que todo esté listo

---

## ❓ Preguntas Frecuentes

### "¿Por dónde empiezo?"
→ Ve a [SETUP.md](SETUP.md) y sigue los pasos 1-6.

### "¿Cómo uso el API?"
→ Mira los ejemplos en [README.md](README.md#-endpoints).

### "¿Qué debo hacer antes de hacer commit?"
→ Revisa [CONTRIBUTING.md](CONTRIBUTING.md) y [CHECKLIST.md](CHECKLIST.md).

### "¿Cuáles son las próximas features?"
→ Consulta [ROADMAP.md](ROADMAP.md).

### "¿Cómo escribo un test?"
→ Sigue la guía en [TESTING.md](TESTING.md).

### "¿Mi error no está documentado?"
→ Busca en [README.md](README.md#-troubleshooting) o en [TESTING.md](TESTING.md#-si-algo-falla).

---

## 🤝 Soporte

- **Problemas de setup**: [SETUP.md](SETUP.md#-si-algo-falla)
- **Dudas de código**: [CONTRIBUTING.md](CONTRIBUTING.md#-estructura-de-blueprints)
- **Troubleshooting general**: [README.md](README.md#-troubleshooting)

---

## 📊 Progreso del Proyecto

```
✅ Fase 1: Base (70%) - En Progreso
🔄 Fase 2: Funcionalidades Avanzadas (0%) - Próxima
⏳ Fase 3: Seguridad (0%) - Futura
⏳ Fase 4: Frontend (0%) - Futura
```

Más detalles en [ROADMAP.md](ROADMAP.md).

---

## 📝 Última Actualización

- **Fecha**: Junio 2026
- **Versión del API**: 1.0.0
- **Versión de Python**: 3.8+
- **Versión de Flask**: 3.x

---

## 📖 Recursos Externos

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Git Guide](https://git-scm.com/docs)

---

**¡Bienvenido a RentStyle! Estamos felices de tenerte en el equipo. 🎉**
