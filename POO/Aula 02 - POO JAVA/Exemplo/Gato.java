package Exemplo;

public class Gato extends Felino{

    private String raca;
    
    public Gato(String raca, String nome, int idade, String cor){
        super(nome, idade, cor);
        this.raca = raca;
    }

    public String getRaca() {
        return this.raca;
    }

    public void setRaca(String raca) {
        this.raca = raca;
    }

    @Override
    public void fazerSom(){
        System.out.println("Miau!\n");
    }

    @Override
    public void brincar(){
        System.out.println("Brincando!\n");
    }
    //Sobrescrever
    public void comer(){
        System.out.println("Comendo no pratinho!\n");
    }

    public void correr(){
        System.out.println("Correndo pela casa!\n");
    }

    public void dormir(){
        System.out.println("Dormindo na caixa de papelão!\n");
    }
    //Sobrecarga
    public void comer(String comida){
        System.out.printf("Comendo %s ", comida);
    }

    public void comer(Gato amigo){
        System.out.printf("Comendo a comida do %s ", amigo);
    }

}
