from deepface import DeepFace
import json
#result  = DeepFace.verify("image11.jpg", "image12.jpg")
results = DeepFace.verify([['image6.jpg', 'image7.jpg'], 
['image6.jpg', 'image10.jpg'], ['image7.jpg', 'image10.jpg'], ['image7.jpg', 'image11.jpg'], ['image11.jpg', 'image12.jpg']])

print(json.dumps(results, indent="\t"))