import java.util.*;
class Main {
public static String rotateLeft(String s, int k) {
int n = s.length();
if (n == 0) return s;
k = myMod(k, n);
StringBuilder rotated = new StringBuilder(n);
for (int i = 0; i < n; i++) {
rotated.append(s.charAt(myMod(i + k, n)));
}
return rotated.toString();
}
public static int myMod(int a, int b) {
if (b == 0) {
throw new ArithmeticException("Modulo by zero is not allowed.");
}
while (a < 0) {
a += b;
}
return a % b;
}
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
String str1 = sc.nextLine();
int rotate = sc.nextInt();
sc.close();
try{
String rotated = rotateLeft(str1, rotate);
System.out.println(rotated);
} catch (ArithmeticException e) {
System.err.println("Error: " + e.getMessage());
}
}
}