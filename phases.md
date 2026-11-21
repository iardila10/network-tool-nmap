================================================================================
FASE 1: FRONTEND (Interfaz de Usuario)
================================================================================

+--------------------------------------------------------------------------+

| [ Input: Dirección IP ] ---> [ Botón: Escanear ] |
| |
| [ Tabla de Resultados ] <--- (# Puerto | Estado | Servicio | Versión) |
| [ Tabla de Historial ] <--- (Fecha | IP | Puertos | Ver Detalle) |
+-----------------------------------+--------------------------------------+
|
Peticiones HTTP (JSON / REST)
POST /api/scan | GET /api/reports
v
================================================================================

                            FASE 2: BACKEND (Capa API)

================================================================================
+--------------------------------------------------------------------------+

| 1. ROUTES (Enrutador) |
| * Define los endpoints (/api/scan, /api/reports) |
| | |
| v |
| 2. CONTROLLERS (Controladores) |
| * Valida formato de IP y parámetros de entrada |
| * Devuelve códigos HTTP (200 OK, 400 Error) y respuesta JSON |
+-----------------------------------+--------------------------------------+
|
Llamada interna de funciones
v
================================================================================

                      FASE 3: LÓGICA DE NEGOCIO Y PERSISTENCIA

================================================================================
+-----------------------------------+ +-----------------------------------+

| 3. SERVICE LAYER (Lógica) | | 4. CAPA DE HISTORIAL (Datos) |
| * Ejecuta escaneo de puertos | | * Guarda reporte generado |
| * Detecta estado (Abierto/ | | * Consulta reportes pasados |
| Cerrado/Filtrado) | | |
| * Identifica servicio/versión | | |
+-----------------+-----------------+ +-----------------+-----------------+

                    |                                      |
                    v                                      v
         [ Red / Host Objetivo ]               [ Base de Datos / JSON ]
          (IP a auditar: ej. .1)                (Almacena el historial)

================================================================================

Plan de Desarrollo por Fases (Layout Técnico)

Fase Enfoque Entregables clave Estado / Datos
Fase 1 Frontend (UI) Formulario IP, tabla de resultados y tabla de historial. Usa datos falsos (mock data) en JSON para probar la vista.
Fase 2 Backend (API) Endpoints REST, routes y controllers. Recibe la IP desde el frontend y devuelve respuestas simuladas.
Fase 3 Lógica y Datos Capa services (escaneo real) y base de datos para historial. Ejecuta el análisis real, guarda el reporte y lo consulta.
