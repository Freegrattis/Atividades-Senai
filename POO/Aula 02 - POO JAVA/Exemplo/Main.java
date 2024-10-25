package Exemplo;

public class Main{
    public static void main(String[] args) {

        Gato dory = new Gato("SRD","Dory",2,"Preto");
        dory.brincar();

        Tutor eu = new Tutor("Eu", dory);
        Casa minhaCasa = new Casa("rua do floresta: Longe");
        minhaCasa.adotarGato(dory);
        minhaCasa.chamarMoradores();
    }
}


