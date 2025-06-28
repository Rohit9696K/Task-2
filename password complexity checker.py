import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    score = 0
    feedback = []

    if length_criteria:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if uppercase_criteria:
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z).")

    if lowercase_criteria:
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z).")

    if digit_criteria:
        score += 1
    else:
        feedback.append("❌ Include at least one number (0-9).")

    if special_char_criteria:
        score += 1
    else:
        feedback.append("❌ Use at least one special character (e.g. !, @, #, $).")

    # Final strength rating
    strength_levels = {
        5: "✅ Very Strong",
        4: "✔️ Strong",
        3: "⚠️ Moderate",
        2: "❗ Weak",
        1: "❌ Very Weak",
        0: "❌ Extremely Weak"
    }

    print(f"\nPassword Strength: {strength_levels[score]}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(" -", tip)

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ").strip()
    check_password_strength(password)

if __name__ == "__main__":
    main()
