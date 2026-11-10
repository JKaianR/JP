from sqlalchemy import create_engine, column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker

#Configuracion 

base = declarative_base()
engine = create_engine("sqlite: ///personas.db", echo=True)
Ssesion = sessionmaker(bind= engine)
ssesion = Ssesion()

#Modelo

class Persona ( base):
    __tablename__= "personas"
    id = column (Integer, primary_key = True)
    nombre = column (String)
    edad = column (Integer)
    
#Crea la tabla si no exite

base.metadata.create_all(engine)

#Funcion Basica "Text-To_SQL"
def interpretar_texto(texto):
    palabras = texto.lower() .split()
    if palabras [0] == "Agregar" and palabras [1] == "persona":
        nombre = palabras [2]
        edad = int(palabras[3])
        nueva = Persona(nombre = nombre, edad = edad)
        ssesion.add(nueva)
        ssesion.commit()
        return f"Persona '{nombre}' agregada con edad {edad}"
    
    elif texto == "muestra todas las personas" :
        personas = ssesion.query(Persona).all()
        if personas:
            return "\n".join([f"{p.id}. {p.nombre} - {p.edad} años" for p in personas])
        else: 
            return "No hay personas registradas."
        
    elif texto.startswith("Borra Persona"):
        nombre = palabras [2]
        persona = ssesion.query(Persona).filter_by (nombre = nombre).first()
        
        if persona:
            ssesion.delete(persona)
            ssesion.commit()
            return f"Persona '{nombre}' eliminada"
        
        else:
            return f"No se encontro la persona '{nombre}'"
        
    else:
        return "Instruccion no reconocida."
    

    
     
