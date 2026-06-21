# 🗺️ Roadmap del Proyecto

## ✅ Fase 1: Base (Completada)

### Configuración del Proyecto
- [x] Estructura de carpetas
- [x] Configuración de Flask
- [x] Conexión a MySQL
- [x] Variables de entorno (.env)
- [x] Migraciones de base de datos

### Modelos (SQLAlchemy)
- [x] Roles
- [x] Usuarios
- [x] Categoría
- [x] Prenda
- [x] Inventario
- [x] Reserva
- [x] Detalle_Reserva
- [x] Comprobante
- [x] Cita

### Blueprints CRUD
- [x] Roles (GET, POST, PUT, DELETE)
- [x] Usuarios (GET, POST, PUT, DELETE)
- [x] Categorías (GET, POST, PUT, DELETE)
- [x] Prendas (GET, POST, PUT, DELETE)
- [x] Inventario (GET, POST, PUT, DELETE)
- [x] Reservas (GET, POST, PUT, DELETE)

### Utilidades
- [x] Funciones de respuesta JSON estándar
- [x] Serialización de modelos
- [x] Manejo de errores

### Documentación
- [x] README.md
- [x] SETUP.md
- [x] CONTRIBUTING.md
- [x] .gitignore
- [x] .env.example

---

## 🔄 Fase 2: Funcionalidades Avanzadas (Próximas)

### Autenticación & Autorización
- [ ] Sistema de login con JWT
- [ ] Hash de contraseñas (Werkzeug)
- [ ] Verificación de roles
- [ ] Middleware de autenticación

### Búsqueda y Filtros
- [ ] Filtrar prendas por categoría
- [ ] Búsqueda por nombre/descripción
- [ ] Ordenamiento (fecha, precio)
- [ ] Paginación

### Validaciones Avanzadas
- [ ] Email válido
- [ ] Teléfono válido
- [ ] Fechas lógicas en reservas
- [ ] Validación de documentos (DNI)

### Blueprints Adicionales
- [ ] Comprobante (CRUD completo)
- [ ] Cita (CRUD completo)
- [ ] Detalle_Reserva (CRUD completo)

### Reportes y Estadísticas
- [ ] Reservas por período
- [ ] Ingresos por categoría
- [ ] Disponibilidad de prendas
- [ ] Clientes frecuentes

---

## 🔐 Fase 3: Seguridad y Optimización

### Seguridad
- [ ] Rate limiting
- [ ] CORS configurado
- [ ] Validación de input (SQL injection)
- [ ] Logging de acciones

### Optimización
- [ ] Cache de consultas frecuentes
- [ ] Índices en la BD
- [ ] Lazy loading de relaciones
- [ ] Paginación de resultados

### Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Test de cobertura

---

## 📱 Fase 4: Frontend (Integración)

### Documentación API
- [ ] Swagger/OpenAPI
- [ ] Postman collection

### Endpoints Especializados
- [ ] Dashboard de admin
- [ ] Panel de cliente
- [ ] Historial de reservas
- [ ] Calificaciones/Reviews

---

## 📊 Estado Actual: 35% Completado

```
Fase 1: ████████████████████░░░░░░░░ 70%
Fase 2: ░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%
Fase 3: ░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%
Fase 4: ░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%
```

---

## 👥 Tareas por Hacer (Corto Plazo)

1. **Fase 2.1**: Implementar autenticación JWT
2. **Fase 2.2**: Agregar búsqueda y filtros
3. **Fase 3.1**: Escribir tests unitarios
4. **Documentación**: Crear Swagger

---

## 📝 Notas

- El proyecto está listo para que el equipo lo clone y comience a trabajar
- Las Fases 2-4 pueden hacerse en paralelo con diferentes miembros del equipo
- Mantener comunicación en el equipo para evitar conflictos de merge

---

**Última actualización: 20 de Junio 2026**
