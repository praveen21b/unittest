from typing import List

def joins(xs:List[int], delimiter:str)-> str:
    """Produce string from the list sepearated by the deilimter"""
    generated_string = ''

    for item in xs:
        if generated_string == '':
            generated_string += str(item)
        else:
            generated_string += delimiter+str(item)
    
    return generated_string


if __name__ == '__main__':
    print(joins([1,2,30],','))