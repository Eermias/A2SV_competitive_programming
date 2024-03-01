class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptrName = 0
        ptrTyped = 0
        if len(typed) < len(name):
            return False
        while ptrName < len(name) and ptrTyped < len(typed):
            if name[ptrName] == typed[ptrTyped]:
                ptrName += 1
                if ptrName < len(name):
                    if name[ptrName] != name[ptrName - 1]:
                        while typed[ptrTyped] == name[ptrName - 1]:
                            ptrTyped += 1
                            if ptrTyped == len(typed):
                                return False
                    else:
                        ptrTyped += 1
            else:
                return False
        while ptrTyped < len(typed) - 1:
            if typed[ptrTyped + 1] != typed[ptrTyped]:
                return False
            ptrTyped += 1
        
        return True

        