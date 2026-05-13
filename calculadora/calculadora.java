import java.util.Scanner;
public class Capitulo1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int n1, n2, soma;
        System.out.print("Digite um número: ");
        n1 = entrada.nextInt();
        Sysyem.out.print("Digite outro número: ");
        n2 = entrada.nextInt();
        soma =  n1+ n2;
        System.out.print("Soma = " + soma);
    }

}