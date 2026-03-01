def http_status(status:str) -> str:
    match(status):
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 500:
            return "Internal Sersver Error"
        case _:
            return "Unknown status"
        

print(http_status(500))        