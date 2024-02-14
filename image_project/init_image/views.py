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
   return render(request, 'init_image/index.html')

def black_white(request):
   tableau_extension = ['jpeg', 'jpg', 'svg', 'png']

   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']

      nom_image = str(image)
      nom_fichier = nom_image.split(".")[0]
      extension = nom_image.split(".")[-1]


      if extension not in tableau_extension:
         return render(request, 'init_image/black_white.html', context={"image_classique" : False,
            'message_erreur' : 'mauvaise extension (jpeg/jpg, png ou svg)'})

      # ouvrir image 
      image_t = open_image(image)
      image_t.save("media/image_classique.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = convert_to_black_and_white(image_t)
      image_noir_blanc.save("media/image_noir-blanc.png")

      return render(request, 'init_image/black_white.html', context={"image_classique" : True})

   return render(request, 'init_image/black_white.html', context={"image_classique" : False})

def page_gray(request):
   tableau_extension = ['jpeg', 'jpg', 'svg', 'png']

   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']

      nom_image = str(image)
      nom_fichier = nom_image.split(".")[0]
      extension = nom_image.split(".")[-1]


      if extension not in tableau_extension:
         return render(request, 'init_image/gray.html', context={"image_classique" : False,
            'message_erreur' : 'mauvaise extension (jpeg/jpg, png ou svg)'})

      # ouvrir image
      image_t = open_image(image)
      image_t.save("media/image_classique.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = convert_to_grayscale(image_t)
      image_noir_blanc.save("media/image_gray.png")

      return render(request, 'init_image/gray.html', context={"image_classique" : True})
         
   return render(request, 'init_image/gray.html', context={"image_classique" : False})

def resize_picture(request):
   tableau_extension = ['jpeg', 'jpg', 'svg', 'png']

   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']

      nom_image = str(image)
      nom_fichier = nom_image.split(".")[0]
      extension = nom_image.split(".")[-1]


      if extension not in tableau_extension:
         return render(request, 'init_image/resize.html', context={"image_classique" : False,
            'message_erreur' : 'Erreur : mauvaise extension (jpeg/jpg, png ou svg)'})

      try :
         hauteur = int(request.POST['hauteur'])
         largeur = int(request.POST['largeur'])
      except:
         return render(request, 'init_image/resize.html', context={"image_classique" : False,
            'message_erreur' : 'Erreur : seulement des intiers pour la hauteur et la largeur'})

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
   tableau_extension = ['jpeg', 'jpg', 'svg', 'png']

   if request.method == 'POST' and request.FILES:
      '''
      image = request.FILES['image']
      image2 = request.FILES['image2']

      nom_image = str(image)
      nom_image2 = str(image2)
      nom_fichier, extension = nom_image.split(".")
      nom_fichier, extension2 = nom_image2.split(".")

      if extension not in tableau_extension or extension2 not in tableau_extension:
         return render(request, 'init_image/align_vertical.html', context={"image_classique" : False,
            'message_erreur' : 'Erreur : mauvaise extension (jpeg/jpg, png ou svg)'})

      # ouvrir image
      image_t1 = open_image(image)
      image_t1.save("media/image_classique_1.png")

      image_t2 = open_image(image2)
      image_t2.save("media/image_classique_2.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = fusionner_verticalement(image_t1, image_t2)
      image_noir_blanc.save("media/image_fusion-vertical.png")

      return render(request, 'init_image/align_vertical.html', context={"image_classique" : True})
      '''
      
      tableau_images = []
      i = 0

      images = request.FILES.getlist('images[]')

      for image in images :
        tableau_images.append(image)

      for image in tableau_images:
         nom_image = str(image)
         nom_fichier = nom_image.split(".")[0]
         extension = nom_image.split(".")[-1]

         if extension not in tableau_extension:
            return render(request, 'init_image/align_vertical.html', context={"image_classique" : False,
            'message_erreur' : 'Erreur : mauvaise extension (jpeg/jpg, png ou svg)'})
      
      if len(tableau_images) <2:
          return render(request, 'init_image/align_vertical.html', context={"image_classique" : False,
               'message_erreur' : 'Erreur : Nombre d\'image insuffisant (2 images minimum)'})

      

      # save all picture
      for image in tableau_images:
         image_t1 = open_image(image)
         image_t1.save("media/image_align_v_" + str(i) + ".png")
         tableau_images[i] = image_t1
         i += 1

      tab_number = [number for number in range(0, i)]


      img_align = fusionner_verticalement(tableau_images[0], tableau_images[1])
      for i in range(2, len(tableau_images)):
         img_align = fusionner_verticalement(img_align, tableau_images[i])
      
      img_align.save("media/image_fusion-vertical.png")


      return render(request, 'init_image/align_vertical.html', context={"image_classique" : True, 'tab_number' : tab_number})

   return render(request, 'init_image/align_vertical.html', context={"image_classique" : False})

def alignement_horizontal(request):
   tableau_extension = ['jpeg', 'jpg', 'svg', 'png']

   if request.method == 'POST' and request.FILES:
      '''
      image = request.FILES['image']
      image2 = request.FILES['image2']

      nom_image = str(image)
      nom_image2 = str(image2)
      nom_fichier, extension = nom_image.split(".")
      nom_fichier, extension2 = nom_image2.split(".")

      if extension not in tableau_extension or extension2 not in tableau_extension:
         return render(request, 'init_image/align_horizontal.html', context={"image_classique" : False,
            'message_erreur' : 'Erreur : mauvaise extension (jpeg/jpg, png ou svg)'})

      # ouvrir image
      image_t1 = open_image(image)
      image_t1.save("media/image_classique_1.png")

      image_t2 = open_image(image2)
      image_t2.save("media/image_classique_2.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = fusionner_horizontalement(image_t1, image_t2)
      image_noir_blanc.save("media/image_fusion-horizontal.png")
      '''

      tableau_images = []
      i = 0

      images = request.FILES.getlist('images[]')

      for image in images :
        tableau_images.append(image)

      for image in tableau_images:
         nom_image = str(image)
         nom_fichier = nom_image.split(".")[0]
         extension = nom_image.split(".")[-1]

         if extension not in tableau_extension:
            return render(request, 'init_image/align_horizontal.html', context={"image_classique" : False,
            'message_erreur' : 'Erreur : mauvaise extension (jpeg/jpg, png ou svg)'})
      
      if len(tableau_images) <2:
          return render(request, 'init_image/align_horizontal.html', context={"image_classique" : False,
               'message_erreur' : 'Erreur : Nombre d\'image insuffisant (2 images minimum)'})

      

      # save all picture
      for image in tableau_images:
         image_t1 = open_image(image)
         image_t1.save("media/image_align_h_" + str(i) + ".png")
         tableau_images[i] = image_t1
         i += 1

      tab_number = [number for number in range(0, i)]


      img_align = fusionner_horizontalement(tableau_images[0], tableau_images[1])
      for i in range(2, len(tableau_images)):
         img_align = fusionner_horizontalement(img_align, tableau_images[i])
      
      img_align.save("media/image_fusion-horizontal.png")

      return render(request, 'init_image/align_horizontal.html', context={"image_classique" : True, 'tab_number' : tab_number})

   return render(request, 'init_image/align_horizontal.html', context={"image_classique" : False})

def fusion(request):
   tableau_extension = ['jpeg', 'jpg', 'svg', 'png']

   if request.method == 'POST' and request.FILES:
      image = request.FILES['image']
      image2 = request.FILES['image2']

      nom_image = str(image)
      nom_image2 = str(image2)
      nom_fichier = nom_image.split(".")[0]
      extension = nom_image.split(".")[-1]

      nom_fichier = nom_image2.split(".")[0]
      extension2 = nom_image2.split(".")[-1]


      if extension not in tableau_extension or extension2 not in tableau_extension:
         return render(request, 'init_image/fusion.html', context={"image_classique" : False,
            'message_erreur' : 'Erreur : mauvaise extension (jpeg/jpg, png ou svg)'})

      opacite = request.POST['opacite']
      opacite = opacite.replace(',', '.')
      opacite = float(opacite)

      try :
         position_x = int(request.POST['position_x'])
         position_y = int(request.POST['position_y'])
      except:
         return render(request, 'init_image/fusion.html', context={"image_classique" : False,
            'message_erreur' : 'Erreur : seulement des intiers pour l\'opacité et la position (x,y)'})

      # ouvrir image
      image_t1 = open_image(image)
      image_t1.save("media/image_classique_1.png")

      image_t2 = open_image(image2)
      image_t2.save("media/image_classique_2.png")
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = blend_images(image_t1, image_t2, opacite, (position_x,position_y))
      image_noir_blanc.save("media/image_fusion.png")

      return render(request, 'init_image/fusion.html', context={"image_classique" : True})

   return render(request, 'init_image/fusion.html', context={"image_classique" : False})

def animation(request):
   tableau_extension = ['jpeg', 'jpg', 'svg', 'png']

   if request.method == 'POST' and request.FILES:

      tableau_images = []
      i = 0

      duree = int(request.POST['duree'])
      images = request.FILES.getlist('images[]')

      for image in images :
        tableau_images.append(image)

      for image in tableau_images:
         nom_image = str(image)
         nom_fichier = nom_image.split(".")[0]
         extension = nom_image.split(".")[-1]
         if extension not in tableau_extension:
            return render(request, 'init_image/animation.html', context={"image_classique" : False,
               'message_erreur' : 'Erreur : mauvaise extension (jpeg/jpg, png ou svg)'})

      
      # save all picture
      for image in tableau_images:
         image_t1 = open_image(image)
         image_t1.save("media/image_classique_" + str(i) + ".png")
         tableau_images[i] = image_t1
         i += 1

      tab_number = [number for number in range(0, i)]
      
      # 1. Transformation en noir et blanc
      image_noir_blanc = creer_gif(tableau_images, duree)

      return render(request, 'init_image/animation.html', context={"image_classique" : True, 
            'tab_number' : tab_number})

   return render(request, 'init_image/animation.html', context={"image_classique" : False})

