class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = []
        sett = (".", "..", "")
        path = path.split("/")
        for folder in path:
            if folders and folder == "..":
                folders.pop()
            elif folder not in sett:
                folders.append(folder)
        return "/" + "/".join(folders)

        
        