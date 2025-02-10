# your_app/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_word_at_position(text, position):
    try:
        # Ensure position is an integer
        position = int(position)

        # Split the text into words
        words = text.split()

        # Adjust for 1-based index (position - 1 for 0-based index in Python)
        return words[position - 1] if 0 < position <= len(words) else ""
    except (ValueError, IndexError):
        return ""  # Return empty string if there's an error


@register.filter
def get_sentence_with_blank(text, position):
    try:
        # Ensure position is an integer
        position = int(position)

        # Split the text into words
        words = text.split()

        # Replace the word at the specified position with a blank (1-based index)
        if 0 < position <= len(words):
            words[position - 1] = "_____"

        # Rejoin the words into a sentence
        return " ".join(words)
    except (ValueError, IndexError):
        return text  # Return the original text if there's an error
