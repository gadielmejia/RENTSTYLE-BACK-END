# 🚀 Guía de Configuración Inicial

## Pasos para que el equipo pueda trabajar correctamente

### 1️⃣ Después de clonar el repositorio

```bash
# Navegar a la carpeta
cd RENTSTYLE-BACK-END

# Crear ambiente virtual
python -m venv venv

# Activar ambiente virtual
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Configurar la base de datos

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tus credenciales de MySQL
# Cambiar: MYSQL_USER, MYSQL_PASSWORD, etc.
```

### 4️⃣ Crear la base de datos MySQL

```bash
mysql -u root -p

# En la consola de MySQL:
CREATE DATABASE rentstyle CHARACTER SET utf8mb4;
EXIT;
```

### 5️⃣ Ejecutar migraciones

```bash
# Generar migraciones (si hay cambios en modelos)
flask --app run db migrate -m "Descripción del cambio"

# Aplicar migraciones
flask --app run db upgrade
```

### 6️⃣ Iniciar el servidor

```bash
flask --app run run

# El servidor estará en: http://127.0.0.1:5000
```

## ✅ Checklist

- [ ] Ambiente virtual creado y activado
- [ ] Dependencias instaladas
- [ ] `.env` configurado con credenciales MySQL
- [ ] Base de datos creada
- [ ] Migraciones ejecutadas
- [ ] Servidor ejecutándose sin errores

## 🔑 Puntos Importantes

1. **NO subir** `venv/`, `__pycache__/`, `.env` a Git
2. **Siempre trabajar con el ambiente virtual activado**
3. **Crear rama nueva para cada feature**
4. **Hacer pull antes de empezar a trabajar**
5. **Hacer push regularmente**

## 📝 Comandos Git útiles

```bash
# Crear rama para nueva feature
git checkout -b feature/mi-funcionalidad

# Ver cambios
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "feat: descripción clara del cambio"

# Enviar cambios
git push origin feature/mi-funcionalidad

# Actualizar rama actual
git pull origin main
```

## 🆘 Si algo falla

### Error: "ModuleNotFoundError: No module named 'flask'"
- Verifica que el ambiente virtual esté **activado**
- Ejecuta `pip install -r requirements.txt` de nuevo

### Error: "Can't connect to MySQL"
- Verifica que MySQL esté corriendo
- Comprueba las credenciales en `.env`
- Verifica que la base de datos exista

### Error al ejecutar migraciones
```bash
# Eliminar carpeta migrations (solo si es la primera vez)
rm -rf migrations

# Crear migraciones de nuevo
flask --app run db init
flask --app run db migrate -m "Initial migration"
flask --app run db upgrade
```

## 📞 Contacto

Para preguntas, contacta con el equipo de desarrollo.
