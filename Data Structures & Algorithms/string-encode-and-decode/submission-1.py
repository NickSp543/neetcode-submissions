class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator
            while s[j] != '#':
                j += 1

            # Get the word length
            length = int(s[i:j])

            # Extract exactly that many characters
            word = s[j + 1:j + 1 + length]

            result.append(word)

            # Move to the beginning of the next encoded word
            i = j + 1 + length

        return result