class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for token in path:
            if stack and token == '..':
                stack.pop()
            else:
                if token not in ['','..','.']:
                    stack.append(token)

        return '/' + '/'.join(stack)
