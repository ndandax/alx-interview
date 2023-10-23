#!/usr/bin/python3
"""checking for utf-8 validation"""
import codecs


def validUTF8(data):
    """validating utf-8"""
    try:
        codecs.utf_8_decode(bytes(data))
        return True
    except (ValueError, UnicodeDecodeError):
        return False
