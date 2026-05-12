Bug 1 – bug1_fixed.py
Input: ``, n=3

Expected Output: ``

Actual Output: `` 

Note: range(start, len(items)) istifadə edilərək indeks xətası aradan qaldırıldı.

Bug 2 – bug2_fixed.py
Input: n=5; n=0

Expected Output: 120; 1

Actual Output: 120; 1 

Note: result dəyişəni 1-dən başladıldı və n=0 halı üçün xüsusi şərt əlavə edildi.

Bug 3 – bug3_fixed.js
Input: [NaN, 1, 2]; []

Expected Output: 1.5; 0

Actual Output: 1.5; 0 

Note: Number.isNaN yoxlaması və reduce üçün başlanğıc dəyər (0) əlavə edildi.

Bug 4 – bug4_fixed.js
Input: URL (e.g., JSONPlaceholder)

Expected Output: ["ALICE", ...] (Böyük hərflərlə adlar massivi)

Actual Output: ["LEANNE GRAHAM", ...] 

Note: fetch və json() əməliyyatlarından əvvəl await əlavə edilərək asinxronluq təmin edildi.

Bug 5 – bug5_fixed.java
Input: "the cat sat on the mat the cat"; null

Expected Output: "the"; Empty Map/No Crash

Actual Output: "the"; No Crash 

Note: getOrDefault metodu və null yoxlaması ilə NullPointerException aradan qaldırıldı.

Bug 6 – bug6_fixed.py
Input: CSV row Alice,85,90,78

Expected Output: Alice,84.33

Actual Output: Alice,84.33 

Note: Sətir tipli məlumatlar float()-a çevrildi və fayl əməliyyatları with bloku daxilində icra edildi.