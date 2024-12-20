
def checkIfExist(arr) -> bool:
    # self.arr = arr
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == 2 * arr[j]:
                return True
    return False


print(checkIfExist([7,1,14,11]))