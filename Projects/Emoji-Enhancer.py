"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

def emoji_enhancer(message):
    emoji_map = {
        "love": "❤️",
        "code": "💻",
        "tea": "🍵",
        "happy": "😊",
        "sad": "😢",
        "coffee": "☕",
        "python": "🐍",
        "fire": "🔥",
        "star": "⭐",
        "rocket": "🚀",
        "food": "🍔",
        "music": "🎵",
        "book": "📚",
        "sun": "☀️",
        "moon": "🌙",
        "smile": "😄",
        "laugh": "😂",
        "cool": "😎",
        "party": "🎉",
        "heart": "💖"
    }

    updated_words = []

    for word in message.split():
        # Extract punctuation at the end
        punctuation = ""
        cleaned_word = word
        while cleaned_word and cleaned_word[-1] in ".,!?;:":
            punctuation = cleaned_word[-1] + punctuation
            cleaned_word = cleaned_word[:-1]

        # Get emoji for the cleaned word (case-insensitive)
        emoji = emoji_map.get(cleaned_word.lower(), "")

        if emoji:
            updated_words.append(cleaned_word + " " + emoji + punctuation)
        else:
            updated_words.append(word)

    result = ' '.join(updated_words)
    return result


def main():
    print("=== Emoji Enhancer ===")
    print("Enter a message to enhance with emojis!\n")

    user_message = input("Your message: ")

    enhanced_message = emoji_enhancer(user_message)

    print("\nEnhanced message:")
    print(enhanced_message)


if __name__ == "__main__":
    main()
