import Photo as ph
import Slide as slide

def readInput(filename):

    lines = [line.rstrip('\n') for line in open(filename)]
    N= int(lines[0])
    ID = 0
    output_h = []
    output_v = []
    for i in range(1,N-1):
        photo_components = lines[i].split(" ")
        photo = ph.Photo(ID,photo_components[0],photo_components[1],photo_components[2::])
        if photo.type == 'H':
            output_h.append(photo)
        else:
            output_v.append(photo)
        ID +=1
    return (output_h,output_v)




if __name__ == "__main__" :

    file = "a_example.txt"
    o1, o2 =readInput(file)

