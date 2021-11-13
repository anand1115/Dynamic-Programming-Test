def maximumUnits(num,boxes,unitsize,unitPerBox,truckSize):
    boxTypes=list(zip(boxes,unitPerBox))
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    count=0
    for box in boxTypes:
        rem=min(truckSize,box[0])
        count+=rem*box[1]
        truckSize-=rem
        if truckSize<=0:
            break
    return count
print(maximumUnits(2,[1,1],2,[9,6],1))

