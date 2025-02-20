from flask import request, session,redirect,render_template
from datetime import datetime
from model import *
from werkzeug.utils import secure_filename
import os
from uuid import uuid4
from appConfig import config


def getRequet(diResult):
    if request.method=='POST':
        for name in request.form.to_dict().keys():
            li=request.form.getlist(name)
            if len(li)>1:
                diResult[name]=request.form.getlist(name)
            elif len(li)==1:
                diResult[name]=li[0]
            else:
                diResult[name]=""
    elif request.method=='GET':  
        for name in request.args.to_dict().keys():
            li=request.args.getlist(name)
            if len(li)>1:
                diResult[name]=request.args.getlist(name)
            elif len(li)==1:
                diResult[name]=li[0]
            else:
                diResult[name]=""     

def upload_file (diResult) :
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
    MAX_CONTENT_LENGTH = 1024 * 1024     
    if request.method == 'POST' :         
        for key in request.files.keys():  
            diResult[key]={} 
            diResult[key]['file_error']=False            
            
            f = request.files[key] 
            if f.filename!="":     
                #filename_secure = secure_filename(f.filename)
                file_extension=str(os.path.splitext(f.filename)[1])
                filename_unique = uuid4().__str__() + file_extension
                path_filename=os.path.join( config['upload_folder'] , filename_unique)
                # Validaciones
                if file_extension not in UPLOAD_EXTENSIONS:
                    diResult[key]['file_error']=True
                    diResult[key]['file_msg']='Error: No se admite subir archivos con extension '+file_extension
                if os.path.exists(path_filename):
                    diResult[key]['file_error']=True
                    diResult[key]['file_msg']='Error: el archivo ya existe.'
                    diResult[key]['file_name']=f.filename
                try:
                    if not diResult[key]['file_error']:
                        diResult[key]['file_error']=True
                        diResult[key]['file_msg']='Se ha producido un error.'

                        f.save(path_filename)   
                        diResult[key]['file_error']=False
                        diResult[key]['file_name_new']=filename_unique
                        diResult[key]['file_name']=f.filename
                        diResult[key]['file_msg']='OK. Archivo cargado exitosamente'
 
                except:
                        pass
            else:
                diResult[key]={} # viene vacio el input del file upload

##########################################################################
#  P Á G I N A S
##########################################################################

def homePag(): 
    # Agarramos los productos de la base de datos, y los guardarmos en una lista 
    base = selectDB(BASE,"select * from productos;")
    return render_template('index.html', base=base)

def adminLoginPag(param):
    if session.get('admin'):
        return redirect('/onlyfans_admin')
    return render_template('admin_login.html', param=param)
 
def checkAdminPassword(param, request):
    miRequest={}
    getRequet(miRequest)
    if miRequest.get('password') == '2948167968':
        session['admin'] = True
        return redirect('/onlyfans_admin')
    else:
        param['error_msg_login']="Error: Contraseña incorrecta"
        return adminLoginPag(param)

def adminPagOrg(param):
    if session.get('admin'):
        productos = selectDB(BASE,"select * from productos;")
        return render_template('admin.html',param=param, productos=productos)
    else:
        return redirect('/onlyfans')

def createProductAlg(request):
    miRequest={}
    getRequet(miRequest)
    insertDB(BASE,"insert into productos (id, name, descriptio, price, image) values (NULL, '{}', '{}', '{}', 'hola');".format(miRequest.get('nombre'), miRequest.get('precio'), miRequest.get('descripcion')))
    return redirect('/onlyfans_admin')

def deleteProductAlg(request):
    # POST request
    miRequest={}
    getRequet(miRequest)
    insertDB(BASE,"delete from productos where id = {};".format(miRequest.get('id')))
    return redirect('/onlyfans_admin')

def notFound(name):
    return render_template('404.html',name=name)

BASE={ "host":"database-1.cbqsyomsicfl.sa-east-1.rds.amazonaws.com",
        "user":"admin",
        "pass":"romasurdo123",
        "dbname":"Tinos"}