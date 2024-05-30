#!/usr/bin/env python3
"""Regex"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    returns the log message obfuscated
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all
                    fields in the log line (message)
    """
    pattern = "|".join(map(re.escape, fields))
    return re.sub(f"({pattern})", redaction, message, flags=re.IGNORECASE)
