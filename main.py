import fastapi
from fastapi import FastAPI, APIRouter, Depends, Request,status,Form
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from models import UserDetails,Base,Products,Cart,Orders
from pydantic import BaseModel
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# PostgreSQL database connection Configuration
DATABASE_URL = f"postgresql://joelnencil:Jojima2003@db:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# PostgreSQL database connection Configuration

app = FastAPI()
router = APIRouter()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    email: str
    password: str

@app.get('/',response_class=HTMLResponse,include_in_schema=False)
def form(request:Request):
    return templates.TemplateResponse("/index.html",{"request":request})

    
    
@app.get("/account",response_class=HTMLResponse)
def dashboard(request:Request):
    print("hello world")
    return templates.TemplateResponse("/account.html",{"request":request})

@app.get("/products",response_class=HTMLResponse)
def dashboard(request:Request,db:Session = Depends(get_db)):
    print("hello world")
    products=db.query(Products).all()
    return templates.TemplateResponse("/products.html",{"request":request,'products':products})

@app.get("/product-details",response_class=HTMLResponse)
def dashboard(request:Request):
    print("hello world")
    return templates.TemplateResponse("/product-details.html",{"request":request})

@app.get("/cart",response_class=HTMLResponse)
def dashboard(request:Request,db:Session = Depends(get_db)):
    print("hello world")
    cart=db.query(Cart).all()
    return templates.TemplateResponse("/cart.html",{"request":request,"cart":cart})


@app.post("/register",response_class=HTMLResponse)
def register(request:Request,email: str = Form(...),password: str = Form(...),db:Session = Depends(get_db)):
    user_details=db.query(UserDetails).filter(UserDetails.email==email,UserDetails.password==password).first()
    if user_details:
        return RedirectResponse(url='/account',status_code=status.HTTP_302_FOUND)
    else:
        db_register = UserDetails(
            email=email,
            password=password
        )
        db.add(db_register)
        db.commit()
        response=RedirectResponse(url='/products',status_code=status.HTTP_302_FOUND)
        return response

@app.post("/login",response_class=HTMLResponse)
def register(request:Request,email: str = Form(...),password: str = Form(...),db:Session = Depends(get_db)):
    user_details=db.query(UserDetails).filter(UserDetails.email==email,UserDetails.password==password).first()
    if user_details:
        return RedirectResponse(url='/products',status_code=status.HTTP_302_FOUND)
    else:
        return RedirectResponse(url='/account',status_code=status.HTTP_302_FOUND)


@app.post("/add-to-cart",response_class=HTMLResponse)
def addtocart(request:Request,id: str = Form(...),name: str = Form(...),price:str = Form(...),db:Session = Depends(get_db)):
        db_register = Cart(
            id=id,
            product_name=name,
            product_price=price
        )
        db.add(db_register)
        db.commit()
        response=RedirectResponse(url='/products',status_code=status.HTTP_302_FOUND)
        return response

@app.post("/checkout", response_class=HTMLResponse)
def checkout(request: Request, db: Session = Depends(get_db)):
    cart_items = db.query(Cart).all()
    
    for item in cart_items:
        order = Orders(
            id=item.id,
            product_name=item.product_name,
            product_price=item.product_price
        )
        db.add(order)
        db.delete(item)
    
    db.commit()
    response = RedirectResponse(url='/products', status_code=status.HTTP_302_FOUND)
    return response


    
    





