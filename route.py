import os
from flask import Flask, render_template, request, redirect, session, flash, url_for  
from controller import *
from werkzeug.utils import secure_filename

def route(app):    
    @app.route("/")
    @app.route("/home")
    def home():
        return homePag()   
        
    @app.route("/onlyfans")
    def onlyfans():
        param={}
        return adminLoginPag(param)
    
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
        return redirect('/onlyfans')

    @app.route("/createProduct", methods =["GET", "POST"])
    def createProduct():
        return createProductAlg(request)
    
    @app.route("/deleteProduct", methods =["GET", "POST"])
    def deleteProduct():
        return deleteProductAlg(request)

    @app.route("/editProduct", methods =["GET", "POST"])
    def editProduct():
        return editProductPage(request)

    @app.route("/editProductAlg", methods =["GET", "POST"])
    def editProductAlg():
        return editProductLog(request)
    
    @app.route("/updatePhoto", methods =["GET", "POST"])
    def updatePhotoPag():
        return updatePhoto(request)

    @app.route('/<name>')
    def noEncontrada(name):
        return notFound(name)
    