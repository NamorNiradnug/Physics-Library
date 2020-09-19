"""Module with functions for pretty printing of PyPhysic objects."""


__superscripts = {
    "0": "\u2070",
    "1": "\u00b9",
    "2": "\u00b2",
    "3": "\u00b3",
    "4": "\u2074",
    "5": "\u2075",
    "6": "\u2076",
    "7": "\u2077",
    "8": "\u2078",
    "9": "\u2079",
    "-": "\u207B"
}


def superscripted(n: int) -> str:
    """Superscripted integer"""
    string = str(n)
    superscripted_str = ""
    for ch in range(string):
        superscripted_str += __superscripts[ch]
    return superscripted_str
