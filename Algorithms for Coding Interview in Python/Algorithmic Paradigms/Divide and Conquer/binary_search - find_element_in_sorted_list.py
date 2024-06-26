"""This method assumes that the list is sorted"""
def search(searchList, key):
    print(searchList)
    mid = int(len(searchList) / 2)
    print("Searching midpoint at ", str(searchList[mid]))
    
    if mid == 0:
        print("Key Not Found!")
        return key
    
    elif key == searchList[mid]:
        print("Key Found!")
        return searchList[mid]
    
    elif key > searchList[mid]:
        print("searchList now contains ",
              searchList[mid:len(searchList)])
        search(searchList[mid:len(searchList)], key)
    else:
        print("searchList now contains ",
              searchList[0:mid])
        search(searchList[0:mid], key)

if __name__ == "__main__":
    aList = list(range(1, 21))
    search(aList, 5)