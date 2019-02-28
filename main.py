import Photo as ph
import Slide as sl
import random

def readInput(filename):

    lines = [line.rstrip('\n') for line in open(filename)]
    N= int(lines[0])
    ID = 0
    slides_h = []
    output_v = []
    for i in range(1,N):
        photo_components = lines[i].split(" ")
        photo = ph.Photo(ID,photo_components[0],photo_components[1],photo_components[2::])
        if photo.type == 'H':
            slide = sl.Slide([photo.id], photo.tags)
            slides_h.append(slide)
        else:
            output_v.append(photo)
        ID +=1
    return (slides_h,output_v,N)

def slideshow_vertical(new_list):

    random.shuffle(new_list)
    list_slides = []
    for i in range(0,len(new_list)-1,2):
        mergeset= set( new_list[i].tags + new_list[i+1].tags)
        mergelist= list(mergeset)
        slide = sl.Slide([new_list[i].id, new_list[i+1].id], mergelist)
        list_slides.append(slide)
    return list_slides

def merge_twoLists(l1,l2):
    list_slides = l1 + l2
    sortedlist = sorted(list_slides, key=lambda x: len(x.tags), reverse=True)
    return  sortedlist



if __name__ == "__main__" :

    file = "d_pet_pictures.txt"
    o1, o2 , N =readInput(file)
    list_slides = slideshow_vertical(o2)
    list = merge_twoLists(list_slides,o1)



