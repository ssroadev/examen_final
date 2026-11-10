# Instrucciones para Subir el Proyecto a GitHub

## Paso 1: Crear un repositorio en GitHub

1. Ve a [GitHub](https://github.com)
2. Haz clic en el botón **"New"** o **"+"** en la esquina superior derecha
3. Selecciona **"New repository"**
4. Completa la información:
   - **Repository name**: `parcial_logica` (o el nombre que prefieras)
   - **Description**: "Programa comparador de algoritmos de ordenamiento en Python"
   - **Public/Private**: Elige según tu preferencia
   - ⚠️ **NO marques** "Initialize this repository with a README" (ya tenemos uno)
5. Haz clic en **"Create repository"**

## Paso 2: Conectar el repositorio local con GitHub

Después de crear el repositorio, GitHub te mostrará varias opciones. Usa la opción **"push an existing repository from the command line"**.

Ejecuta estos comandos en tu terminal (PowerShell) desde la carpeta del proyecto:

```powershell
# Añadir el repositorio remoto (reemplaza TU_USUARIO con tu nombre de usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/parcial_logica.git

# Verificar que se agregó correctamente
git remote -v

# Renombrar la rama a main (opcional, si GitHub usa 'main' como predeterminado)
git branch -M main

# Subir los cambios a GitHub
git push -u origin main
```

## Paso 3: Verificar la subida

1. Refresca la página de tu repositorio en GitHub
2. Deberías ver todos los archivos:
   - `ordenamiento.py`
   - `README.md`
   - `.gitignore`
   - `test_ordenamiento.py`
   - `INSTRUCCIONES_GITHUB.md`

## Paso 4: Copiar el enlace del repositorio

Una vez subido, el enlace de tu repositorio será:
```
https://github.com/TU_USUARIO/parcial_logica
```

Copia este enlace y súbelo en la plataforma de tu curso.

---

## Solución de Problemas Comunes

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/parcial_logica.git
```

### Error: "authentication failed"
Puede que necesites usar un token de acceso personal en lugar de tu contraseña:
1. Ve a GitHub → Settings → Developer settings → Personal access tokens
2. Genera un nuevo token con permisos de "repo"
3. Usa el token como contraseña cuando te lo pida

### Usar SSH en lugar de HTTPS (opcional)
```powershell
git remote add origin git@github.com:TU_USUARIO/parcial_logica.git
```

---

## Comandos Git Útiles

```powershell
# Ver el estado del repositorio
git status

# Ver el historial de commits
git log --oneline

# Ver las diferencias antes de hacer commit
git diff

# Añadir todos los cambios
git add .

# Hacer commit con mensaje
git commit -m "Descripción de los cambios"

# Subir cambios a GitHub
git push
```

---

## Contenido del Proyecto

✅ **ordenamiento.py** - Programa principal con:
- Generación de lista aleatoria
- Ordenamiento Burbuja
- Ordenamiento por Inserción
- Menú interactivo
- Comparación de iteraciones

✅ **README.md** - Documentación del proyecto

✅ **test_ordenamiento.py** - Script de pruebas automatizado

✅ **.gitignore** - Archivos a ignorar por Git

---

## Estructura del Repositorio

```
parcial_logica/
├── .gitignore
├── README.md
├── INSTRUCCIONES_GITHUB.md
├── ordenamiento.py
└── test_ordenamiento.py
```

---

¡Listo! Tu proyecto está preparado para ser subido a GitHub. 🚀
