import random
import string
import base64

def generar_nombre_aleatorio(longitud=8):
    # Genera un nombre aleatorio que empieza por guion bajo para despistar
    letras = string.ascii_letters
    return "_" + "".join(random.choice(letras) for _ in range(longitud))

def cifrar_xor(texto, clave=5):
    # Cifra caracteres individuales mediante XOR básico
    return "".join(chr(ord(c) ^ clave) for c in texto)

def ofuscar_codigo_lua(codigo_fuente):
    clave_xor = random.randint(2, 20)
    
    # Cabecera de desencriptación en tiempo de ejecución para Lua
    stub_desencriptacion = f"""
-- [Ofuscado por Vangeliicide Protection]
local function _dec(s)
    local r = ""
    for i = 1, #s do
        r = r .. string.char(string.byte(s, i) ~ {clave_xor})
    end
    return r
end
"""
    
    # Limpiar líneas vacías y comentarios básicos
    lineas = codigo_fuente.split('\n')
    lineas_limpias = []
    
    for linea in lineas:
        linea_str = linea.strip()
        if linea_str.startswith('--') or not linea_str:
            continue
        lineas_limpias.append(linea)
        
    codigo_procesado = "\n".join(lineas_limpias)
    
    # Sustitución simple de cadenas entre comillas para encriptarlas
    import re
    def reemplazar_string(match):
        texto_original = match.group(1)
        texto_cifrado = cifrar_xor(texto_original, clave_xor)
        # Convertir a bytes/hex visual para que no se lea en texto plano
        hex_encoded = "".join(f"\\x{ord(c):02x}" for c in texto_cifrado)
        return f"_dec(\"{hex_encoded}\")"
        
    codigo_ofuscado = re.sub(r'"([^"\\]*(?:\\.[^"\\]*)*)"', reemplazar_string, codigo_procesado)
    
    resultado_final = stub_desencriptacion + "\n" + codigo_ofuscado
    return resultado_final

# ==========================================
# EJEMPLO DE USO:
# ==========================================
if __name__ == "__main__":
    codigo_lua_original = """
    -- Script de prueba para Roblox Luau
    local mensaje = "Hola mundo desde Roblox"
    print(mensaje)
    
    local function saludar(nombre)
        print("Bienvenido " .. nombre)
    end
    
    saludar("SylentAsura")
    """

    print("--- CÓDIGO OFUSCADO ---")
    print(ofuscar_codigo_lua(codigo_lua_original))
