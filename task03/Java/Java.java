import java.util.Scanner;

public class Java {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        System.out.println("Prime numbers up to " + n + "are:");
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                System. out.print(i + " ");
            }
        }
        System.out.println();
    }
    
                
    static boolean isPrime(int num) {
        if (num <= 1) return false;
        if (num == 2)return true;
        if (num % 2 == 0) return false;
        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i == 0)return false;
        }
        return true;
   }
  }   
