from fastapi import FastAPI
import os
import psycopg2
from dotenv import load_dotenv
from pydantic import BaseModel 

class Tiket(BaseModel):
    user_request : int 
    status : str 
    tiket_content : str 
    due_date : str 
    assigned_to : int 
    team: str 
    affected : str 

class Staff(BaseModel):
    name : str 
    email: str 
    team : str
    rol : str  

class Users(BaseModel):
    name : str 
    email : str 

load_dotenv()
connection = os.getenv("DB_Connector")
app = FastAPI()

@app.get("/")


def r():
    return{"hello : world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


#sumbit a tiket
@app.post("/uploadtiket")
def create_tiket(tiket:Tiket):
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    try : 
        cursor.execute("""INSERT INTO public.tikets
        (user_request , status , tiket_contet,due_date,assigned_to,team,affected)
        VALUES (%s,%s,%s,%s,%s,%s,%s)""",
        (tiket.user_request,tiket.status,tiket.tiket_content,
        tiket.due_date,tiket.assigned_to,tiket.team,tiket.affected)
        
    )
        conn.commit()
        return {"mensaje":"tiket creado exitosamente"}
    except Exception as e :
        conn.rollback()
        return {"error":str(e)}
    finally :
        cursor.close()
        conn.close()

#register a new person in staff 
@app.post("/registerStaff")
def create_staff(user:Staff):
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO public.staff (name,email,team,rol) 
        VALUES (%s,%s,%s,%s) """ ,
        (user.name, user.email, user.team, user.rol)         
        )
        conn.commit()
        return {"mensaje":"staff agregado con exito"}
    except Exception as e :
        conn.rollback()
        return {"error":str(e)}
    finally:
        cursor.close()
        conn.close()


#register a new user 
@app.post("/registerUser")
def create_user(users:Users):
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    try :
        cursor.execute(""" INSERT INTO public.users (name,email) 
                       VALUES (%s,%s)""",
                       users.name , users.email
        )
        conn.commit()
        return {"mensaje" : "usuario agregado con exito"}
    except Exception as e :
        conn.rollback()
        return {"error":str(e)}
    finally:
        cursor.close()
        conn.close()



# add tiket again 
@app.post("/newEntry")
def new_tik(tiket:Tiket):
    conn = psycopg2.connect(connection)
    cursor  = conn.cursor()
    try:
        cursor.execute(""" INSERT INTO public.tikets (user_request,status,tiket_content,due_date,assigned_to,team,affected)
                       VALUES (%s,%s,%s,%s,%s,%s,%s) 
            """,
            tiket.user_request,tiket.status,tiket.tiket_content,tiket.due_date,tiket.due_date,tiket.assigned_to,tiket.team,tiket.affected
    )
        conn.commit()
        return {"mensaje":"tiket creado exitosamente"}
    except Exception as e :
        conn.rollback()
        return {"error":str(e)}
    finally:
        cursor.close()
        conn.close()
        

#consult staff
@app.get("/staff")
def staff():
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM public.staff;")
        resultado = cursor.fetchall()
        if not resultado:

            raise Exception("no hay staff registrado")
        columnas = [desc[0] for desc in cursor.description]
        staf = [dict(zip(columnas,fila)) for fila in resultado]
        return staf
        
    except Exception as e :
        conn.rollback()
        return {"error": str(e)}
    finally:
        conn.cursor()
        conn.close()
        

#consult users 

@app.get("/users")
def users():
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    try :
        cursor.execute("SELECT * FROM public.users;")
        resultado = cursor.fetchall()
        if not resultado :
             raise Exception("no hay usuarios registrados")
        columnas = [desc[0] for desc in cursor.description]
        userss = [dict(zip(columnas, fila)) for fila in resultado]
        return userss
    except Exception as e :
        conn.rollback()
        return {"mensaje": str(e)}
    finally:
        conn.close()
        cursor.close()
        


#consult tikets 
@app.get("/tikets/") 
def tikets():
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    try : 
        cursor.execute("SELECT * FROM public.tikets;")
        resultado = cursor.fetchall()
        if not resultado :
    
            raise Exception("no hay tikets en el pool")
        columnas = [desc[0] for desc in cursor.description]
        tickets = [dict(zip(columnas, fila)) for fila in resultado]
        return tickets
    except Exception as e:
        conn.rollback()
        return {"error" : str(e)} 
    finally :
        conn.close()
        cursor.close()



