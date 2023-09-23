import random 
def generate_code(length=8):
    data =  '012345678hgfjkdfaffyhjtuo'
    code =''.join(random.choice(data) for _ in range(length))
    return code 