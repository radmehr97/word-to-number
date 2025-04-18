def number_to_words_fa(n):
    yekan = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
    dahgan = ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
    sadgan = ["", "یکصد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
    dah_ta_nuzdah = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]

    basex = ["", "هزار", "میلیون", "میلیارد", "تریلیون", "کادریلیون", "کوینتیلیون", "سکستیلیون", "سپتیلیون", "اکتیلیون", "نانیلیون", "دسیلیون"]

    def three_digit_to_words(num):
        num = int(num)
        if num == 0:
            return ""
        s = ""
        s += sadgan[num // 100]
        num %= 100
        if 10 <= num <= 19:
            s += " و " if s else ""
            s += dah_ta_nuzdah[num - 10]
        else:
            if num >= 20:
                s += " و " if s else ""
                s += dahgan[num // 10]
            if num % 10:
                s += " و " if s else ""
                s += yekan[num % 10]
        return s

    if n == 0:
        return "صفر"

    n = str(n).zfill(3 * ((len(str(n)) + 2) // 3))  # Pad to full triplets
    parts = [n[i:i+3] for i in range(0, len(n), 3)]
    result = []
    for i, p in enumerate(parts):
        word = three_digit_to_words(p)
        if word:
            suffix = basex[len(parts) - i - 1]
            result.append(f"{word} {suffix}".strip())
    return " و ".join(result)


# تست با عددهای بزرگ:
print(number_to_words_fa())
