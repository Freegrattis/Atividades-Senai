package Herenca;

public class Cliente extends Pessoa {
    private double valorUltimaCompra;
    private double valorMaiorCompra;

    public double getValorUltimaCompra() {
        return valorUltimaCompra;
    }

    public void setValorUltimaCompra(double valorUltimaCompra) {
        this.valorUltimaCompra = valorUltimaCompra;
    }

    public double getValorMaiorCompra() {
        return valorMaiorCompra;
    }

    public void setValorMaiorCompra(double valorMaiorCompra) {
        this.valorMaiorCompra = valorMaiorCompra;
    }

    public Cliente(String nome, String cpf, String endereco, String telefone, double valorUltimaCompra, double valorMaiorCompra){
        super(nome, cpf, endereco, telefone);
        this.valorUltimaCompra = valorUltimaCompra;
        this.valorMaiorCompra = valorMaiorCompra;
    }

    @Override
    public void mostrarDados(){
        super.mostrarDados();
        System.out.println("Valor Última Compra: "+getValorUltimaCompra());
        System.out.println("Valor Maior Compra: "+getValorMaiorCompra());
    }
}