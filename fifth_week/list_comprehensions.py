#!/usr/bin/env python3

#saját megoldás
def main():
    print("1. feladat: ")
    li1 = ['auto', 'villamos', 'metro']
    li1_comp = [s.upper() for s in li1]
    print(li1, "->", li1_comp)
    print()

    print("2. feladat: ")
    li2 = ['aladar', 'bela', 'cecil']
    li2_comp = [s.capitalize() for s in li2]
    print(li2, "->", li2_comp)
    print()

    print("3. feladat: ")
    li3 = [0 for n in range(10)]
    print(li3)
    print()

    print("4. feladat: ")
    li4 = [n for n in range(1, 10 + 1)]
    li4_comp = [n+n for n in li4]
    print(li4, "->", li4_comp)
    print()

    print("5. feladat: ")
    li5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    li5_comp = [int(s) for s in li5]
    print(li5, "->", li5_comp)
    print()

    print("6. feladat: ")
    s1 = "1234567"
    li6 = [int(c) for c in list(s1)]
    print(s1, "->", li6)
    print()

    print("7. feladat: ")
    s2 = "The quick brown fox jumps over the lazy dog"
    li7 = [len(s) for s in s2.split(" ")]
    print(s2, "->", li7)
    print()

    print("8. feladat: ")
    s3 = "python is an awesome language"
    li8 = [s[0] for s in s3.split(" ")]
    print(s3, "->", li8)
    print()

    print("9. feladat: ")
    s4 = "The quick brown fox jumps over the lazy dog"
    li9_szavak = [s for s in s4.split(" ")]
    li9_hossz = [len(s) for s in s4.split(" ")]
    li9_comp = [(li9_szavak[i], li9_hossz[i]) for i in range(0, len(li9_szavak))]
    print(s4, "->", li9_comp)
    print()

    print("10. feladat: ")
    li10 = [n for n in range(0, 9 + 1) if n % 2 == 0]
    print(li10)
    print()

    print("11. feladat: ")
    li11 = [n*n for n in range(0, 19 + 1) if n % 2 == 0]
    print(li11)
    print()

    print("12. feladat: ")
    li12 = [n*n for n in range(0, 19 + 1) if str(n * n).endswith("4")]
    print(li12)
    print()

    print("13. feladat: ")
    li13 = [chr(n) for n in range(65, 90 + 1)]
    s5 = "".join([str(c) for c in li13])
    print(li13, "->", s5)
    print()

    print("14. feladat: ")
    li14 = [' apple ', ' banana ', ' kiwi']
    li14_comp = [s.strip() for s in li14]
    print(li14, "->", li14_comp)
    print()

    print("15.feladat: ")
    li15 = [1, 0, 1, 1, 0, 1, 0, 0]
    s6 = "".join([str(c) for c in li15])
    print(li15, "->", s6)
    print()

if __name__ == "__main__":
    main()