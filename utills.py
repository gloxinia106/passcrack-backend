from hangul_utils import split_syllables

kor_to_eng_dic = {
    'ㄱ': 'r', 'ㄴ': 's', 'ㄷ': 'e', 'ㄹ': 'f', 'ㅁ': 'a', 'ㅂ': 'q', 'ㅅ': 't', 'ㅇ': 'd', 'ㅈ': 'w', 'ㅊ': 'c', 'ㅋ': 'z', 'ㅌ': 'x', 'ㅍ': 'v', 'ㅎ': 'g',
    'ㄲ': 'R', 'ㄸ': 'E', 'ㅃ': 'Q', 'ㅆ': 'T', 'ㅉ': 'W',
    'ㅏ': 'k', 'ㅑ': 'i', 'ㅓ': 'j', 'ㅕ': 'u', 'ㅗ': 'h', 'ㅛ': 'y', 'ㅜ': 'n', 'ㅠ': 'b', 'ㅡ': 'm', 'ㅣ': 'l',
    'ㅐ': 'o', 'ㅒ': 'O', 'ㅔ': 'p', 'ㅖ': 'P', 'ㅘ': 'hk', 'ㅙ': 'ho', 'ㅚ': 'hl', 'ㅝ': 'nj', 'ㅞ': 'np', 'ㅟ': 'nl', 'ㅢ': 'ml',
    'ㄳ': 'rt', 'ㄵ': 'sw', 'ㄶ': 'sg', 'ㄺ': 'fr', 'ㄻ': 'fa', 'ㄼ': 'fq', 'ㄽ': 'ft', 'ㄾ': 'fx', 'ㄿ': 'fv', 'ㅀ': 'fg', 'ㅄ': 'qt',
}

def kor_to_eng(text):
    result = ''
    for syllable in split_syllables(text):
        for char in syllable:
            if char in kor_to_eng_dic:
                result += kor_to_eng_dic[char]
            else:
                result += char
    return result