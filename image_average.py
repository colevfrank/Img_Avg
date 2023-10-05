"""                                                                                                                                                                      
  This script calculates the pixel-wise average of all images in the ~/Desktop/Screenshots directory                                                                             
  and saves the result as an image in the same directory.                                                                                                                        
  """                                                                                                                                                                            
                                                                                                                                                                                 
  import glob                                                                                                                                                                    
  import os                                                                                                                                                                      
  import numpy as np                                                                                                                                                             
  from PIL import Image                                                                                                                                                          
                                                                                                                                                                                 
  dir_path = os.path.expanduser("~/Desktop/Screenshots")                                                                                                                         
  image_files = glob.glob(os.path.join(dir_path, "*.[Pp][Nn][Gg]")) + glob.glob(os.path.join(dir_path, "*.[Jj][Pp][Gg]*"))                                                       
                                                                                                                                                                                 
  images = []                                                                                                                                                                    
  min_width = min_height = np.inf                                                                                                                                                
                                                                                                                                                                                 
  for file in image_files:                                                                                                                                                       
      img = Image.open(file)                                                                                                                                                     
      images.append(img)                                                                                                                                                         
      if img.size[0] < min_width:                                                                                                                                                
          min_width = img.size[0]                                                                                                                                                
      if img.size[1] < min_height:                                                                                                                                               
          min_height = img.size[1]                                                                                                                                               
                                                                                                                                                                                 
  images = [img.resize((min_width, min_height)) for img in images]                                                                                                               
  image_arrays = [np.array(img) for img in images]                                                                                                                               
  average_image_array = np.average(image_arrays, axis=0)                                                                                                                         
  average_image_array = average_image_array.astype(int)                                                                                                                          
  average_image = Image.fromarray(np.uint8(average_image_array))                                                                                                                 
                                                                                                                                                                                 
  output_path = os.path.join(dir_path, "averaged_image.png")                                                                                                                     
  average_image.save(output_path)" > ~/Library/CloudStorage/OneDrive-SoftwareEngineeringInstitute/Code/adversarial_example_aml_course/Img_Avg/image_average.py   