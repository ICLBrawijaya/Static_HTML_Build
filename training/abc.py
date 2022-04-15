edit_asisten= Asisten.objects.get(nim=updatenim)
edit_asisten[“nama”]= “Maemunah” 
edit_asisten.save()

