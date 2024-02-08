import numpy as np

from django.shortcuts import render

from .src.blend_images import blend_images
from .src.image_opener import open_image
from .src.convert_to_grayscale import convert_to_grayscale
from .src.convert_to_black_and_white import convert_to_black_and_white
from .src.resize_image import redimensionner_image
from .src.fusionner_verticalement import fusionner_verticalement
from .src.fusionner_horizontalement import fusionner_horizontalement
from .src.create_gif import creer_gif

# Create your views here.
def upload_image(request):
   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']

      # ouvrir image
      image_t = open_image(image)
      image_t.save("media/image_classique.png")
      return render(request, 'init_image/traitement.html')
   
   return render(request, 'init_image/index.html')

def page_gray(request):
   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']

      # ouvrir image
      image_t = open_image(image)
      image_t.save("media/image_classique.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = convert_to_grayscale(image_t)
      image_noir_blanc.save("media/image_gray.png")

      return render(request, 'init_image/gray.html', context={"image_classique" : True})
         
   return render(request, 'init_image/gray.html', context={"image_classique" : False})

def black_white(request):
   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']

      # ouvrir image
      image_t = open_image(image)
      image_t.save("media/image_classique.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = convert_to_black_and_white(image_t)
      image_noir_blanc.save("media/image_noir-blanc.png")

      return render(request, 'init_image/black_white.html', context={"image_classique" : True})

   return render(request, 'init_image/black_white.html', context={"image_classique" : False})

def resize_picture(request):
   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']
      hauteur = int(request.POST['hauteur'])
      largeur = int(request.POST['largeur'])

      if(hauteur < 1 ):
         hauteur = 100
      if(largeur <1):
         largeur = 100

      # ouvrir image
      image_t = open_image(image)
      image_t.save("media/image_classique.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = redimensionner_image(np.asarray(image_t), hauteur, largeur)
      image_noir_blanc.save("media/image_resize.png")

      return render(request, 'init_image/resize.html', context={"image_classique" : True})

   return render(request, 'init_image/resize.html', context={"image_classique" : False})

def alignement_vertical(request):
   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']
      image2 = request.FILES['image2']

      # ouvrir image
      image_t1 = open_image(image)
      image_t1.save("media/image_classique_1.png")

      image_t2 = open_image(image2)
      image_t2.save("media/image_classique_2.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = fusionner_verticalement(image_t1, image_t2)
      image_noir_blanc.save("media/image_fusion-vertical.png")

      return render(request, 'init_image/align_vertical.html', context={"image_classique" : True})

   return render(request, 'init_image/align_vertical.html', context={"image_classique" : False})

def alignement_horizontal(request):
   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']
      image2 = request.FILES['image2']

      # ouvrir image
      image_t1 = open_image(image)
      image_t1.save("media/image_classique_1.png")

      image_t2 = open_image(image2)
      image_t2.save("media/image_classique_2.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = fusionner_horizontalement(image_t1, image_t2)
      image_noir_blanc.save("media/image_fusion-horizontal.png")

      return render(request, 'init_image/align_horizontal.html', context={"image_classique" : True})

   return render(request, 'init_image/align_horizontal.html', context={"image_classique" : False})

def fusion(request):
   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']
      image2 = request.FILES['image2']

      # ouvrir image
      image_t1 = open_image(image)
      image_t1.save("media/image_classique_1.png")

      image_t2 = open_image(image2)
      image_t2.save("media/image_classique_2.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = blend_images(image_t1, image_t2, 0.1, (1000,1000))
      image_noir_blanc.save("media/image_fusion.png")

      return render(request, 'init_image/fusion.html', context={"image_classique" : True})

   return render(request, 'init_image/fusion.html', context={"image_classique" : False})

def animation(request):
   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']
      image2 = request.FILES['image2']
      duree = int(request.POST['duree'])

      # ouvrir image
      image_t1 = open_image(image)
      image_t1.save("media/image_classique_1.png")

      image_t2 = open_image(image2)
      image_t2.save("media/image_classique_2.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = creer_gif([image_t1, image_t2], duree)

      return render(request, 'init_image/animation.html', context={"image_classique" : True})

   return render(request, 'init_image/animation.html', context={"image_classique" : False})

