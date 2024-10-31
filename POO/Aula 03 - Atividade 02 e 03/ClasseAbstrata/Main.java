import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        LojaShopping loja1 = new LojaShopping("11111111111111", "Loja A", "Endereço 1", "Gerente A");
        LojaShopping loja2 = new LojaShopping("22222222222222", "Loja B", "Endereço 2", "Gerente B");
        LojaShopping loja3 = new LojaShopping("33333333333333", "Loja C", "Endereço 3", "Gerente C");

        ArrayList<LojaShopping> lojas = new ArrayList<>();
        lojas.add(loja1);
        lojas.add(loja2);
        lojas.add(loja3);

        for (LojaShopping loja : lojas) {
            loja.registraAberturaDia();
            System.out.println(loja.mostrarDados());
        }
    }
}
