import re

try:
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()
        
        matches = re.findall(r'pwd\s*==\s*["\'](.*?)["\'].*?{.*?(console\.log\(".*?"\)|alert\(".*?"\))', content, re.DOTALL)
        
        if matches:
            print("Mots de passe et logs associés trouvés :")
            for pwd, log in matches:
                print(f"Mot de passe : {pwd}")
                log_message = re.search(r'"(.*?)"', log).group(1)
                print(f"Log/Message : {log_message}\n")
        else:
            print("Aucun mot de passe ou log trouvé dans le fichier.")
except FileNotFoundError:
    print("Le fichier 'index.html' est introuvable.")
