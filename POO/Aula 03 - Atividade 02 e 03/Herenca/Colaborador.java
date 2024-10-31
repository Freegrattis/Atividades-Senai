package Herenca;

public class Colaborador extends Pessoa {
    private Departamento departamento;
    private double salario;

    public Colaborador(String nome, String cpf, String endereco, String telefone, Departamento departamento, double salario){
        super(nome, cpf, endereco, telefone);
        this.departamento = departamento;
        this.salario = salario;
    }

    public Departamento getDepartamento() {
        return departamento;
    }

    public void setdepartamento(Departamento departamento) {
        this.departamento = departamento;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    @Override
    public void mostrarDados(){
        super.mostrarDados();
        System.out.println("Departamento: "+getDepartamento());
        System.out.println("Salário: "+getSalario());
    }
}