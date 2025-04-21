class Solution:
    def splitMessage(self, message, limit):
        """
        Split the given message into one or more parts based on the limit.
        Each part will have a suffix "<a/b>", where "b" is the total number of parts and "a" is the current part index.
        Return the parts as an array of strings, or an empty array if it's not possible to split the message.
        """
        for part_count in range(1, len(message) + 1):
            suffix_length = len(f"<{part_count}/{part_count}>")
            if suffix_length * part_count + len(message) <= limit * part_count:
                result = []
                idx = 0
                for i in range(1, part_count + 1):
                    suffix = f"<{i}/{part_count}>"
                    part_length = limit - len(suffix)
                    result.append(message[idx:idx + part_length] + suffix)
                    idx += part_length
                return result
        return []