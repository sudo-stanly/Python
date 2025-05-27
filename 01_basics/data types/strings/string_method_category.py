#Case Conversion / Formatting
    #capitalize() – First character uppercase
    #casefold() – Aggressive lowercasing (for comparisons)
    #lower() – Converts to lowercase
    #upper() – Converts to uppercase
    #swapcase() – Swaps case
    #title() – Capitalizes first letter of each word

#Alignment
    #center(width) – Centers the string
    #ljust(width) – Left-justifies the string
    #rjust(width) – Right-justifies the string
    #zfill(width) – Pads string on the left with zeros

#Search & Find
    #find(sub[, start[, end]]) – Returns index of first occurrence (or -1)
    #rfind(sub[, start[, end]]) – Same, but from right
    #index(sub[, start[, end]]) – Like find, but raises error if not found
    #rindex(sub[, start[, end]]) – Like rfind, but raises error

#Testing / Boolean Checks
    #isalnum() – Letters and numbers only
    #isalpha() – Only letters
    #isdigit() – Only digits
    #isdecimal() – Only decimal characters
    #isnumeric() – Numeric characters (includes other scripts)
    #islower() – All lowercase
    #isupper() – All uppercase
    #istitle() – Title case
    #isspace() – Only whitespace
    #isprintable() – Printable characters
    #isascii() – ASCII characters only
    #startswith(prefix[, start[, end]]) – Checks if string starts with prefix
    #endswith(suffix[, start[, end]]) – Checks if string ends with suffix

#Modification / Replacement
    #replace(old, new[, count]) – Replaces substrings
    #strip([chars]) – Trims both ends
    #lstrip([chars]) – Trims left side
    #rstrip([chars]) – Trims right side

#Splitting and Joining
    #split(sep=None, maxsplit=-1) – Splits by separator
    #rsplit(sep=None, maxsplit=-1) – Splits from the right
    #splitlines([keepends]) – Splits on line breaks
    #partition(sep) – Splits into 3 parts (before, sep, after)
    #rpartition(sep) – Same, but from right
    #join(iterable) – Joins iterable of strings into one string

#Encoding & Formatting
    #encode(encoding="utf-8") – Encodes string into bytes
    #format() – Formats string using placeholders
    #format_map(mapping) – Formats string using a dictionary
    #maketrans() – Creates a translation table
    #translate(table) – Translates string using a translation table
    #expandtabs(tabsize=8) – Replaces tabs with spaces