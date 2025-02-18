import os
from flask import Flask, render_template, request, redirect, session, flash, url_for  
from controller import *
from werkzeug.utils import secure_filename

def route(app):    
    @app.route("/")
    @app.route("/home")
    def home():
        param={} 
        return homePag(param)   
        
    @app.route("/onlyfans")
    def onlyfans():
        param={}
        return adminPag(param)
    
    @app.route("/adminCheck", methods =["GET", "POST"])
    def adminCheck():
        param={}
        return checkAdminPassword(param,request)
    
    @app.route("/onlyfans_admin")
    def onlyfans_admin():
        param={}
        return adminPagOrg(param)
    
    @app.route("/closeAdminSession")
    def closeAdminSession():
        session['admin'] = False
        return redirect('/')

    @app.route("/createProduct", methods =["GET", "POST"])
    def createProduct():
        return createProductAlg(request)
    
    @app.route("/deleteProduct", methods =["GET", "POST"])
    def deleteProduct():
        return deleteProductAlg(request)
    

    @app.route("/signup", methods =["GET", "POST"])
    def signup():
        ''' Info:
          Recepciona la solicitud request que es enviada
          desde el formulario de registro 
          registroDeUsuario: Luego de realizar el proceso de 
             registro del usuario, retorna la pagina del login 
        '''
        param={}
        return registrarUsuario(param,request)


    @app.route('/signin', methods =["GET", "POST"])
    def signin(): 
        ''' Info: 
          Recepciona la solicitud request que es enviada
          desde el formulario de login 
          retorna la pagina home en caso de exito 
                  o la pagina login en caso de fracaso
        '''
        param={}
        return ingresoUsuarioValido(param,request)

 
    @app.route("/logout")
    def logout():  
        ''' Info: 
          Cierra la sesión.
          retorna la redirección a la pagina home   
        ''' 
        cerrarSesion()     
        return redirect('/')
    

    @app.route("/pagina01")
    def pag01():
        ''' Info:
          Carga la pagina 01
          Retorna la pagina 01, si hay sesion; sino retorna la home.
        '''
        param={}
        return pagina01(param)


    @app.route("/pagina02")
    def pag02():
        ''' Info:
          Carga la pagina 02
          Retorna la pagina 02, si hay sesion; sino retorna la home.
        '''
        param={}
        return pagina02(param)   


    @app.route("/edit_user")
    def edit_user():
        ''' Info:
          Carga la edit_user
          Retorna la edit_user, si hay sesion; sino retorna la home.
        '''
        param={}
        return editarUsuario_pagina(param)    
 

    @app.route("/update_user", methods =["GET", "POST"])
    def update_user():
        ''' Info:
          Recepciona la solicitud request que es enviada
              desde el formulario de edit_user 
          Retorna 
            si hay sesion: retorna la edit_user con los datos actualizados
               y un mensaje de exito o fracaso sobre el mismo form ; 
            si no hay sesion: retorna la home.
        '''
        param={}
        return actualizarDatosDeUsuarios(param,request)
    

    @app.route("/about")
    def about():
        ''' Info:
          Carga la pagina about
        '''
        param={}
        return acercaDe_pagina(param)      


    @app.route('/<name>')
    def noEncontrada(name):
        ''' Info:
          Entra en esta ruta todo direccionamiento recibido que 
          no machea con ningun otro route. Es decir no es un pagina (dirección)
            válida en el sistema.
          Retorna una pagina indicando el error. 
        '''  
        
        return paginaNoEncontrada(name)
    
    @app.route('/upload') 
    def  upload () : 
      return"""
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="uploader" method="post" enctype="multipart/form-data">
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
      """
    
    @app.route('/uploader', methods = ['GET', 'POST'])
    def formrecibe():
      diRequest={}
      #getRequet(diRequest)
      upload_file (diRequest)
      return  diRequest # Cambiar a un retorno de una pagina (esto es solo prueba) 

   