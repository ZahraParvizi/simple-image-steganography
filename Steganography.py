from PIL import Image

def encode_text (img_input , text , img_output):
    #vonvert text to ascii code
    ascii_code= [ord(ch) for ch in text]
    text_len=len(text)
    idx=0  
    
    img=Image.open(img_input)
    
    #save Text length in first pixle of image
    r, g, b = img.getpixel((0, 0))
    img.putpixel((0, 0), (text_len, g, b))
    
    #Encrypting text in images
    for y in range(10,img.size[0],10):
        for x in range(10,img.size[1],10):
            if x==0 and y==0:
                continue
            if idx < text_len:
                r, g, b = img.getpixel((x,y))
                img.putpixel((x,y), (ascii_code[idx], g, b))
                idx+=1
            else:
                break
        if idx >= text_len:
            break
        
    #saving encrypted photo
    img.save(img_output)
    print("Text successfully saved inside the image.✅")
    img.show()
        
    
def decode_text(image_path):
    img=Image.open(image_path)
    
    #get Text length from the first pixel of the image
    r, g, b = img.getpixel((0,0))
    text_len= r
    
    chars=[]
    idx=0
    
    #decoding image
    for y in range(10,img.size[0],10):
        for x in range(10,img.size[1],10):
            if x==0 and y==0:
                continue
            if idx < text_len:
                r, g, b = img.getpixel((x,y))
                chars.append(chr(r))
                idx+=1
            else:
                break
        if idx >= text_len:
            break
    return "".join(chars)
    
    
#Get the user's desired operation(Encrypting/decoding)
user_request=int(input("Enter number 1 for Encrypting your text OR enter number 2 for decoding: "))

#Taking text from the user and performing encryption operations
if user_request ==1:
    text=input("pleas enter the text you want Encrypting: ")
    img_input=input("enter the path of image you want encript your text on this: ")
    img_output=input("enter a path for encripting image in output(The image format must be PNG.): ")
    encode_text (img_input , text , img_output)

#Receiving an image and decoding text from it    
elif user_request== 2 :
    image_path=input("pleas enter the path of your image(The image format must be PNG.): ")
    print("\n 🔓 Decrypted text: ", decode_text(image_path))    


           
    
