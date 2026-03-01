from typing import Dict
Dict1 : Dict[str,int]={"Dibya":22,"Bhabani":44}
Dict2 : Dict[str,int] = {"Bhama":77,"Dibya":90}


merged = Dict1 | Dict2
print(merged)