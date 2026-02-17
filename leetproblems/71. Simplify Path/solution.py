class Solution:
    def simplifyPath(self, path: str) -> str:
        queue = []
        items = path.split("/")

        prev = ""
        for item in items:
            if item == "." or item == "":
                continue
            elif item == "..":
                if queue:
                    queue.pop()
            else:
                queue.append(item)

        return "/" + "/".join(queue)