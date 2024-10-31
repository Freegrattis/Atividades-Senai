package Herenca;

public class Main {
    public static void main(String[] args) {

        Departamento departamento = new Departamento();
        departamento.setDescricao("Teste");
        
        Colaborador colaborador = new Colaborador("Brunno", "12345678910", "Rua Inexistente", "998877665", departamento, 2000);
        
        Cliente  cliente = new Cliente("Bervanda", "12345678911", "Rua dos Sabugos", "741258963",15,3215);

        colaborador.mostrarDados();
        cliente.mostrarDados();
        
    }
}