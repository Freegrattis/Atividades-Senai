package Exemplo;
 
public abstract class Felino implements Animal{
    private String nome, cor;
    private int idade;

    public  Felino(String nome, int idade,String cor){
        this.nome = nome;
        this.idade = idade;
        this.cor = cor;
    }

    public String getNome() {
        return this.nome.toUpperCase();
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCor() {
        return this.cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public int getIdade() {
        return this.idade;
    }

    public void setIdade(int idade) {
        if (this.idade<0){
            this.idade = 0;
        }else{
            this.idade = idade;
        }
        
    }
    
    @Override
    public void comer(){
        System.err.println("Comendo!\n");
    }
 
    @Override
    public void dormir(){
        System.out.println("ZZZZ\n");
    }

    public abstract void fazerSom();
    public abstract void brincar();

    public void correr(){
        System.out.println("ZZZZ\n");
    }

}
