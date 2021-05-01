import requests

for y in range(1,6):
    file_url = "http://panchbhaya.weebly.com/uploads/1/3/7/0/13701351/phys11_sm_7_" + str(y) + ".pdf"

    r = requests.get(file_url, stream = True)
    
    with open("Chapter_7_Lesson"+str(y)+".pdf","wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
    
            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)
