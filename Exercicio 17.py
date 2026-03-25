codigo = int(input("Digite um código HTTP: "))

match codigo:
    case 200:
        print("200 -> OK")
    
    case 400:
        print("400 -> Bad Request")
    
    case 401:
        print("401 -> Unauthorized")
    
    case 403:
        print("403 -> Forbidden")
    
    case 404:
        print("404 -> Not Found")
    
    case 500:
        print("500 -> Internal Server Error")
    
    case _:
        print("Código não reconhecido ou não cadastrado.")
